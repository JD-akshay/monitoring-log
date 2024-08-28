import time
import os

# Path to the log file you want to monitor
log_file_path = '/var/log/syslog'  # Replace with your log file path

# Function to monitor the log file
def monitor_log_file(file_path):
    with open(file_path, 'r') as file:
        # Move the pointer to the end of the file
        file.seek(0, os.SEEK_END)

        while True:
            # Read the new line from the log file
            line = file.readline()

            if not line:
                # If no new line, wait for some time and retry
                time.sleep(0.1)
                continue

            # Check for specific keywords like 'ERROR'
            if 'ERROR' in line:
                print(f"Error Detected: {line.strip()}")

if __name__ == "__main__":
    monitor_log_file(log_file_path)
