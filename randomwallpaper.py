import ctypes
import sys
import os
import time
import random

def set_wallpaper(imgpath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imgpath, 0)


def is_img_file(f):
    img_exts = ['.bmp', '.jpg', '.jpeg', '.png', '.tiff']
    return os.path.splitext(f)[1] in img_exts


def main():
    if len(sys.argv) != 3:
        print('Usage: randomwallpaper.py <folder> <minutes per wallpaper>')
        return
    
    while True:
        files = [f for f in os.listdir(sys.argv[1]) if is_img_file(f)]
        set_wallpaper(os.path.join(sys.argv[1], random.choice(files)))
        time.sleep(float(sys.argv[2]) * 60)


if __name__ == '__main__':
    main()