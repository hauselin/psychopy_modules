import pandas as pd
import numpy as np
import random, os, time
from scipy import stats
from psychopy import visual, core, event, data, gui, logging, monitors, sound

from exp import instruct

config = {"screen_hz": 60, "fullscreen": False, "monitor": 'testMonitor'}
exp_objects = {}

exp_objects['win'] = visual.Window(size=(1300, 1000), fullscr=config['fullscreen'], units='norm', monitor=config['monitor'], colorSpace='rgb', color=(-1, -1, -1)) # create window

exp_objects['mouse'] = event.Mouse(visible=False, win=exp_objects['win'])  # create mouse
exp_objects['mouse'].setVisible(0)  # make mouse invisible

instruct.exp_objects = exp_objects
instruct.show_instructions(["hey1", "hey2", "hey3"])

exp_objects['win'].close()
core.quit()