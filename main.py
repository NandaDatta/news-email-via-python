import requests
from send_email import send_email

api_key = "f40dff873ecb46c291d4bbfefb2794ff"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-07-07&sortBy=publishedAt&" \
      "apiKey=f40dff873ecb46c291d4bbfefb2794ff"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content['articles']:
    title = article["title"] if article["title"] is not None else "No Title"
    description = article["description"] if article["description"] is not None else "No Description"
    body = body + title + "\n" + description + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
