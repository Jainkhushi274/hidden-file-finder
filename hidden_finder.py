import os
import matplotlib.pyplot as plt
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- Scanner ---
def scan_hidden_files(directory):
    suspicious = []
    normal = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            if file.startswith('.') or file.endswith(('.exe', '.bat', '.js', '.sh')):
                suspicious.append(filepath)
            else:
                normal.append(filepath)
    return suspicious, normal

# --- Logger ---
def log_results(suspicious):
    with open("hidden_files_log.txt", "w") as log:
        for f in suspicious:
            log.write(f + "\n")

# --- Visualization ---
def visualize_results(suspicious, normal):
    labels = ['Suspicious/Hidden', 'Normal']
    counts = [len(suspicious), len(normal)]
    plt.bar(labels, counts, color=['red','green'])
    plt.title("File Scan Results")
    plt.show()

# --- Real-time Monitor ---
class HiddenFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            if filename.startswith('.') or filename.endswith(('.exe','.bat','.js','.sh')):
                print(f"ALERT: Suspicious file created → {event.src_path}")

if __name__ == "__main__":
    directory = input("Enter directory to scan: ").strip()

    # Safety check: create directory if missing
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist. Creating it...")
        os.makedirs(directory)

    suspicious, normal = scan_hidden_files(directory)
    print("\nSuspicious Hidden Files Found:")
    for f in suspicious:
        print(f)

    log_results(suspicious)
    visualize_results(suspicious, normal)

    choice = input("\nEnable real-time monitoring? (y/n): ")
    if choice.lower() == 'y':
        event_handler = HiddenFileHandler()
        observer = Observer()
        observer.schedule(event_handler, directory, recursive=True)
        observer.start()
        print(f"Monitoring {directory} for suspicious files... Press Ctrl+C to stop.")
        try:
            while True:
                pass
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
