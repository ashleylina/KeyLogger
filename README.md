#KeyLogger
KeyLogger is a simple Python-based keylogging tool that records keystrokes and stores them in a log file. It is designed for educational and testing purposes, demonstrating how key event listeners work in Python.

Features
Captures and logs all keyboard inputs.
Ignores special keys like Shift, Ctrl, and Caps Lock.
Saves recorded keystrokes into a log.txt file.
Includes a separate script to create the log file before logging begins.
Project Structure
This project contains the following files:

create_log.py – Ensures that log.txt exists before logging starts.
keylogger.py – Captures and records keystrokes.
log.txt – Stores recorded keystrokes.
key_descriptions.txt – A list of key descriptions and their functions.
README.md – Project documentation.
Installation & Usage
Step 1: Clone the Repository
To get started, clone the repository from GitHub:

sh
Copy
Edit
git clone https://github.com/ashleylina/KeyLogger.git
cd KeyLogger
Step 2: Install Required Dependencies
Ensure you have Python installed, then install the required package:

sh
Copy
Edit
pip install pynput
Step 3: Run the Scripts
1. Create the Log File
Run the create_log.py script to ensure log.txt is created:

sh
Copy
Edit
python create_log.py
2. Start the Keylogger
Now, start the keylogging process by running:

sh
Copy
Edit
python keylogger.py
This script will run in the background and log all keystrokes to log.txt.

How It Works
create_log.py

Checks if log.txt exists.
Creates log.txt if it does not exist.
keylogger.py

Listens for keyboard input.
Converts key presses into a readable format.
Stores them in log.txt.
Ignores unnecessary keys like Shift, Ctrl, and Caps Lock.
File Modes Explanation
When handling files in Python, different modes are used:

"w" – Write mode (creates a new file or clears existing content).
"r" – Read mode (opens a file for reading).
"a" – Append mode (adds new content without deleting previous data).
"x" – Exclusive creation mode (creates a new file but fails if it already exists).
Disclaimer
This project is intended for educational and ethical use only. Using keyloggers without permission is illegal and may result in legal consequences. Ensure you have explicit consent before deploying this tool.
