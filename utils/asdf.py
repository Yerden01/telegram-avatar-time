from utils import time_has_changed, generate_time_image_bytes, generate_time_image
import moviepy.editor as mp
from datetime import datetime, timedelta
import cv2

video = mp.VideoFileClip("bilal.mp4")

image = generate_time_image(datetime.now().replace(tzinfo=None))
# cv2.imshow('image', image)
# cv2.waitKey(0)
logo = mp.ImageClip(image).set_duration(video.duration).set_pos(("center", "bottom"))

final = mp.CompositeVideoClip([video.set_position("center"), logo])
final.duration = video.duration
final.write_videofile("test.mp4")
