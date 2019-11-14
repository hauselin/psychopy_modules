#!/usr/bin/env python
# -*- coding: utf-8 -*-

#"""
#Demo: show a very basic program: hello world
#"""

#from __future__ import absolute_import, division, print_function

# Import key parts of the PsychoPy library:
from psychopy import visual, core

# Create a visual window:
win = visual.Window(size=(900,900), color='black')

# Variable assigment:
iString = "Testing"
iInt = 5

# Create (but not yet display) some text:
msg1 = visual.TextStim(win, text= iString, pos=(1, -0))  # default position = centered
msg2 = visual.TextStim(win, text=iString, pos=(1, -0.3))

# Draw the text to the hidden visual buffer:
msg1.draw()
msg2.draw()

# Show the hidden buffer--everything that has been drawn since the last win.flip():
win.flip()

# Loops an integer print
for iInt in range(20-iInt):
    msg1 = visual.TextStim(win, text= iInt, color='red', pos=(1, -0.3))
    msg1.draw()
    win.flip()

# Reuses the variable to display the text:
msg1 = visual.TextStim(win, text= "This document is for testing")

# Draw the text to the hidden visual buffer:
msg1.draw()

# Hidden Buffer
win.flip()

# Wait 3 seconds so people can see the message, then exit gracefully:
core.wait(1)

win.close()
core.quit()

# The contents of this file are in the public domain.
