import shutil
from main import PATH_TO_GRADING

"""
Deletes the grading folder
Use after grading is complete to remove all contents of grading folder
"""


def delete():
    try:
        shutil.rmtree(PATH_TO_GRADING)
    except:
        print('Error while deleting directory')


delete()
