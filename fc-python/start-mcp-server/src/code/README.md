# FC SSE Mcp Server

基于 FastMCP 和 Starlette 构建的 Serverless 服务端事件(SSE)应用

## 功能特性

- 使用 FastMCP 框架实现 SSE 协议支持
- 集成 Starlette 高性能 ASGI 服务器
- 提供示例工具端点 `hello` 返回 "Hello World!"
- 支持阿里云函数计算部署

## 快速开始

### 环境要求

- Python ≥3.10
- pip 包管理工具

### 安装依赖

```bash
pip install -r requirements.txt
```

### 本地运行

```bash
uvicorn main:app --host 0.0.0.0 --port 9000
```

## 项目结构

start-mcp-server/
├── src/
│ ├── code/
│ │ ├── main.py # 主应用入口
│ │ └── pyproject.toml # 依赖配置
└── s.yaml # Serverless 部署配置
