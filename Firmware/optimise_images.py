from os import listdir, makedirs
from os.path import isfile, join, splitext
import subprocess

# Import("env")

src = "./GIFS_Raw"
dest = "./GIFS"

gifs = [f for f in listdir(src) if isfile(join(src, f))]

# sources = list(map(lambda f: join(src, f), gifs))


def optimise():
    makedirs(name=dest, exist_ok=True)

    for gif in gifs:
        subprocess.call(["gifsicle", '--verbose', '--optimize=3', '--lossy=80', join(src, gif),
                        "--colors", '256', "--output", join(dest, gif)])


# gifsicle(
#     sources=sources,  # or a single_file.gif
#     # or just omit it and will use the first source provided.
#     destination=dest,
#     optimize=True,  # Whetever to add the optimize flag of not
#     colors=256,  # Number of colors t use
#     options=["--verbose"]  # Options to use.
# )
