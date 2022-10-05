import time
from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from config import users
from utils import time_has_changed, generate_time_image_bytes, generate_video
from datetime import datetime, timedelta
import argparse
import pytz


def valid_tz(s):
    try:
        return pytz.timezone(s)
    except:
        msg = "Not a valid tz: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


clients = []

for user in users:
    print("Starting parsing user: ", user[0])
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_id", required=False, help="user api ID", type=str, default=user[1])
    parser.add_argument("--api_hash", required=False, help="user api Hash", type=str, default=user[2])
    parser.add_argument("--tz", required=False, help="user api Hash", type=valid_tz, default=valid_tz('Asia/Almaty'))

    args = parser.parse_args()

    createdClient = TelegramClient(user[0], args.api_id, args.api_hash)
    createdClient.start()

    clients.append(createdClient)


async def main():
    prev_update_time = datetime.now() - timedelta(minutes=1)

    while True:
        if time_has_changed(prev_update_time):

            for ind in range(len(clients)):
                client = clients[ind]
                if users[ind][3] == 'video':
                    generate_video(datetime.now(args.tz).replace(tzinfo=None))
                    await client(DeletePhotosRequest(await client.get_profile_photos('me')))
                    file = await client.upload_file('./utils/test.mp4')
                    await client(UploadProfilePhotoRequest(video=file))
                else:
                    bts = generate_time_image_bytes(datetime.now(args.tz).replace(tzinfo=None))
                    await client(DeletePhotosRequest(await client.get_profile_photos('me')))
                    file = await client.upload_file(bts)
                    await client(UploadProfilePhotoRequest(file))

            prev_update_time = datetime.now()
            time.sleep(1)


if __name__ == '__main__':
    import asyncio

    asyncio.get_event_loop().run_until_complete(main())
