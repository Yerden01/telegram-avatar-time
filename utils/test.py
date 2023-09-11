from datetime import datetime

import moviepy.editor as mp

from utils import generate_new_time_image

video = mp.VideoFileClip("new2.mp4")

image = generate_new_time_image(datetime.now().replace(tzinfo=None))
logo = mp.ImageClip(image).set_duration(video.duration).set_pos(("center", "bottom"))

final = mp.CompositeVideoClip([video.set_position("center"), logo])
final.duration = video.duration
final.write_videofile("test.mp4")
