from datetime import datetime

log_file = "docs/log.txt"

def log_process(message):
    timestatmp_format = '%Y-%h-%D-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestatmp_format)
    with open(log_file, "a") as file:
        file.write(timestamp + ":" + message + "\n")
