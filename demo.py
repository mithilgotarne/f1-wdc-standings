from moviepy.editor import *
from drivers import *

import os

src_audio = AudioFileClip("media/bg.m4a")

res = []

for id in get_wdc_standings():

    filename = 'media/videos/{}.mov'.format(id)

    if os.path.exists(filename):

        res += [VideoFileClip(filename)]

if len(res) != 20:
    raise SystemExit('[ERROR] No. of drivers should be 20')

res.reverse()

res = [VideoFileClip('media/videos/start.mov')] + res + [VideoFileClip('media/videos/end.mov')]

out: VideoClip = concatenate_videoclips(res)
out = out.resize((1920, 1080)).set_audio(src_audio).set_fps(30)

out.write_videofile("out.mp4", codec='libx264', remove_temp=True)
