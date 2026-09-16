from crewai import Task
from agents_proj.tools import yt_tool
from agents_proj.agents import news_researcher, blog_writer

## Research Task
research_task = Task(
    description =(
        "Identify the latest news on the topic {topic} from Google search."
        "Get detailed information about the news from the internet's most reliable sources and summarize the content for the blog."
    ),
    expected_output = "A comprehensive 3 paragraph long report based on the {topic} of news content.",
    tools = [yt_tool],
    agents = [news_researcher]
)

## Writing Task

write_task = Task(
    description =(
        "Get the information on the topic {topic} from the news researcher and create eye catching content for the blog."
    ),
    expected_output = "A well-written and informative blog post on the topic {topic}",
    async_exectution = False,   ## Not parallel processing coz we need the research first
    agents = [blog_writer],
    output_files = ['blog_post.txt']
)