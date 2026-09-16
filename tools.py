from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
import os
from crewai_tools import SerperDevTool
groq_api_key = os.getenv("GROQ_API_KEY")
# Initialize the tool for internet searching capabilities
yt_tool = SerperDevTool()