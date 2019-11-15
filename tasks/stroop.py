from exp import instruct

def run_task(exp_objects):
    instructions = instruct.Instructions(exp_objects, ["This is a stroop task.", "Try me."])
    instructions.show_wait()