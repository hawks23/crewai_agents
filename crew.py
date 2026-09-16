from crewai import Crew, Process
from agents_proj.agents import news_researcher, blog_writer
from agents_proj.tasks import research_task, write_task
import os
# Creating the tech-focused team
groq_api_key = os.getenv("GROQ_API_KEY")
crew = Crew(
    agents = [news_researcher, blog_writer],
    tasks = [research_task, write_task],
    process = Process.sequential,   # This is default, so optional
    #memory = True,
    #cache=True,
    #max_rpm=100,
    #share_crew = True
)

## Start task execution

result = crew.kickoff(inputs = {'topic': 'Apple WWDC 2024'})
print(result)