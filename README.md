# 🚀 鹭府预定匹配工具

一个基于Streamlit的智能预订信息与美团订单匹配工具，帮助餐饮企业提高订单管理效率。

## ✨ 功能特性

- 🔍 **智能匹配**: 自动匹配预订信息与美团订单
- 📊 **数据分析**: 提供详细的匹配统计和分析图表
- 🎯 **手动匹配**: 支持手动调整和匹配记录
- 📤 **数据导出**: 导出匹配结果和分析报告
- 🌐 **Web界面**: 现代化的Web用户界面

## 🛠️ 技术栈

- **后端**: Python 3.11+
- **Web框架**: Streamlit
- **数据处理**: Pandas
- **图表可视化**: Plotly
- **部署**: Docker, Heroku, Railway, Streamlit Cloud

## 🚀 快速开始

### 本地运行

1. **克隆项目**
   ```bash
   git clone <your-repo-url>
   cd 鹭府预定匹配工具
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **运行应用**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **访问应用**
   打开浏览器访问 http://localhost:8501

### Docker运行

```bash
# 构建镜像
docker build -t streamlit-app .

# 运行容器
docker run -p 8501:8501 streamlit-app

# 或使用docker-compose
docker-compose up -d
```

## 🌐 云端部署

本项目支持多种云端部署方案，详细说明请查看 [部署指南.md](./部署指南.md)

### 推荐部署方案

1. **Streamlit Cloud** - 最简单，专为Streamlit应用设计
2. **Railway** - 现代化，免费额度充足
3. **Heroku** - 经典选择，稳定可靠

## 📁 项目结构

```
鹭府预定匹配工具/
├── streamlit_app.py      # 主应用文件
├── requirements.txt      # Python依赖
├── Dockerfile           # Docker配置
├── docker-compose.yml   # Docker Compose配置
├── Procfile            # Heroku部署配置
├── railway.json        # Railway部署配置
├── .streamlit/         # Streamlit配置
│   └── config.toml
├── .github/            # GitHub Actions
│   └── workflows/
├── 部署指南.md          # 详细部署说明
└── README.md           # 项目说明
```

## 🔧 配置说明

### Streamlit配置

主要配置在 `.streamlit/config.toml` 文件中：

```toml
[server]
headless = true
enableCORS = false
enableXsrfProtection = false
port = 8501

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
```

### 环境变量

- `STREAMLIT_SERVER_PORT`: 服务端口
- `STREAMLIT_SERVER_ADDRESS`: 服务地址
- `STREAMLIT_SERVER_HEADLESS`: 无头模式

## 📊 使用说明

1. **上传文件**: 上传预订Excel文件和美团订单Excel文件
2. **开始匹配**: 点击"开始匹配"按钮进行自动匹配
3. **查看结果**: 浏览匹配统计和详细信息
4. **手动调整**: 使用手动匹配功能调整结果
5. **导出数据**: 下载匹配结果和分析报告

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

本项目采用MIT许可证。

## 📞 技术支持

如有问题，请查看 [部署指南.md](./部署指南.md) 或提交Issue。

---

**让预订管理变得更简单！** 🎉
