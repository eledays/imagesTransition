from moviepy.editor import *
import random
import os
from PIL import Image

k = 7  # Количество строк и столбцов
w, h = 2560, 1440  # Разрешение видео
color = '#191919'  # Цвет фона
clip_duration = .075

# Получаем список изображений и перемешиваем его
names = os.listdir('../png/imgs')

if len(names) < k ** 2:
    raise Exception('Недостаточно изображений')
else:
    random.shuffle(names)
    names = names[:k ** 2]

if 'bg.png' not in os.listdir():
    Image.new('RGB', (w, h), color).save('bg.png')

# Создаем цветной клип, который будет фоном
video = ImageClip('bg.png', duration=clip_duration * k * k, transparent=True)
clips = []

# Добавляем изображения в видеоклип
for row in range(k):
    for col in range(k):
        if not names:
            break
        image_path = f'imgs/{names.pop()}'
        img_clip = (ImageClip(image_path)
                    .set_duration(video.duration - clip_duration * (k ** 2 - (len(names) + 1)))
                    .resize(height=h // k)
                    .set_start(clip_duration * (k ** 2 - (len(names) + 1))))

        position = (col * (w // k), row * (h // k))
        clips.append(img_clip.set_position(position))

# Создаем финальный видеоклип, объединяя фон и изображения
final = CompositeVideoClip([video, *clips], size=(w, h))

# Экспортируем видеоклип в файл
final.write_videofile('exp.mp4', fps=60)

