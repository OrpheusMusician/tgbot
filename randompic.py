import requests, os
import random
from PIL import Image

symbols = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"
def searching(pics : int, chat_id):
    url = ["https://i.imgur.com/", ".jpg"]
    while (pics != 0):
        pic_id = ''.join(random.choices(symbols, k = 5))
        link = url[0] + pic_id + url[1]
        r = requests.get(link)
        
        if (r.status_code == 200):
            filename = os.path.join('pics', pic_id + url[1])
            with open (filename, 'wb') as f:
                f.write(r.content)

            with Image.open(filename) as myimage:
                width, height = myimage.size

            if (width * height == 13041):
                os.remove(filename)
            else:
                pics -= 1
                print("[", pics, "]: " + link, chat_id)