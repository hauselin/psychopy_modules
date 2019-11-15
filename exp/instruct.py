from psychopy import event, visual, core
from . import utils

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
        

## TODO: instruction class; add background image?
class Instructions(object):
    
    def __init__(self, exp_objects, text=["Welcome to our study!"], image=None):
        """[summary]
        
        Args:
            text (list, optional): [description]. Defaults to ["Welcome to our study!"].
        """
        self.text = text
        self.exp_objects = exp_objects
        self.image = None

    def set_text(self, text):
        """[summary]
        
        Args:
            text ([type]): [description]
        """
        self.text = text

    def _wait(self, secs=0.5):
        """[summary]
        
        Args:
            secs (float, optional): [description]. Defaults to 0.5.
        """
        for _ in range(int(secs * self.exp_objects["screen_hz"])):  # brief pause
            self.exp_objects['win'].flip()

    def show_wait(self, text=None):
        """[summary]
        
        Returns:
            [type]: [description]
        """

        if text is not None:
            self.set_text(text)
        self.exp_objects['mouse'].setVisible(0)
        event.clearEvents()
        for t in self.text:
            self.exp_objects["txt_instructions"].setText(t)
            while not event.getKeys(keyList=['space']):
                self.exp_objects["txt_space_continue"].draw()
                self.exp_objects["txt_instructions"].draw()
                self.exp_objects['win'].flip()
                if event.getKeys(self.exp_objects["skip_keys"]):
                    return None
                utils.check_quit(self.exp_objects['win'], self.exp_objects["quit_keys"], self.exp_objects["dataraw_dir"])
        self._wait()

    def show_automatic(self, secs_to_wait=1, text=None):
        """[summary]
        
        Args:
            secs_to_wait (int, optional): [description]. Defaults to 1.
            text ([type], optional): [description]. Defaults to None.
        
        Returns:
            [type]: [description]
        """
        if text is not None:
            self.set_text(text)
        self.exp_objects['mouse'].setVisible(0)
        event.clearEvents()
        for t in self.text:
            self.exp_objects["txt_instructions"].setText(t)
            instruct_timer = core.Clock()
            while instruct_timer.getTime() < secs_to_wait:
                self.exp_objects["txt_instructions"].draw()
                self.exp_objects['win'].flip()
                if event.getKeys(self.exp_objects["skip_keys"]):
                    return None
                utils.check_quit(self.exp_objects['win'], self.exp_objects["quit_keys"], self.exp_objects["dataraw_dir"])
        self._wait()

    def wait_show(self, secs_to_wait=1, text=None):
        """[summary]
        
        Args:
            secs_to_wait (int, optional): [description]. Defaults to 1.
            text ([type], optional): [description]. Defaults to None.
        """
        if text is not None:
            self.set_text(text)
        self._wait(secs_to_wait)
        self.show_wait()