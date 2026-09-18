import os
import feedparser
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
news = feedparser.parse(url)

articles = []

for item in news.entries[:15]:
    articles.append(
        f"Title: {item.title}\nLink: {item.link}"
    )

prompt = """
You are a morning news assistant.

Select the most important news from these articles.

Group them into:
1. World
2. Business
3. Technology
4. AI

For each story provide:
- Headline
- Short summary
- Source link

Do not invent information.

News:
""" + "\n\n".join(articles)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
