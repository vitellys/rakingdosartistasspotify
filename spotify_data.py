import os
import requests
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

def get_token():
    try:
        response = requests.post('https://accounts.spotify.com/api/token', data={
            'grant_type': 'client_credentials',
            'client_id': SPOTIFY_CLIENT_ID,
            'client_secret': SPOTIFY_CLIENT_SECRET,
        })
        # Imprime o status e o texto da resposta para depuração
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        response.raise_for_status()  # Levanta um erro para status HTTP 4xx/5xx
        return response.json()['access_token']
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter o token: {e}")
        return None

def get_artist_data(token, artist_id):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}', headers=headers)
    return response.json()

def fetch_data():
    artists = [
        {"name": "Ed Sheeran", "id": "6eUKZXaKkcviH0Ku9w2n3V"},
        {"name": "Queen", "id": "1dfeR4HaWDbWqFHLkxsg1d"},
        {"name": "Ariana Grande", "id": "66CXWjxzNUsdJxJ2JdwvnR"},
        {"name": "Maroon 5", "id": "04gDigrS5kc9YWfZHwBETP"},
        {"name": "Imagine Dragons", "id": "53XhwfbYqKCa1cC15pYq2q"},
        {"name": "Eminem", "id": "7dGJo4pcD2V6oG8kP0tJRR"},
        {"name": "Lady Gaga", "id": "1HY2Jd0NmPuamShAr6KMms"},
        {"name": "Coldplay", "id": "4gzpq5DPGxSnKTe4SA8HAU"},
        {"name": "Beyonce", "id": "6vWDO969PvNqNYHIOW5v0m"},
        {"name": "Bruno Mars", "id": "0du5cEVh5yTK9QJze8zA0C"},
        {"name": "Rihanna", "id": "5pKCCKE2ajJHZ9KAiaK11H"},
        {"name": "Shakira", "id": "0EmeFodog0BfCgMzAIvKQp"},
        {"name": "Justin Bieber", "id": "1uNFoZAHBGtllmzznpCI3s"},
        {"name": "Demi Lovato", "id": "6S2OmqARrzebs0tKUEyXyp"},
        {"name": "Taylor Swift", "id": "06HL4z0CvFAxyc27GXpf02"}
    ]

    token = get_token()
    if not token:
        return {'error': 'Não foi possível obter o token'}

    artist_data = [get_artist_data(token, artist['id']) for artist in artists]

    pop_artists = sorted(
        [artist for artist in artist_data if 'pop' in artist.get('genres', [])],
        key=lambda x: x['followers']['total'],
        reverse=True
    )

    genre_counts = {}
    for artist in artist_data:
        for genre in artist.get('genres', []):
            if genre in genre_counts:
                genre_counts[genre] += 1
            else:
                genre_counts[genre] = 1

    common_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

    return {
        'pop_ranking': [{
            'name': artist['name'],
            'followers': artist['followers']['total'],
            'popularity': artist['popularity']
        } for artist in pop_artists],
        'genre_ranking': [genre for genre, count in common_genres[:5]]
    }
