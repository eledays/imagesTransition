import pyperclip
import requests
import winsound
import os
import time

start = 0
end = 49

for i in range(start, end):
    if i in map(lambda x: int(x.rstrip('.png')), os.listdir('../png/imgs')):
        continue

    while True:
        print(f'Ожидаю {i}-е изображение')
        link = pyperclip.waitForNewPaste()
        try:
            r = requests.get(link)
            with open(f'imgs/{i}.png', 'wb') as file:
                file.write(r.content)
            winsound.Beep(2000, 200)
            break
        except Exception as e:
            for _ in range(3):
                winsound.Beep(2000, 200)
                time.sleep(.1)
            print('err')
            print(e)

winsound.Beep(1500, 200)

