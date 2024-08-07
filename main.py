import requests

api_key = "f40dff873ecb46c291d4bbfefb2794ff"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-07-07&sortBy=publishedAt&" \
      "apiKey=f40dff873ecb46c291d4bbfefb2794ff"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
