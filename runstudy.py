import pandas as pd
import numpy as np
import random, os, time
from scipy import stats
from psychopy import visual, core, event, data, gui, logging, monitors, sound

from importlib import reload
from exp import instruct
reload(instruct)


exp_objects = {"screen_hz": 60, "fullscreen": False, "monitor": 'testMonitor'}

exp_objects['win'] = visual.Window(size=(1300, 1000), fullscr=exp_objects['fullscreen'], units='norm', monitor=exp_objects['monitor'], colorSpace='rgb', color=(-1, -1, -1)) # create window

exp_objects['mouse'] = event.Mouse(visible=False, win=exp_objects['win'])  # create mouse
exp_objects['mouse'].setVisible(0)  # make mouse invisible

#%% show instructions

exp_objects["txt_space_continue"] = visual.TextStim(win=exp_objects['win'], units='norm', colorSpace='rgb', color=[1, 1, 1], font='Verdana', text="Press space to continue", height=0.04, wrapWidth=1.4, pos=[0.0, 0.0])
    # instructions to be shown
exp_objects["txt_instructions"] = visual.TextStim(win=exp_objects['win'], units='norm', colorSpace='rgb', color=[1, 1, 1], font='Verdana', text='DEFAULT', height=0.08, wrapWidth=1.4, pos=[0.0, 0.5])

instruct.exp_objects = exp_objects
instruct.show_instructions(["hey1", "hey2", "hey3"])
instruct_begin = instruct.Instructions(["hey11", "hey12", "hey13"])
instruct_begin.show_wait()
instruct_begin.show_automatic()
instruct_begin.wait_show() # not implemented yet

exp_objects['win'].close()
core.quit()