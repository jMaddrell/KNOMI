from os import listdir, makedirs
from os.path import isfile, join, splitext
import subprocess
from PIL import Image

src = "./images_raw"
dest = "./images"

gifs = [f for f in listdir(src) if isfile(join(src, f)) and f.endswith('.gif')]
bmps = [f for f in listdir(src) if isfile(
    join(src, f)) and not f.endswith('.gif')]


def optimise():
    makedirs(name=dest, exist_ok=True)

    for gif in gifs:
        subprocess.call(["gifsicle", '--verbose', '--optimize=3', '--lossy=80', join(src, gif),
                        "--colors", '256', "--output", join(dest, gif)])

    for bmp in bmps:
        im = Image.open(join(src, bmp))
        im.save(join(dest, bmp), optimize=True, quality=65)
