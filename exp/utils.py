import os
from psychopy import event, core

def skip():
    pass


def quit():
    pass

def movefiles(output_dir='dataraw'):
    """[summary]
    
    Args:
        outputDir (str, optional): [description]. Defaults to 'Data'.
    """
    files = os.listdir(os.getcwd())

    # create new directory (or the directory to move files to)
    data_dir = os.getcwd() + os.path.sep + output_dir
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    # move files
    for filename in files:
        if filename.endswith("csv") or filename.endswith("npy") or filename.endswith("txt"):
            new_dir_name = data_dir + os.path.sep + filename
            os.rename(filename, new_dir_name)