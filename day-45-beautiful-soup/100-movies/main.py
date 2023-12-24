from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import lxml

# load dynamic content and save page source to variable
url = "https://www.empireonline.com/movies/features/best-movies-2/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
html = driver.page_source

# parse the page source
soup = BeautifulSoup(html,"lxml")

# grab the movie titles from the H3 elements on the page and store as list
movie_headers = soup.find_all(name="h3", class_="jsx-4245974604")
movies = [movie.getText() for movie in movie_headers]
movies.reverse()

# write list to file
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")