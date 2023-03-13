from task_worker import Task_Worker as tw
from ask_master import Ask_Master as am
from threading import Thread


def StartMaster():
    master = am()
    master.start()

def StartWorker():
    worker = tw()
    worker.start()

if __name__ == "__main__":
    pass
    