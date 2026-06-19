# before moving on, need to remember the python syntax, like the different ways u can import modules/functions
# also understand the libraries you actually imported and what the functions you used do => read spotipy docs
# jog memory on how diff files relate to each other, how functions can be called across files
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

def authenticate():
    load_dotenv()
    client_id = os.environ.get('SPOTIPY_CLIENT_ID')
    client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret) # creates an instance of the SpotifyClientCredentials class, which is used to manage the client credentials for authenticating with the Spotify API. It takes in the client ID and client secret as arguments, which are typically stored in environment variables for security reasons. This manager will handle the authentication process and provide access tokens when making API calls to Spotify.
    sp = spotipy.Spotify(auth_manager=client_credentials_manager) # creates instance of Spotify class, which is used to make API calls to Spotify. It takes in the client credentials manager as an argument, which handles the authentication process for you. You can then use the sp object to call various methods to interact with the Spotify API, such as searching for artists, retrieving playlists, etc.
    return sp

def artist_search(sp, genre):
    artist_info = sp.search(q=f'genre:{genre}', type='artist', limit=10) # searches for artists based on specified genre. Returns dictionary of 10 artists and metadata about those artists.
    items = artist_info['artists']['items'] # artists is overarching key, items is a key that contains a list of 50 dictionaries of each artist's metadata (name, followers, popularity, etc.)
    artist_names = []
    for artist in items:
        artist_names.append(artist['name']) # appends the name of each artist to the artists list
    return artist_names

# def classification(t50):
#     with open('config.yaml', 'r') as f:
#         config = yaml.safe_load(f)

#     artists = []
#     follower_count = []
#     underground = []
#     emerging = []
#     niche = []
#     established = []
#     mainstream = []

#     for i in range(50):
#         artists.append(t50[i]['name']) # appends the name of each artist to the artists list
#         print(t50[0])
#         follower_count.append(t50[i]['followers']['total']) # appends follower count of each artist to list
    
#     paired = sorted(zip(artists, follower_count), key=lambda x: x[1], reverse=True) # sorts the artists and their follower counts in ascending order based on follower count. zip function pairs each artist with their follower count, and sorted function sorts the pairs based on the 1st index (follower count) using a lambda function as the key.
#     names_sorted, followers_sorted = map(list, zip(*paired)) # unzips the sorted pairs into two separate lists. The * operator is used to unpack the paired list of tuples into separate arguments for the zip function, which then groups the first elements and second elements together. The map function is used to convert the resulting tuples back into lists.

#     for i in range(50):
#         if followers_sorted[i] < config['tiers']['underground']['max_followers']:
#             underground.append((names_sorted[i], followers_sorted[i])) # appends the name and follower count of each artist to the underground list as a tuple
#         elif followers_sorted[i] < config['tiers']['emerging']['max_followers']:
#             emerging.append((names_sorted[i], followers_sorted[i])) 
#         elif followers_sorted[i] < config['tiers']['niche']['max_followers']:
#             niche.append((names_sorted[i], followers_sorted[i]))
#         elif followers_sorted[i] < config['tiers']['established']['max_followers']:
#             established.append((names_sorted[i], followers_sorted[i]))
#         else:
#             mainstream.append((names_sorted[i], followers_sorted[i]))
#     return underground[:5], emerging[:5], niche[:5], established[:5], mainstream[:5]
        
    
   


if __name__ == '__main__':
    sp = authenticate()
    results = artist_search(sp, 'indie')
    print(results)
#     underground, emerging, niche, established, mainstream = classification(results)
#     print('Underground:', underground)
#     print('Emerging:', emerging)
#     print('Niche:', niche)
#     print('Established:', established)
#     print('Mainstream:', mainstream)



# what i thought the dictionary looked like
# {
#     'artists': {
#         'items': {
#                name: [name1, name 2, name3,...],
#                followers: [followers1, followers2, followers3,...], 
#                popularity: [popularity1, popularity2, popularity3,...]
#                   }
# }     




    #results = sp.recommendations(seed_genres=[genre], limit=50)
    #tracks = results['tracks']
    
    # extract unique artists from the recommended tracks
    #seen = set()
    #artists = []
    #for track in tracks:
     #   artist = track['artists'][0]
      #  if artist['id'] not in seen:
       #     seen.add(artist['id'])
        #    full_artist = sp.artist(artist['id'])
         #   artists.append(full_artist)
    
    #return artists

  
