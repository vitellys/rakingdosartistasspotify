import requests

url = "https://psel-solution-automation-cf-ubqz773kaq-uc.a.run.app?access_token=bC2lWA5c7mt1rSPR"
headers = {"Content-Type": "application/json"}


data = {

"github_url": "https://github.com/vitellys/rakingdosartistasspotify",
"name": "Ellen Rebeca Simões de Albuquerque",

"pop_ranking": [
{
"artist_name": "Taylor Swift",
"followers": "118971229"
},
{
"artist_name": "Ed Sheeran",
"followers": "115389739"
},
{
"artist_name": "Ariana Grande",
"followers": "98814719"
},
{
"artist_name": "Justin Bieber",
"followers": "76626180"
},
{
"artist_name": "Rihanna",
"followers": "61941130"
},
{
"artist_name": "Bruno Mars",
"followers": "57920481"
},
{
"artist_name": "Imagine Dragons",
"followers": "53945441"
},
{
"artist_name": "Coldplay",
"followers": "52479985"
},
{
"artist_name": "Maroon 5",
"followers": "42305459"
},
{
"artist_name": "Beyoncé",
"followers": "38281054"
},
{
"artist_name": "Shakira",
"followers": "34056123"
},
{
"artist_name": "Lady Gaga",
"followers": "30970792"
},
{
"artist_name": "Demi Lovato",
"followers": "26667120"
}

],

"genre_ranking": [

"pop",
"dance pop",
"rock",
"singer-songwriter pop",
"uk pop"

]

}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.text)




