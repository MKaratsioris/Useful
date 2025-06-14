import logging
import time

logging.basicConfig()
#logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def expensive_func():
    time.sleep(2)
    return time.time()

if __name__ == "__main__":
    if log.isEnabledFor(logging.DEBUG):
        log.debug("The time is %d ns", expensive_func())