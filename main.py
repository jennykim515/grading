#################################################################################################
#                                                                                               #
#   name:   Jenny Kim                                                                           #
#   email:  yjkim@usc.edu                                                                       #
#                                                                                               #
#   How To: Define global variables - downloads and grading paths                               #
#################################################################################################
import os
import re
import zipfile
from pathlib import Path

# TODO: Define downloads and grading path
PATH_TO_DOWNLOADS = ""
PATH_TO_GRADING = ""


# Move files to designated grading folder and removes them from Downloads
def move_files():
    items = os.listdir(PATH_TO_DOWNLOADS)
    os.mkdir(PATH_TO_GRADING)
    for file in items:
        if file.endswith('.zip') or re.search("a.+_.+_.+", file) or re.search("lab.+_", file):
            Path(PATH_TO_DOWNLOADS + "/" + file).rename(PATH_TO_GRADING + "/" + file)


def unzip():
    for item in os.listdir(PATH_TO_GRADING):
        if item.endswith('.zip'):
            with zipfile.ZipFile(PATH_TO_GRADING + "/" + item, 'r') as zip_ref:
                zip_ref.extractall(PATH_TO_GRADING)
                os.remove(PATH_TO_GRADING + "/" + item)


def main():
    move_files()
    unzip()


main()


