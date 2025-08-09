@echo off
chcp 65001 >nul
echo 🚀 正在启动鹭府预定匹配工具...
echo.
echo 📋 检查Python环境...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 未检测到Python环境！
    echo 📥 请先安装Python 3.8或更高版本
    echo 🌐 下载地址: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo ✅ Python环境正常
echo 📦 检查依赖包...

python -c "import streamlit" >nul 2>&1
if %errorlevel% neq 0 (
    echo 📥 正在安装streamlit...
    pip install streamlit
)

python -c "import pandas" >nul 2>&1
if %errorlevel% neq 0 (
    echo 📥 正在安装pandas...
    pip install pandas
)

python -c "import plotly" >nul 2>&1
if %errorlevel% neq 0 (
    echo 📥 正在安装plotly...
    pip install plotly
)

echo ✅ 依赖包检查完成
echo 🚀 启动应用...
echo.
python launcher.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ 程序启动失败！
    echo 💡 请检查错误信息或联系技术支持
    pause
)