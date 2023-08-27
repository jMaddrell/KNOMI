from os import listdir, makedirs
from os.path import isfile, join, splitext
from optimise_images import optimise
import subprocess

# Import("env")

optimise()
images = [f for f in listdir('images') if isfile(join('images', f))]

makedirs(join("src", "generated"), exist_ok=True)

for image in images:
    parts = splitext(image)
    print("Converting: %s" % {parts[0]})
    input_file = "images/%s%s" % (parts[0], parts[1])
    output_file = "src/generated/%s.c" % (parts[0])
    subprocess.call(["lv_img_conv", input_file, "-f", "-c", "CF_RAW_CHROMA", "-o", output_file])
