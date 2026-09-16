# Automated Tech Blog Generator

An autonomous multi-agent AI framework built with **CrewAI**, **LangChain**, and **Groq (Llama 3-70B)**. This system automates the end-to-end process of researching trending technology topics and composing publication-ready blog posts.

---

## 🌟 Architecture Overview

The system uses a sequential multi-agent workflow consisting of specialized AI agents:

1. **Senior News Researcher Agent**:
   - **Role**: Searches for top news stories and reliable sources on a given topic using real-time search tools (`SerperDevTool`).
   - **Output**: A comprehensive research summary synthesized for article writing.

2. **Senior Blog Writer Agent**:
   - **Role**: Takes research findings and crafts a structured, engaging, and readable blog post tailored for public tech audiences.
   - **Output**: Formatted article exported automatically to `blog_post.txt`.

---

## 📁 Repository Structure

```text
agents_proj/
│
├── agents.py           # CrewAI Agent definitions (Researcher & Writer)
├── tasks.py            # Task execution definitions and output configurations
├── tools.py            # SerperDevTool setup for live internet search capabilities
└── main.py             # Entry point to execute the Crew workflow