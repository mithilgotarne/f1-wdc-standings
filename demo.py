from moviepy.editor import *
from drivers import *
import os
import argparse

parser = argparse.ArgumentParser(description="Create WDC standings intro video")
parser.add_argument("-y", "--year", type=int, help="The year for which you want to create the video")

args = parser.parse_args()

year = datetime.datetime.now().year

if args.year:
    year = args.year


src_audio = AudioFileClip(f"media/{year}/bg.m4a")

res = []

for id in get_wdc_standings(year):

    filename = f'media/{year}/videos/{id}.mov'

    if os.path.exists(filename):

        res += [VideoFileClip(filename)]

if len(res) != 20:
    raise SystemExit('[ERROR] No. of drivers should be 20')

res.reverse()

res = [VideoFileClip(f'media/{year}/videos/start.mov')] + res + \
    [VideoFileClip(f'media/{year}/videos/end.mov')]

clip: VideoClip = concatenate_videoclips(res)

resolution = (1920, 1080)


clip = clip.resize(resolution)

clip = clip.set_audio(src_audio)
clip = clip.set_fps(30)

clip.write_videofile("out.mp4", codec='libx264', audio_codec="aac", remove_temp=True,)
