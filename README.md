How to install:
  1. Download code or clone it: **git clone https://github.com/Yerden01/telegram-avatar-time.git**

Steps:

  1. I used Ubuntu 18.04. If you are using MacOS or Windows use requirements.txt to install packages in step 4 and 5.
  2. Change config/config.py api data to your own. You can take api_data here: https://my.telegram.org/apps
  3. Change timezone to yours in main.py (now it is Asia/Almaty)
  4. (Ubuntu) You have to add run.sh to write and executing access: chmod +x run.sh
  5. (Ubuntu) Then run this command to install all the requirements and run python script: sudo ./run.sh.
  5.(optional). If you close terminal, it won't work, to make it work nonstop, run command: nohup python3 main.py

Also for video avatars, there are some video requirements, you can see codec and resolution info of new2.mp4

Thanks to Krock21rus, mumtozvalijonov

Link to Habr Post: https://habr.com/ru/post/457078/

Feel free to ask or add new features with Pull Request