from datetime import datetime
import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image
import moviepy.editor as mp


def convert_time_to_string(dt):
    return dt.strftime("%H:%M")  # f"{dt.hour}:{dt.minute:02}"


def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != convert_time_to_string(prev_time)


def get_black_background(w, h, color):
    return np.full((w, h, 3), color, dtype=np.uint8)


def generate_time_image_bytes(dt):
    W, H = (500, 500)

    text = convert_time_to_string(dt)
    img = get_black_background(500, 500, 0)

    fontpath = "./fonts/digital-7.ttf"

    b, g, r, a = 0, 255, 0, 0

    font = ImageFont.truetype(fontpath, 200)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)

    w, h = draw.textsize(text, font=font)

    draw.text(((W - w) / 2, (H - h) / 2), text, font=font, fill=(b, g, r, a))

    image = np.array(img_pil)

    # text = convert_time_to_string(dt)
    # image = get_black_background()
    # font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    # cv2.putText(img=image, text=text, org=(int(image.shape[0]*0.1), int(image.shape[1]*0.6)), fontFace=font, fontScale=4.5, color=(0, 195, 0), thickness=10)
    # cv2.putText(img=image, text="@yerden4ik", org=(int(image.shape[0]*0.6), int(image.shape[1]*0.8)), fontFace=font, fontScale=1, color=(37, 122, 37), thickness=2)
    _, bts = cv2.imencode('.jpg', image)
    return bts.tobytes()


def generate_new_time_image(dt):
    W, H = (50, 496)

    text = convert_time_to_string(dt)
    img = get_black_background(W, H, 0)

    fontpath = "./fonts/digital-7 (italic).ttf"

    b, g, r, a = 255, 255, 255, 0

    font = ImageFont.truetype(fontpath, 50)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)

    draw.text((216, 5), text, font=font, fill=(b, g, r, a))

    image = np.array(img_pil)

    return image


def generate_video(dt):
    video = mp.VideoFileClip("./utils/new2.mp4").set_duration(5)

    image = generate_new_time_image(dt)
    logo = mp.ImageClip(image).set_duration(video.duration).set_pos(("center", "bottom"))

    final = mp.CompositeVideoClip([video.set_position("center"), logo])
    final.duration = video.duration
    final.write_videofile("./utils/test.mp4")

    return mp.VideoFileClip('./utils/test.mp4')
