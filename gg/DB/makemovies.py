import requests
import json


TMDB_API_KEY ='5fd7a43ce2aa11c0b6d86d8111209b54'



def get_movie_datas():
    for i in range(1, 100):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        
        response = requests.get(request_url)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code} for page {i}")
            continue

        movies = response.json()
        if 'results' not in movies:
            print(f"Error: 'results' key not found in response for page {i}")
            continue

        for movie in movies['results']:
            if movie.get('adult'): continue
            if not movie.get('poster_path'): continue
            if not movie.get('backdrop_path'): continue
            if movie.get('vote_average') == 10: continue
            if movie.get('release_date', ''):
                fields = {
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'backdrop_path': movie['backdrop_path'],
                    'genres': movie['genre_ids'],
                    'youtube_key': '',
                    'actors': [],
                }

                data = {
                    "model": "movies.movie",
                    "pk": movie['id'],
                    "fields": fields
                }
                print(f"성공:  found in response for page {i}")
                movie_list.append(data)

movie_list = []

get_movie_datas()

file_path = "./moviesample.json"
with open(file_path, 'w', encoding='UTF-8') as outfile:
    json.dump(movie_list, outfile, indent="\t", ensure_ascii=False)
