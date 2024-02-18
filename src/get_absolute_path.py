import os
import sys


def get_absolute_path(path):
    if os.path.isabs(path):
        return path
    else:
        main_dir = os.path.dirname(sys.argv[0])
        abs_path = os.path.join(main_dir, path)
        return abs_path

