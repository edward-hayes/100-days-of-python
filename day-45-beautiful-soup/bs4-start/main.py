from bs4 import BeautifulSoup
import requests


url = "http://news.ycombinator.com/news?"
response = requests.get(url)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_titles = soup.select(".titlelink")

article_texts = [title.getText() for title in article_titles]
article_links = [title.get("href") for title in article_titles]
article_upvotes = [int(score.getText().split()[0]) for score in soup.select(".score")]

highest_score = max(article_upvotes)
highest_rated_article = article_upvotes.index(highest_score)

print(f"The highest rated artilce is {article_texts[highest_rated_article]} with a score of {highest_score}\n follow the link here: {article_links[highest_rated_article]}")
print(article_texts)
print(article_links)
print(article_upvotes)

# path_to_file = "website.html"
# with open(path_to_file) as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))


# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")