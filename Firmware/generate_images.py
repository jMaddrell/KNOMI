from os import listdir, makedirs
from os.path import isfile, join, splitext

Import("env")

gifs = [f for f in listdir('GIFS') if isfile(join('GIFS', f))]

makedirs(join("generated", "src"), exist_ok=True)

for gif in gifs:
    parts = splitext(gif)
    print("Converting: %s" % {parts[0]})
    env.Execute("lv_img_conv GIFS/%s%s -f -c CF_RAW_CHROMA -o src/%s.c" % (parts[0], parts[1], parts[0]))

# from os import listdir
# from os.path import isfile, join

# lv_img_conv GIFS/Voron/Voron.gif -c CF_RAW_CHROMA -o ...

# env.Execute("lv_img_conv GIFS/%s %s" % (original_file, patched_file))
#     # env.Execute("touch " + patchflag_path)