import feedparser
import google.generativeai as genai

# Gemini API key
genai.configure(api_key="AQ.Ab8RN6LSL6ok-20_GxO6rNl7HQnJdLlTDLKNuFco81SBG_dxOQ")

# Google News RSS
url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
news = feedparser.parse(url)

articles = []

for item in news.entries[:15]:
    articles.append(f"Title: {item.title}\nLink: {item.link}")

prompt = """
You are a morning news assistant.

From the following latest news articles:
1. Select the most important stories.
2. Group them into World, Business, Technology and AI.
3. Give a short 2-3 sentence summary for each.
4. Include the source link.
5. Do not invent facts.

News:
""" + "\n\n".join(articles)

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content(prompt)

print(response.text)
