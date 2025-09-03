# What is it?
Simple python application that overrides the FOV value of the game during run time, just open the game and them the application (For now only works on the steam version)

# How was it done?
The part that write to the RAM was made based on the code available in the repository below, I just made some small modifications to interpret the values as different types:
https://github.com/vsantiago113/ReadWriteMemory

For the UI the TK lib was used:
https://docs.python.org/pt-br/3/library/tk.html

# How to use
To use it just run the game and then the FOV Changer, you should see a small window with the FOV slider:

![alt text](https://github.com/rod-amorim/Penumbra-overtureFovChanger/blob/main/Main_screen.PNG)

If the game is not running an error will be displayed:

![alt text](https://github.com/rod-amorim/Penumbra-overtureFovChanger/blob/main/Main_screen_error.PNG)

Clicking OK will terminate the app

# Download

The download of the .exe is available in the releases section of this page

# Build your own EXE (only if you choose to clone the repository)
```
python -m PyInstaller --onefile -w -F --add-binary "icon.ico;." --noconsole --icon=icon.ico Penumbra-overtureFovChanger.py
```
