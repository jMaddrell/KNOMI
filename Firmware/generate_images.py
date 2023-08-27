from os import listdir, makedirs, path
from os.path import isfile, join, splitext
from optimise_images import optimise
import subprocess
import shutil

images_dir = 'images'
generated_dir = join("src", "generated")

# Import("env")
for dir in [images_dir, generated_dir]:
    if path.exists(dir) and path.isdir(dir):
        print("Removing old %s directory" % (dir))
        shutil.rmtree(dir)

optimise()
images = [f for f in listdir(images_dir) if isfile(join(images_dir, f))]

makedirs(generated_dir, exist_ok=True)

header_prefix = """
#ifndef IMAGES
#define IMAGES

#ifdef __cplusplus
extern "C" {
#endif

#include <lvgl.h>
"""
header_suffix = """
#ifdef __cplusplus
} /* extern "C" */
#endif

#endif
"""

header = header_prefix
code = """
#include "images.h"
#include <lvgl.h>

"""

for image in images:
    parts = splitext(image)
    print("Converting: %s" % {parts[0]})
    input_file = "images/%s%s" % (parts[0], parts[1])
    output_file = "src/generated/%s.c" % (parts[0])
    subprocess.call(["lv_img_conv", input_file, "-f", "-c",
                    "CF_RAW_CHROMA", "-o", output_file])
    header += """
extern lv_obj_t *img_%s;
void image_%s_display();
    """ % (parts[0], parts[0])

    code += """
LV_IMG_DECLARE(%s);
lv_obj_t *img_%s;
void image_%s_display() {
    img_%s = lv_img_create(lv_scr_act());
    lv_img_set_src(img_%s, &%s);
    lv_obj_align(img_%s, LV_ALIGN_CENTER, 0, 0);
}
    """ % (parts[0], parts[0], parts[0], parts[0], parts[0], parts[0], parts[0])

header += header_suffix

with open(join(generated_dir, "images.h"), "w") as f:
    f.write(header)

with open(join(generated_dir, "images.cpp"), "w") as f:
    f.write(code)
