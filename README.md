KeyLogger
KeyLogger is a simple Python-based keylogging tool that records keystrokes and stores them in a log file. It is designed for educational and testing purposes, demonstrating how key event listeners work in Python.

Features
Captures and logs all keyboard inputs.
Ignores special keys like Shift, Ctrl, and Caps Lock.
Saves recorded keystrokes into a log file.
Project Structure
create_log.py – Ensures that log.txt exists before logging starts.
keylogger.py – Captures and records keystrokes.
Installation & Usage
Step 1: Clone the Repository
git clone https://github.com/ashleylina/KeyLogger.git
cd KeyLogger

Step 2: Install Required Dependencies
pip install pynput

Step 3: Run the Scripts
Create the Log File
python create_log.py

Start the Keylogger
python keylogger.py

Disclaimer
This project is for educational purposes only. Using keyloggers without permission is illegal and may result in legal consequences.
