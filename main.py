import threading
import logging
import time
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
global is_processing_worker2
global is_processing_worker3
global pause_process_worker1
pause_process_worker1 = False
is_processing_worker2 = True
is_processing_worker3 = True


def worker3():
    global is_processing_worker3
    logging.debug("Worker 3 started")
    for i in range(15, 0, -1):
        is_processing_worker3 = True
        logging.debug(f"Worker 3 counting: {i}")
    logging.debug("Worker 3 finished")
    is_processing_worker3 = False


def worker2():
    global pause_process_worker1
    global is_processing_worker2
    logging.debug("Worker 2 started")
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        is_processing_worker2 = True
        logging.debug(f"Worker 2 printing: {letter}")
        if letter == "J":
            pause_process_worker1 = True
        if letter == "L":
            worker3_thread = threading.Thread(target=worker3)
            worker3_thread.start()
            time.sleep(.05)
    logging.debug("Worker 2 finished")
    is_processing_worker2 = False


def worker1():
    global pause_process_worker1
    logging.debug("Worker 1 started")
    count = 0
    while True:
        count += 1
        logging.debug(f"Worker 1 counting: {count}")
        if pause_process_worker1:
            time.sleep(.005)
            pause_process_worker1 = False
        if count == 5:
            worker2_thread = threading.Thread(target=worker2)
            worker2_thread.start()
            time.sleep(0.005)
        if not (is_processing_worker2 and is_processing_worker3):
            time.sleep(0.5)
            break
    logging.debug("Worker 1 finished")


if __name__ == "__main__":
    worker1_thread = threading.Thread(target=worker1)
    worker1_thread.start()
