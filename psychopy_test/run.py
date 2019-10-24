# https://www.knowledgehut.com/blog/programming/run-python-scripts
# https://discourse.psychopy.org/t/open-experiments-using-code-in-a-preceding-experiment/1066/4

import os 
print(os.getcwd())

from psychopy import core
# import scripts
# from scripts import s1
# from scripts import s2

import os
# doesn't work
# os.rename('data/abc.txt', '/Volumes/inzlicht-shared/Behavioural/Computer 1/test/abc.txt')

# https://stackoverflow.com/questions/26765130/how-can-i-move-files-between-mounts-using-python
# https://www.codespeedy.com/difference-between-os-rename-and-shutil-move-in-python/
import shutil # works
shutil.copy('data/abc.txt', '/Volumes/inzlicht-shared/Behavioural/Computer 1/test/abc.txt')
# os.rename('data/abc.txt', "/Users/hause/Desktop/untitled folder/abc.txt")

# import importlib
#importlib.reload(scripts.s1)
#importlib.reload(scripts.s2)


#import runpy
#runpy.run_module('./scripts/s1.py')
#runpy.run_module('./scripts/s2.py')


# print(dir(scripts))
#print('run script 1')
#exec(open('./scripts/s1.py').read())
#print('finish script 1')
#print('run script 2')
#exec(open('./scripts/s2.py').read())
#print('finish script 2')

core.quit()