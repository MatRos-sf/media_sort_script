import datetime
import logging
import os
import shutil
import traceback
from pathlib import Path

picture = ('.jpg', '.JPG')
video = ('.mp4', '.MP4')

# main directory where it will be create new one
DIR_MAIN = 'E:\\Document\\Obrazy'
# directory path that include all media
DIR_MEDIA = 'E:\\Document\\Obrazy\\0_sortowanie'


def name_directory():
    """
    Function create new directory
    :return: main name which it will be names directory and files
    """

    # podanie nazwy katalogu
    name_directory = input("Enter a directory name: ")
    name_year = input("Enter the year: ")

    name_directory = name_directory.lower().replace(' ', '_')

    if not name_year:
        name_year = str(datetime.datetime.now().year)

    os.chdir(DIR_MAIN)
    directories = os.listdir()
    full_name = name_directory + '_' + name_year
    if full_name in directories:
        return
    else:
        return full_name


def create_directory(name):
    """
    Function creates tree directory:
        -name
             ----video
             ----photo
    :param name: name new directory
    :return: two paths:
            -directory photo
            -directory video
    """

    Path(name).mkdir(exist_ok=True)
    os.chdir(DIR_MAIN + '\\' + name)
    Path('photo').mkdir(exist_ok=True)
    Path('video').mkdir(exist_ok=True)

    return os.getcwd() + '\\photo\\', os.getcwd() + '\\video\\'


def move_file(path, name_file):
    """
    Function copies files from DIR_MEDIA to DIR_MAIN + \\name_directory\video_or_photo
    :param path: target path (DIR_MAIN + \\name_directory\video_or_photo)
    :param name_file: name single file
    :return: None
    """
    original_path = os.getcwd() + '\\' + name_file
    target_path = path + name_file

    shutil.copyfile(original_path, target_path)

    os.remove(original_path)


if __name__ == '__main__':

    while True:
        name = name_directory()
        if name:
            print(f"Name directory: {name}")
            break
        else:
            print("Directory exist. Try again.")

    os.chdir(DIR_MAIN)

    # create directory
    photo_path, video_path = create_directory(name)

    # rename file and remove to directory
    os.chdir(DIR_MEDIA)

    for index, file in enumerate(os.listdir()):
        f = Path(file)
        suffix_name = f.suffix
        new_name = f"{name}_{index}{suffix_name}"
        f.rename(new_name)
        if suffix_name in video:
            try:
                move_file(video_path, new_name)
            except Exception as e:
                print(f"Something is wrong:\n {logging.error(traceback.format_exc())}")
        elif suffix_name in picture:
            try:
                move_file(photo_path, new_name)
            except Exception as e:
                print(f"Something is wrong:\n {logging.error(traceback.format_exc())}")
        else:
            print(f"inny format {suffix_name}")
    os.chdir(DIR_MAIN + '\\' + name)

    print(f"Done. \nDirectory: {os.getcwd()}")
