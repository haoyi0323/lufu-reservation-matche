#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
鹭府预定匹配工具启动器
"""

import os
import sys
import subprocess
import webbrowser
import time
import threading
import socket
import psutil
import requests
from pathlib import Path

def start_streamlit():
    """启动Streamlit服务"""
    # 获取当前脚本所在目录
    current_dir = Path(__file__).parent
    main_script = current_dir / "streamlit_app.py"
    
    # 启动Streamlit
    cmd = [
        sys.executable, "-m", "streamlit", "run", 
        str(main_script),
        "--server.headless", "true",
        "--server.port", "8501",
        "--browser.gatherUsageStats", "false"
    ]
    
    return subprocess.Popen(cmd, cwd=current_dir)

def check_service_running():
    """检查服务是否已在运行"""
    # 方法1: 检查锁文件
    lock_file = Path(__file__).parent / "app.lock"
    if lock_file.exists():
        try:
            with open(lock_file, 'r') as f:
                pid = int(f.read().strip())
            # 检查进程是否还存在
            if psutil.pid_exists(pid):
                proc = psutil.Process(pid)
                if proc.is_running() and 'streamlit' in ' '.join(proc.cmdline()):
                    return True
            # 如果进程不存在，删除锁文件
            lock_file.unlink()
        except (ValueError, psutil.NoSuchProcess, FileNotFoundError):
            # 锁文件损坏或进程不存在，删除锁文件
            try:
                lock_file.unlink()
            except FileNotFoundError:
                pass
    
    # 方法2: 检查进程
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['cmdline'] and any('streamlit' in str(cmd) and '8501' in str(cmd) for cmd in proc.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    # 方法3: 尝试HTTP请求
    try:
        response = requests.get('http://localhost:8501', timeout=2)
        return True
    except:
        pass
    
    # 方法4: 端口检查
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('localhost', 8501))
            return True
        except:
            return False

def create_lock_file():
    """创建锁文件"""
    lock_file = Path(__file__).parent / "app.lock"
    with open(lock_file, 'w') as f:
        f.write(str(os.getpid()))

def remove_lock_file():
    """删除锁文件"""
    lock_file = Path(__file__).parent / "app.lock"
    try:
        lock_file.unlink()
    except FileNotFoundError:
        pass

def open_browser():
    """延迟打开浏览器"""
    time.sleep(3)  # 等待服务启动
    webbrowser.open("http://localhost:8501")

def main():
    print("🚀 启动鹭府预定匹配工具...")
    
    # 检查服务是否已在运行
    if check_service_running():
        print("⚠️  检测到服务已在运行中！")
        print("📱 请直接访问: http://localhost:8501")
        print("💡 如需重启服务，请先关闭现有程序")
        print("❌ 程序将在5秒后自动退出...")
        time.sleep(5)
        return
    
    # 启动Streamlit服务
    print("🔄 正在启动Streamlit服务...")
    process = start_streamlit()
    create_lock_file()
    
    # 等待服务启动
    print("⏳ 等待服务启动...")
    time.sleep(3)
    
    # 检查进程是否还在运行
    if process.poll() is not None:
        print(f"❌ Streamlit进程异常退出，退出码: {process.returncode}")
        return
    
    # 在新线程中打开浏览器
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    print("✅ 服务已启动！")
    print("📱 浏览器将自动打开，如未打开请手动访问: http://localhost:8501")
    print("❌ 按 Ctrl+C 退出程序")
    
    try:
        # 等待进程结束
        process.wait()
        remove_lock_file()
        print(f"🔚 Streamlit进程已结束，退出码: {process.returncode}")
    except KeyboardInterrupt:
        print("\n🛑 正在关闭服务...")
        process.terminate()
        process.wait()
        remove_lock_file()
        print("✅ 服务已关闭")

if __name__ == "__main__":
    main()