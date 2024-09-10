# keylogger
A python-based keylogger for windows.

the default directory of the logging file is C:\Users\user\Documents but it can be changed in keylogger.py (see the code for more info)


## Installation 

```
pip install pynput

python keylogger.py
```

---------------------------------------------------------------------------

in case you want to compile into a .exe file do the following steps:

Open cmd as admin

```
cd C:\Python312\Scripts
pip install pyinstaller

pyinstaller --onefile --noconsole your\file\path\here.py
```

.exe file will be placed under C:\Python312\Scripts\dist
