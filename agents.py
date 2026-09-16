from crewai import Agent
from agents_proj.tools import yt_tool
#from langchain_google_genai import ChatGoogleGenerativeAi
import os
from langchain_community.llms import Ollama
import huggingface_hub

# from langchain_groq import ChatGroq

# llm=Ollama(temperature=0,
#              model="llama3",
#             #  
# )
groq_api_key = os.getenv("GROQ_API_KEY")
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
     
    # api_key="" # Optional if not set as an environment variable
    groq_api_key = os.getenv("GROQ_API_KEY")
    
)

## Senior blog researcher

news_researcher = Agent(
    role = 'News researcher for writing articles',
    goal = 'Find the relevant latest news on topic {topic} from the internet',
    name = 'Senior News Researcher',
    description = 'This agent is responsible for finding relevant news on a specific topic from the internet. The agent will be responsible for finding the best and the most reliable news on the topic and providing a summary of the news for writing the blog post.',
    verbose = True,
    allow_delegation = True,
    # memory = True,
    backstory = 'The agent has been working as a news researcher for the past 2 years and has experience in finding the best and most reliable news for blog posts. The agent has a good understanding of how to search the internet for content on the latest news. He is great at summarizing the news for blog writers to write their blogs.',
    tools = [yt_tool],
    llm=llm,
)

## Senior blog writer

blog_writer = Agent(
    role = 'Blog Writer for Latest News Articles',
    goal = 'Write a blog post summarizing the topic {topic} from the latest news articles found by the news researcher',
    name = 'Senior Blog Writer',
    verbose = True,
    memory = True,
    allow_delegation = True,
    backstory = 'With a flair for simplifying complex topics, he writes engaging narratives that captivate and educate readers. He has a keen eye for detail and a passion for storytelling. He has been writing news blogs for the past 3 years and has experience in writing on a wide range of topics. He is great at turning complex topics into easy-to-understand blog posts.',
    tools = [yt_tool],
    llm=llm,
)