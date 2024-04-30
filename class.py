import time

class Timer:

    product_id = 'asin' #amazon standard identification number

    #variable constructor
    def __init__(self, BOO, ZOO, UPC, EAN, ISBN): #European article number; international standard book number
        self.BOO = BOO
        self.ZOO = ZOO
        self.UPC = UPC
        self.EAN = EAN
        self.ISBN = ISBN

    
class timer:

    #attributes
    start_exec_time = time.time()
    end_exec_time = time.time()
    start_proc_time = time.process_time()
    end_proc_time = time.process_time()

    #methods
    def exec_time(self):
        exec_time = self.end_exec_time - self.start_exec_time
        return exec_time
    
    def proc_time(self):
        proc_time = self.end_proc_time - self.start_proc_time
        return proc_time
    
        #pass #avoid errors