import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

movie_names = []
movie_ratings = []
movie_votes = []
movie_gross = []
url = "https://www.imdb.com/search/title/?release_date=2017-01-01,&start=1&ref_=adv_nxt"
opended_url = urlopen(url).read()
movie_content = bs(opended_url, "html.parser")
all_movies = movie_content.find_all("div", class_="lister-item mode-advanced")
for movie in all_movies:
    name = movie.h3.a.text
    ratings = movie.find("strong")
    votes = movie.find("span", {"name":"nv"})
    gross = movie.find_all("span", {"name":"nv"})
    movie_names.append(name)
    if ratings is not None:
        movie_ratings.append(ratings.text)
    else:
        movie_ratings.append(ratings)
    if votes is not None:
        movie_votes.append(votes.text)
    else:
        movie_votes.append(votes)
    if gross is not None and len(gross) > 1:
        movie_gross.append(gross[1].text)
    else:
        movie_gross.append("None")
    
# for rating in movie_ratings:
#     print(rating)
# for vote in movie_votes:
#     print(vote)
# for gross in movie_gross:
#     print(gross)

movie_data = pd.DataFrame({
    "name": movie_names,
    "rating": movie_ratings,
    "votes": movie_votes,
    "gross_income": movie_gross
})

print(movie_data.head(10))
