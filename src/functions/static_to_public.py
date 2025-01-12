from os import listdir, remove, mkdir
from os.path import isfile, join, exists

from shutil import copy, rmtree

def static_to_public():
    if not exists('public') or not exists('static'):
        return
    
    rmtree('public')
    mkdir('public')

    def copy_files_from_directory(directory, path=''):
        tree_elements = listdir(directory)
        for element in tree_elements:
            if isfile(join(directory, element)):
                copy(join(directory, element), join('public', path, element))
            else:
                mkdir(join('public', path, element))
                copy_files_from_directory(join(directory, element), join(path, element))

    copy_files_from_directory('static')

    