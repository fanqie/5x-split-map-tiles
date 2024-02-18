import os
import shutil
from dotenv import load_dotenv

from src.split_and_save_tiles import split_and_save_tiles
from src.get_absolute_path import get_absolute_path

load_dotenv()


def main():
    input_folder = get_absolute_path(os.getenv("INPUT_DIR"))
    output_folder = get_absolute_path(os.getenv("OUTPUT_DIR"))
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        shutil.rmtree(output_folder)
        os.mkdir(output_folder)
        print("Output folder")
    for level in range(int(os.getenv("LEVEL_MAX"))):
        level_folder = f"{output_folder}/{level}"
        if not os.path.exists(level_folder):
            os.mkdir(level_folder)
        split_and_save_tiles(input_folder, level + 1, level_folder)
    print("Done!")


if __name__ == "__main__":
    main()
