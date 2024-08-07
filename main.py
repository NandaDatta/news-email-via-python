import requests
from send_email import send_email

topic = "tesla"
api_key = "f40dff873ecb46c291d4bbfefb2794ff"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&"\
      "from=2024-07-07&sortBy=publishedAt&" \
      "apiKey=f40dff873ecb46c291d4bbfefb2794ff&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
subject = "Today's News"
for article in content['articles'][:20]:
    title = article["title"] if article["title"] is not None else "No Title"
    description = article["description"] if article["description"] is not None else "No Description"
    url = article['url']
    body += "Subject: Today's News" + "\n" + title + "\n" + description + "\n" + url + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
