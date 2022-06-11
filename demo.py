from moviepy.editor import *
import random
import requests
import os

src_audio = AudioFileClip("media/bg.m4a")

res = []

response = requests.get('https://ergast.com/api/f1/current/driverStandings.json')

for driver in response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']:

    id = driver['Driver']['driverId']

    filename = 'media/videos/{}.mov'.format(id)

    if os.path.exists(filename):

        res += [VideoFileClip(filename)]

res.reverse()

res = [VideoFileClip('media/videos/start.mov')] + res + [VideoFileClip('media/videos/end.mov')]

out: VideoClip = concatenate_videoclips(res)
out = out.set_audio(src_audio) 

out.write_videofile("out.mp4", codec='libx264', audio_codec='aac',
                    temp_audiofile='temp-audio.m4a', remove_temp=True)
