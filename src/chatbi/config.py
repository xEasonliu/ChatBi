import os

from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "chatbi_mvp"),
    "charset": "utf8mb4"
}

LLM_CONFIG = {
    "api_key": os.getenv("DEEPSEEK_API_KEY"),
    "base_url": os.getenv("OPENAI_BASE_URL"),
    "model": os.getenv("LLM_MODEL"),
    "temperature":0.2,
    "max_tokens":2000,
    "embedding_api_key":"sk-ws-H.ERIDXHD.qzGZ.MEUCIB_W7LNwCWnyMojpsb_4Y3nPLjzlXQG5FphABqJSxruiAiEA_V_P8gpAq_GPRhxIYQMIoXTuwEUD-X3nlCsjO_uFYy0"
}

EMBEDDING_CONFIG={
    "embedding_model":"qwen-embedding",
    "base_url":"https://ws-pwpt874gw09j1p2f.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    "api_key":"sk-ws-H.ERIDXHD.qzGZ.MEUCIB_W7LNwCWnyMojpsb_4Y3nPLjzlXQG5FphABqJSxruiAiEA_V_P8gpAq_GPRhxIYQMIoXTuwEUD-X3nlCsjO_uFYy0"
}
