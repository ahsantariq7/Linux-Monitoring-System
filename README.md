Certainly! Here's the README.md file in code format:

```markdown
# Linux Monitoring System

## Introduction

This project is a Linux Monitoring System that captures an image when the laptop is powered on, sends an email with the laptop's status, and checks if the person using the laptop is authorized. It utilizes face recognition, system information retrieval, and email sending capabilities.

## Installation

1. Copy and paste the Python file into `/usr/local/bin/monitor.py`:

   ```bash
   sudo nano /usr/local/bin/monitor.py
   ```

   Paste the content of `monitor.py` into the file and save it.

2. Copy and paste the service file into `/etc/systemd/system/monitor.service`:

   ```bash
   sudo nano /etc/systemd/system/monitor.service
   ```

   Paste the content of `monitor.service` into the file and save it.

3. Enable the service:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable monitor.service
   sudo systemctl start monitor.service
   ```

## Functionality

- **Face Recognition:** The system uses face recognition to check if the person using the laptop is authorized.

- **System Status Email:** An email is sent with laptop status information, including IP address, OS, CPU usage, disk space, and battery status.

- **Capture and Save Photo:** The system captures a photo when the laptop is powered on and saves it in a specified folder.

- **Internet Connectivity Check:** The system checks for internet connectivity before sending emails.

## Usage

Once the system is set up, it will run in the background. The service is configured to start automatically when the system boots.

## Notes

- Make sure to adjust the camera index in the `capture_and_save_photo` function if needed.

- Customize the email configuration (sender and recipient email, password) in the `send_status_email` function.

- The known face for recognition is loaded from the file `ahsan.png`. Ensure that this file contains the authorized face.

- Adjust the tolerance level in the `recognize_faces` function for face recognition accuracy.

## Author

This monitoring system was developed by Engr. Ahsan Tariq.

Feel free to reach out for any questions or issues.
```

