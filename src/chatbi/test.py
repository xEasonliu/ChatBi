from langchain_community.embeddings import DashScopeEmbeddings
from langchain_openai import OpenAIEmbeddings

from chatbi.config import EMBEDDING_CONFIG

embedding=DashScopeEmbeddings()

if __name__=='__main__':
    vec=embedding.embed_query("你好")
    print(vec)