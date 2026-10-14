import os
import re
from typing import Generator

from dotenv import load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings
from src.chatbi.config import LLM_CONFIG
from src.chatbi.database import DatabaseClient
from src.chatbi.query_parser import QueryParser
from src.chatbi.result_formatter import ResultFormatter

load_dotenv()
from openai import OpenAI


class LLMClient:
    """LLM客户端类"""

    def __init__(self):
        self.client=OpenAI(
            api_key=LLM_CONFIG["api_key"],
            base_url=LLM_CONFIG["base_url"]
        )
        self.model=LLM_CONFIG["model"]
        self.temperature=LLM_CONFIG["temperature"]
        self.max_tokens=LLM_CONFIG["max_tokens"]

    def generate_sql(self,system_prompt:str,user_query:str) ->str:
        response=self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role":"system","content":system_prompt},
                {"role":"user","content":user_query}
            ]
        )
        content=response.choices[0].message.content.strip()
        sql=re.sub(r'```sql|```','',content)
        return sql

    def generate_text(self, system_msg: str, prompt: str) -> str:
        """
        调用 LLM 生成普通文本（同步，一次性返回）

        Args:
            system_msg: 系统角色消息
            prompt: 完整的用户 Prompt

        Returns:
            模型返回的原始文本内容
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        return response.choices[0].message.content.strip()

    def generate_sql_stream(self, system_msg: str, prompt: str) -> Generator[str, None, None]:
        """
        调用 LLM 流式生成 SQL（逐 chunk 产出）

        Args:
            system_msg: 系统消息
            prompt: 用户提示

        Yields:
            str: 逐段生成的 SQL 文本
        """
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stream=True,
        )

        for chunk in stream:
            delta_content = chunk.choices[0].delta.content
            if delta_content is not None:
                yield delta_content

    def get_embedding(self, text: str) -> list[float]:
        """
        获取输入文本的向量嵌入（embedding）。

        Args:
            text: 待编码的文本字符串。

        Returns:
            文本对应的嵌入向量（浮点数列表）。
        """
        embedding = DashScopeEmbeddings(
            dashscope_api_key=LLM_CONFIG["embedding_api_key"]  # 替换为你的真实密钥[reference:13]
        )
        return embedding.embed_query(text)

if __name__=='__main__':
    llm_client=LLMClient()
    vec=llm_client.get_embedding(text="你好")
    print(vec)