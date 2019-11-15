"""
Use this file to run tasks/experiments.
DO NOT EDIT unless you know what you're doing!
"""


import pandas as pd
import numpy as np
import random, os, time
from scipy import stats
from psychopy import visual, core, event, data, gui, logging, monitors, sound

from importlib import reload
from exp import instruct, utils
from tasks import stroop
reload(instruct)
reload(utils)

exp_objects = {"win_size": (500, 500), "screen_hz": 60, "fullscreen": False, "monitor": 'testMonitor', "dataraw_dir": "dataraw_TEST", "skip_keys": ["bracketright"], "quit_keys": ["backslash"]}

exp_objects['win'] = visual.Window(size=exp_objects["win_size"], fullscr=exp_objects['fullscreen'], units='norm', monitor=exp_objects['monitor'], colorSpace='rgb', color=(-1, -1, -1)) # create window

exp_objects['mouse'] = event.Mouse(visible=False, win=exp_objects['win'])  # create mouse
exp_objects['mouse'].setVisible(0)  # make mouse invisible

#%% show instructions

exp_objects["txt_space_continue"] = visual.TextStim(win=exp_objects['win'], units='norm', colorSpace='rgb', color=[1, 1, 1], font='Verdana', text="Press space to continue", height=0.04, wrapWidth=1.4, pos=[0.0, 0.0])
exp_objects["txt_instructions"] = visual.TextStim(win=exp_objects['win'], units='norm', colorSpace='rgb', color=[1, 1, 1], font='Verdana', text='DEFAULT', height=0.08, wrapWidth=1.4, pos=[0.0, 0.5])

instructions = instruct.Instructions(exp_objects, ["hey11", "hey12", "hey13"])
instructions.show_wait()
instructions.show_wait(text=["a", "b", "c"])

instructions.set_text(["new1", "new2"])
instructions.show_automatic()
instructions.show_automatic(text=["e", "f"])

instructions.wait_show(text=["abc", "cde"])

#%% test stroop module

stroop.run_task(exp_objects)

#%% finish

exp_objects['win'].close()
utils.movefiles(exp_objects["dataraw_dir"])
core.quit()