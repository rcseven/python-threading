import threading
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
global is_processing
is_processing = True


def worker3():
    global is_processing
    logging.debug("Worker 3 started")
    for i in range(15, 0, -1):
        is_processing = True
        logging.debug(f"Worker 3 counting: {i}")
    logging.debug("Worker 3 finished")
    is_processing = False


def worker2():
    global is_processing
    logging.debug("Worker 2 started")
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        is_processing = True
        logging.debug(f"Worker 2 printing: {letter}")
        if letter == "L":
            worker3_thread = threading.Thread(target=worker3)
            worker3_thread.start()
    logging.debug("Worker 2 finished")
    is_processing = False


def worker1():
    logging.debug("Worker 1 started")
    count = 0
    while is_processing:
        count += 1
        logging.debug(f"Worker 1 counting: {count}")
        if count == 5:
            worker2_thread = threading.Thread(target=worker2)
            worker2_thread.start()
    logging.debug("Worker 1 finished")


if __name__ == "__main__":
    worker1_thread = threading.Thread(target=worker1)
    worker1_thread.start()
    logging.debug("Main thread finished")
