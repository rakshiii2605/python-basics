import requests

API_KEY = "your_api_key"  # Replace with your NewsAPI key
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    articles = data["articles"]
    for i, article in enumerate(articles[:5], start=1):
        print(f"{i}. {article['title']}")
else:
    print("Error fetching news.")
