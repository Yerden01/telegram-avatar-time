
# Telegram avatar time

The Real-Time Telegram Avatar Updater is an project designed to add a touch of dynamism and creativity to your Telegram profile. This project continuously updates your Telegram profile picture every minute with captivating images or videos of a clock, creating a visually engaging and personalized experience.
### Image example
![Telegram Avatar Image](https://i.ibb.co.com/Zx6zfB5/Screenshot-2023-09-11-at-15-38-48.png)
### Video Example

![Telegram Video Avatar](https://i.ibb.co.com/pxbvzzj/clideo-editor-eab61543992947f4a9a9d451a0de6650.gif)


## How to install:
Download code or clone it: **git clone https://github.com/Yerden01/telegram-avatar-time.git**

Steps:
  1. I used Ubuntu 18.04. If you are using MacOS or Windows use requirements.txt to install packages in step 4 and 5.
  2. Change config/config.py api data to your own. You can take api_data here: https://my.telegram.org/apps
  3. Change timezone to yours in main.py (now it is Asia/Almaty)
  4. (Ubuntu) You have to add run.sh to write and executing access: chmod +x run.sh
  5. (Ubuntu) Then run this command to install all the requirements and run python script: sudo ./run.sh.
  6. (optional). If you close terminal, it won't work, to make it work nonstop, run command: ```nohup python3 main.py```
\
**Also for video avatars, there are some video requirements, you can see codec and resolution info of new2.mp4**

Thanks to Krock21rus, mumtozvalijonov

Link to Habr Post: https://habr.com/ru/post/457078/

Feel free to ask or add new features with Pull Request