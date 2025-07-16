import time
import os

while True:
    os.system("git add .")
    os.system('git commit -m "Game Data Update"')
    os.system('git push origin main')

    time.sleep(300)
