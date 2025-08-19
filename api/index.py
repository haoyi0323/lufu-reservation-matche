from streamlit.web import cli as stcli
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    # 设置Streamlit配置
    sys.argv = [
        "streamlit",
        "run",
        "streamlit_app.py",
        "--server.port=8000",
        "--server.address=0.0.0.0",
        "--server.headless=true",
        "--server.enableCORS=false",
        "--server.enableXsrfProtection=false"
    ]
    
    # 切换到项目根目录
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # 启动Streamlit
    stcli.main()

if __name__ == "__main__":
    main()