import os
from psychopy import event, core

def check_skip(key_list=['bracketright']):
    if event.getKeys(keyList=key_list):
        pass

def check_quit(win_to_close, key_list=['backslash'], output_dir='dataraw'):
    if event.getKeys(keyList=key_list):
        win_to_close.close()
        movefiles(output_dir)
        core.quit()

def movefiles(output_dir='dataraw'):
    """[summary]
    
    Args:
        output_dir (str, optional): [description]. Defaults to 'dataraw'.
    """
    files = os.listdir(os.getcwd())
    # create new directory (or the directory to move files to)
    data_dir = os.getcwd() + os.path.sep + output_dir
    
    # move files
    for filename in files:
        if filename.endswith("csv") or filename.endswith("npy") or filename.endswith("txt"):
            if not os.path.exists(data_dir):
                os.mkdir(data_dir)
            new_dir_name = data_dir + os.path.sep + filename
            os.rename(filename, new_dir_name)
            print(f"Moved {filename} to {output_dir + os.path.sep + filename}.")