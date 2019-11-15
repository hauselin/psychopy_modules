from psychopy import event, visual, core

## TODO: change to a class rather than function?
def show_instructions(text, timeBeforeAutomaticProceed=0, timeBeforeShowingSpace=0):
    '''Show instructions.
    text: Provide a list with instructions/text to present. One list item will be presented per page.
    timeBeforeAutomaticProceed: The time in seconds to wait before proceeding automatically.
    timeBeforeShowingSpace: The time in seconds to wait before showing 'Press space to continue' text.
    '''
    exp_objects['mouse'].setVisible(0)
    event.clearEvents()
    # 'Press space to continue' text for each 'page'
    continueText = visual.TextStim(win=exp_objects['win'], units='norm', colorSpace='rgb', color=[1, 1, 1], font='Verdana', text="Press space to continue", height=0.04, wrapWidth=1.4, pos=[0.0, 0.0])
    # instructions to be shown
    instructText = visual.TextStim(win=exp_objects['win'], units='norm', colorSpace='rgb', color=[1, 1, 1], font='Verdana', text='DEFAULT', height=0.08, wrapWidth=1.4, pos=[0.0, 0.5])
    
    for i in range(len(text)): # for each item/page in the text list
        instructText.text = text[i] # set text for each page
        if timeBeforeAutomaticProceed == 0 and timeBeforeShowingSpace == 0:
            while not event.getKeys(keyList=['space']):
                continueText.draw()
                instructText.draw()
                exp_objects['win'].flip()
                if event.getKeys(keyList=['backslash']):
                    exp_objects['win'].close()
                    core.quit()
                elif event.getKeys(['bracketright']): #if press 7, skip to next block
                    return None
        elif timeBeforeAutomaticProceed != 0 and timeBeforeShowingSpace == 0:
            # clock to calculate how long to show instructions
            # if timeBeforeAutomaticProceed is not 0 (e.g., 3), then each page of text will be shown 3 seconds and will proceed AUTOMATICALLY to next page
            instructTimer = core.Clock()
            while instructTimer.getTime() < timeBeforeAutomaticProceed:
                if event.getKeys(keyList=['backslash']):
                    exp_objects['win'].close()
                    core.quit()
                elif event.getKeys(['bracketright']):
                    return None
                instructText.draw()
                exp_objects['win'].flip()
        elif timeBeforeAutomaticProceed == 0 and timeBeforeShowingSpace != 0:
            instructTimer = core.Clock()
            while instructTimer.getTime() < timeBeforeShowingSpace:
                if event.getKeys(keyList=['backslash']):
                    exp_objects['win'].close()
                    core.quit()
                elif event.getKeys(['bracketright']):
                    return None
                instructText.draw()
                exp_objects['win'].flip()
            exp_objects['win'].flip()
            event.clearEvents()
    instructText.setAutoDraw(False)
    continueText.setAutoDraw(False)
    for _ in range(30):
        exp_objects['win'].flip()  # wait at the end of the block
        

## TODO: intruction class
class Instructions(object):
    
    def __init__(self, text=["Welcome to our study!"]):
        """[summary]
        
        Args:
            text (list, optional): [description]. Defaults to ["Welcome to our study!"].
        """
        self.text = text

    ## TODO: maybe switch to use generator rather than loop?
    def _show(self):
        """[summary]
        
        Returns:
            [type]: [description]
        """
        for t in self.text:
            exp_objects["txt_instructions"].text = t
            while not event.getKeys(keyList=['space']):
                exp_objects["txt_space_continue"].draw()
                exp_objects["txt_instructions"].draw()
                exp_objects['win'].flip()
                if event.getKeys(keyList=['backslash']):
                    exp_objects['win'].close()
                    core.quit()
                elif event.getKeys(['bracketright']): #if press 7, skip to next block
                    return None

    def _wait(secs=0.5):
        for _ in range(int(0.5 * exp_objects["screen_hz"])):  # brief pause
            exp_objects['win'].flip()

    def show_wait(self):
        """[summary]
        
        Returns:
            [type]: [description]
        """
        exp_objects['mouse'].setVisible(0)
        event.clearEvents()
        for t in self.text:
            exp_objects["txt_instructions"].setText(t)
            while not event.getKeys(keyList=['space']):
                exp_objects["txt_space_continue"].draw()
                exp_objects["txt_instructions"].draw()
                exp_objects['win'].flip()
                if event.getKeys(keyList=['backslash']):
                    exp_objects['win'].close()
                    core.quit()
                elif event.getKeys(['bracketright']): 
                    return None
        self._wait()

    def show_automatic(self, secs_to_wait=1):
        exp_objects['mouse'].setVisible(0)
        event.clearEvents()
        for t in self.text:
            exp_objects["txt_instructions"].setText(t)
            exp_objects["txt_instructions"].setAutoDraw(True)
            instruct_timer = core.Clock()
            while instruct_timer.getTime() < secs_to_wait:
                exp_objects['win'].flip()
                if event.getKeys(keyList=['backslash']):
                    exp_objects['win'].close()
                    core.quit()
                elif event.getKeys(['bracketright']): 
                    return None
            exp_objects["txt_instructions"].setAutoDraw(False)
        self._wait()

    def wait_show(self, secs_to_wait=1):
        exp_objects['mouse'].setVisible(0)
        event.clearEvents()