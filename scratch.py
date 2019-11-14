from importlib import reload
import exp
from exp import instruct
from exp.instruct import *
reload(instruct)
from psychopy import visual, core, event, data, gui, logging, monitors, sound

fullscreen = False
win = visual.Window(size=(1300, 1000), fullscr=fullscreen, units='norm', colorSpace='rgb', color=(-1, -1, -1))
mouse = event.Mouse(visible=False, win=win)
show_instructions(['page 1', 'page2'])

# expobjs = {"mouse": mouse}

# instruct.xyz = 4
# instruct.sayhi = "hi"
# exp.instruct.hey2()
# exp.instruct.saysomething()

# xyz = 4
# hey()

d = {"win": "window1", "name": "Hause"}
instruct.expobj = d

instruct.expobj['win']
instruct.expobj['name']

# show_instructions(['page1', "page2"])