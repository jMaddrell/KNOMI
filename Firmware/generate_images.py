from os import listdir, makedirs
from os.path import isfile, join, splitext
from optimise_images import optimise

Import("env")

optimise()
gifs = [f for f in listdir('GIFS') if isfile(join('GIFS', f))]

makedirs(join("src", "generated"), exist_ok=True)

for gif in gifs:
    parts = splitext(gif)
    print("Converting: %s" % {parts[0]})
    env.Execute("lv_img_conv GIFS/%s%s -f -c CF_RAW_CHROMA -o src/generated/%s.c" %
                (parts[0], parts[1], parts[0]))
