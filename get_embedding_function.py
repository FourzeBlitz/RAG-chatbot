"""Embed chunks"""
from langchain_community.embeddings.bedrock import BedrockEmbeddings

# # aws embeddings
# def get_embedding_function():
#     embeddings = BedrockEmbeddings(
#        credentials_profile_name='default', region_name='us-east-1'
#     )
#     return embeddings

# ollama embeddings (fully local)
from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function():
    embeddings = OllamaEmbeddings(model='nomic-embed-text')
    return embeddings