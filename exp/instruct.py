# from psychopy import event, visual
def hey2():
    print(xyz)

def saysomething():
    print(sayhi)

def show_instructions(text, timeBeforeAutomaticProceed=0, timeBeforeShowingSpace=0):
    '''Show instructions.
    text: Provide a list with instructions/text to present. One list item will be presented per page.
    timeBeforeAutomaticProceed: The time in seconds to wait before proceeding automatically.
    timeBeforeShowingSpace: The time in seconds to wait before showing 'Press space to continue' text.
    '''
    mouse.setVisible(0)
    event.clearEvents()
    # 'Press space to continue' text for each 'page'
    continueText = visual.TextStim(win=win, units='norm', colorSpace='rgb', color=[1, 1, 1], font='Verdana', text="Press space to continue", height=0.04, wrapWidth=1.4, pos=[0.0, 0.0])
    # instructions to be shown
    instructText = visual.TextStim(win=win, units='norm', colorSpace='rgb', color=[1, 1, 1], font='Verdana', text='DEFAULT', height=0.08, wrapWidth=1.4, pos=[0.0, 0.5])
    for i in range(len(text)): # for each item/page in the text list
        instructText.text = text[i] # set text for each page
        if timeBeforeAutomaticProceed == 0 and timeBeforeShowingSpace == 0:
            while not event.getKeys(keyList=['space']):
                continueText.draw(); instructText.draw();  win.flip()
                if event.getKeys(keyList=['backslash']):
                    win.close()
                    core.quit()
                elif event.getKeys(['bracketright']): #if press 7, skip to next block
                    return None
        elif timeBeforeAutomaticProceed != 0 and timeBeforeShowingSpace == 0:
            # clock to calculate how long to show instructions
            # if timeBeforeAutomaticProceed is not 0 (e.g., 3), then each page of text will be shown 3 seconds and will proceed AUTOMATICALLY to next page
            instructTimer = core.Clock()
            while instructTimer.getTime() < timeBeforeAutomaticProceed:
                if event.getKeys(keyList=['backslash']):
                    win.close()
                    core.quit()
                elif event.getKeys(['bracketright']):
                    return None
                instructText.draw(); win.flip()
        elif timeBeforeAutomaticProceed == 0 and timeBeforeShowingSpace != 0:
            instructTimer = core.Clock()
            while instructTimer.getTime() < timeBeforeShowingSpace:
                if event.getKeys(keyList=['backslash']):
                    win.close()
                    core.quit()
                elif event.getKeys(['bracketright']):
                    return None
                instructText.draw(); win.flip()
            win.flip(); event.clearEvents()
    instructText.setAutoDraw(False)
    continueText.setAutoDraw(False)
    for _ in range(30):
        win.flip() # wait at the end of the block