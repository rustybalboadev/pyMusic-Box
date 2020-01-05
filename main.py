import json
import requests
import github
import time
last_fm = '' #Last FM Key created at: https://www.last.fm/api/account/create
ghub_token = '' #Github token found in User Profile > Settings > Developer Settings
gist_id = '' #your gist id (found in url of gist)
username = '' # LastFM Username
base_url = requests.get('http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&format=json&period=7day&user={}&api_key={}'.format(username, last_fm)).json()
content = """"""
gh = github.Github(ghub_token)
gist = gh.get_gist(gist_id)
#Top 7 Tracks, you can change the 7 to get how ever many songs :)
for x in range(0,7):
    #Get Artist name for that song
    top_artist = base_url['toptracks']['track'][x]['artist']['name']
    #Get Play count for that song
    play_count = base_url['toptracks']['track'][x]['playcount']
    #Get Track name
    top_track = base_url['toptracks']['track'][x]['name']
    #Make the spaces equal. Fucks up if the artist has a symbol
    if len(top_artist) < 15:
        amount = 15 - len(top_artist)
        top_artist = top_artist + " "* amount
    #Make the spaces equal. Fucks up if the artist has a symbol
    if len(top_track) < 30:
        amount = 30 - len(top_track)
        top_track = top_track + " "* amount
    #Make the finishing content
    content += top_artist + "| " + top_track + "Plays:" + play_count + "\n"
#update the gist!
gist.edit(
    files={'My Week Of Music': github.InputFileContent(content=content)},
)

 
