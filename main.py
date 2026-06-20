import sys
from spotify import authenticate, artist_search
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

sp = authenticate()

# takes in user input from command line
user_genres = sys.argv[1:]

# checks if user manually inputted genres, if not, uses default genres from config file
if len(user_genres) == 0: # if not user_genres
    user_genres = config['genres']

# runs artist_search function for each genre in user_genres list and prints the results
for genre in user_genres:
    artist_recs = artist_search(sp, genre)
    print(f"Top artists in {genre}: {artist_recs}")