# hidden-file-finder
## Overview
Hidden File Finder is a Python tool built on Kali Linux to detect hidden and suspicious files.  
It scans directories, logs suspicious files, visualizes results with bar charts, and provides real-time monitoring alerts.

## Features
- **Scan**: Detect hidden dotfiles and suspicious extensions (.exe, .bat, .js, .sh).  
- **Log**: Save suspicious file paths into `hidden_files_log.txt`.  
- **Visualize**: Generate a bar chart showing hidden vs normal files.  
- **Monitor**: Real-time alerts when new suspicious files are created.

## Setup Instructions
1. Install Python 3 and dependencies:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install watchdog matplotlib
2. Clone this repository:
   ```
   git clone https://github.com/Jainkhushi274/hidden-file-finder.git
   cd hidden-file-finder
3. Run the script:
   ```
   python3 hidden_finder.py
## Usage
- Enter the directory you want to scan.
- View suspicious files listed in the terminal.
- Check hidden_files_log.txt for saved results.
- See a bar chart visualization of hidden vs normal files.
- Enable real-time monitoring to get instant alerts when new suspicious files appear.

## Demo Screenshots
Terminal Alerts
<img width="1920" height="945" alt="alerts" src="https://github.com/user-attachments/assets/c684c75f-9dce-4693-8b07-1f3919a68fcf" />
Bar Chart Visualization
<img width="1920" height="945" alt="visual" src="https://github.com/user-attachments/assets/f5abf8f6-23b3-449c-8b70-f9568b578f12" />
Log File Contents
<img width="1920" height="945" alt="logfile" src="https://github.com/user-attachments/assets/5073fd64-4d69-45ec-95bf-76c81f2c66cb" />
## Future Improvements
- Add hash integrity checks for tampering detection.
- Implement whitelist/blacklist system.
- Send alerts via email or Slack.


