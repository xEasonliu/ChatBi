# ChatBi

ChatBi 是一个对话式商业智能（Chat BI）Demo，尝试通过自然语言完成数据查询、分析与可视化，降低数据分析的使用门槛。

## 功能特性

- 自然语言提问，自动理解分析意图
- 自动生成 SQL 并查询数据
- 以表格 / 图表展示查询结果
- 支持多轮对话上下文
- 可配置大模型 API 与数据源
- 适合作为 Chat BI 方向的学习与原型项目

> 请根据项目实际实现增删功能点。

## 技术栈

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)（依赖与虚拟环境管理）
- 大语言模型 API（OpenAI / DeepSeek / 通义千问等，按实际填写）
- SQLAlchemy / SQLite / MySQL / PostgreSQL（按实际填写）
- Streamlit / Gradio / FastAPI（按实际填写）

## 目录结构

```text
ChatBi/
├── data/                 # 示例数据或数据源配置
├── src/
│   └── chatbi/           # 核心代码
│       ├── __init__.py
│       └── ...
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

## 快速开始

### 1. 环境要求

- Python 3.10 或更高版本
- [uv](https://github.com/astral-sh/uv)（推荐）

### 2. 安装依赖

```bash
uv sync
```

### 3. 配置环境变量

在项目根目录创建 `.env` 文件，按实际需要填写：

```env
# 大模型 API 配置
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1

# 数据库配置
DATABASE_URL=sqlite:///data/demo.db
```

### 4. 运行项目

```bash
uv run python -m chatbi
```

如果项目配置了命令行入口，也可以使用：

```bash
uv run chatbi
```

## 使用示例

启动后，在界面或终端中输入自然语言问题，例如：

- “上个月销售额最高的产品是什么？”
- “按地区统计用户数量，并画出柱状图。”
- “对比今年和去年的订单量。”
- “帮我找出最近 7 天增长最快的品类。”

## 开发

```bash
# 安装开发依赖
uv sync --dev

# 运行测试
uv run pytest
```

## 贡献

欢迎提交 Issue 和 Pull Request。

1. Fork 本仓库
2. 创建分支：`git checkout -b feature/your-feature`
3. 提交修改：`git commit -m "feat: add your feature"`
4. 推送分支：`git push origin feature/your-feature`
5. 提交 Pull Request

