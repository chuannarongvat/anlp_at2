from bs4 import BeautifulSoup
import requests

url_news = 'https://www.skynews.com.au/world-news/global-affairs/russia-accuses-ukraine-of-drone-strike-which-sparked-a-major-fire-at-a-crimea-fuel-depot/video/e93942202d834a47bc18c3ab0a6fde90'
r = requests.get(url_news)

# Extract the content
c = r.content

# Create a soup object
soup = BeautifulSoup(c, "html.parser")
testNews = str(soup.findAll('p'))

import re

clean = re.compile("<.*?>")
testNews = re.sub(clean, '', testNews)
testNews = re.sub(r'\[|\]', '', testNews)

print(testNews)

with open('testNews.txt', 'w') as f:
    f.write("".join(testNews))


# %%
