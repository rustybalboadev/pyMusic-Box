import json
import requests
import github
import time
import os
import crayons
import toml

with open("config.toml", 'r') as f:
    config = toml.loads(f.read())

last_fm =  config['last_fm']
ghub_token = config['github_token']
gist_id = config['gist_id']
username = config['username']

content = """"""
times = 0
gh = github.Github(ghub_token)
gist = gh.get_gist(gist_id)
while True:
    base_url = requests.get('http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&format=json&period=7day&user={}&api_key={}'.format(username, last_fm)).json()
    user_info = requests.get('http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user={}&api_key={}&format=json'.format(username, last_fm)).json()
    #Top 7 Tracks, you can change the 7 to get how ever many songs :)
    try:
        for x in range(0,7):
            #Get playcount for title
            playcount = user_info['user']['playcount']
            #Get username
            #Get Artist name for that song
            top_artist = base_url['toptracks']['track'][x]['artist']['name']
            #Get Play count for that song
            play_count = base_url['toptracks']['track'][x]['playcount']
            #Get Track name
            top_track = base_url['toptracks']['track'][x]['name']
            #Make the spaces equal. Fucks up if the artist has a symbol
            if len(top_artist) < 24:
                amount = 24 - len(top_artist)
                top_artist = top_artist + " "* amount
            #Make the spaces equal. Fucks up if the artist has a symbol
            if len(top_track) < 27:
                amount = 27 - len(top_track)
                top_track = top_track + " "* amount
            #Make the finishing content
            content += top_artist + "| " + top_track + "Plays:" + play_count + "\n"
    #update the gist!
        last_title = str(gist.files).split("'")[1]
        new_title = '{} | Playcount: {}'.format(username, playcount)
        gist.edit(
            files={last_title: github.InputFileContent(content=content, new_name=new_title)},
        )
    except:
        pass
    times += 1
    os.system('cls')
    print (crayons.red("""
    Uploaded Content
    Times: {}
    Now waiting: 20 min
    """.format(str(times))))
    content = """"""
    time.sleep(1200)
    os.system('cls')
