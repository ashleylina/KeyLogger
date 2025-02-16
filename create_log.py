# create_log.py - Ensures log.txt file exists before running keylogger.py

def create_log_file():
    try:
        with open("log.txt", "x") as f:  # Create log.txt if not exists
            pass  
    except FileExistsError:  # Ignore if file already exists
        pass  

if __name__ == "__main__":  
    create_log_file()  # Run function when script is executed
