'''
print("My name is Ahsan")
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define your Gmail account credentials
sender_email = "ahsantariq0724@gmail.com"
sender_password = "ifym fpod yonw mbki "  # Use an "App Password" if you have two-factor authentication enabled

# Define the recipient's email address
recipient_email = "ahsantariq0724@gmail.com"

# Create the email message
subject = "Are you Ahsan?"
message = "Yes, I am Ahsan."

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

msg.attach(MIMEText(message, "plain"))

# Connect to the SMTP server (Gmail in this case) and send the email
try:
    time.sleep(10)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Email sending fail {e}")
'''
'''
import requests
from geopy.geocoders import Nominatim
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to get your public IP address
def get_public_ip():
    response = requests.get("https://api64.ipify.org?format=json")
    data = response.json()
    return data['ip']

# Function to get your location based on your IP address
def get_location(ip_address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ip_address)
    return location

# Function to send an email
def send_email(subject, body):
    from_email = 'your_email@gmail.com'  # Replace with your email
    to_email = 'recipient_email@gmail.com'  # Replace with the recipient's email
    password = 'your_password'  # Replace with your email password

    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = message.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Get your public IP address
public_ip = get_public_ip()

# Get your location based on your IP address
location = get_location(public_ip)

if location:
    location_info = f"Your IP Address: {public_ip}\nYour Location: {location.address}"
else:
    location_info = "Unable to determine location."

# Send an email with IP address and location information
email_subject = "IP Address and Location"
email_body = location_info

send_email(email_subject, email_body)

print("Email sent with your IP address and location.")
'''
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import socket
from datetime import datetime
import platform
import psutil
import time
from PIL import ImageGrab 
import subprocess
import os

# Define your Gmail account credentials
sender_email = "ahsantariq0724@gmail.com"
sender_password = "ifym fpod yonw mbki "  # Use an "App Password" if you have two-factor authentication enabled

# Define the recipient's email address
recipient_email = "ahsantariq0724@gmail.com"

# Get your laptop's IP address
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

# Capture a screenshot
# Capture a screenshot
screenshot_filename = "screenshot.png"
screenshot = ImageGrab.grab()
screenshot.save(screenshot_filename)
# Log user activity
activity_log = subprocess.check_output("who", shell=True).decode("utf-8")

# Get additional laptop information
os_info = platform.platform()
processor = platform.processor()
architecture = platform.architecture()
memory_info = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Total RAM in GB

# Create the email message
subject = "Laptop Status Update"
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

message = f"Hello,\n\nI wanted to inform you that your laptop is currently powered on. Here are the details:\n\n"
message += f"- IP Address: {ip_address}\n"
message += f"- Current Time: {current_time}\n"
message += f"- Operating System: {os_info}\n"
message += f"- Processor: {processor}\n"
message += f"- Architecture: {architecture[0]} {architecture[1]}\n"
message += f"- Total RAM: {memory_info} GB\n\n"
message += "It appears that your laptop is actively in use. If you have any questions or need assistance, please don't hesitate to reach out. Enjoy your day!\n\n"
message += "Best regards,\nYour Laptop Monitoring System"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

msg.attach(MIMEText(message, "plain"))

# Attach the screenshot to the email
with open(screenshot_filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {screenshot_filename}")
    msg.attach(part)

# Attach the user activity log to the email
msg.attach(MIMEText(activity_log, "plain"))

# Connect to the SMTP server (Gmail in this case) and send the email
try:
    time.sleep(10)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Email sending failed: {str(e)}")

# Clean up the screenshot file
os.remove(screenshot_filename)
'''
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import socket
from datetime import datetime
import platform
import psutil
from PIL import Image
import subprocess
import os
from Xlib import display
import time
# Define your Gmail account credentials
# Define your Gmail account credentials
sender_email = "ahsantariq0724@gmail.com"
sender_password = "ifym fpod yonw mbki "  # Use an "App Password" if you have two-factor authentication enabled

  # Use an "App Password" if you have two-factor authentication enabled
# Define the recipient's email address
recipient_email = "ahsantariq0724@gmail.com"

# Get your laptop's IP address
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

# Capture a screenshot on Linux
screenshot_filename = "screenshot.png"

display_obj = display.Display()
root = display_obj.screen().root
raw = root.get_image(0, 0, root.get_width(), root.get_height(), Xlib.X.ZPixmap, 0xffffffff)
image = Image.frombytes("RGB", (root.get_width(), root.get_height()), raw.data, "raw", "BGRX")

# Save the screenshot
image.save(screenshot_filename)

# Log user activity
activity_log = subprocess.check_output("who", shell=True).decode("utf-8")

# Get additional laptop information
os_info = platform.platform()
processor = platform.processor()
architecture = platform.architecture()
memory_info = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Total RAM in GB

# Create the email message
subject = "Laptop Status Update"
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

message = f"Hello,\n\nI wanted to inform you that your laptop is currently powered on. Here are the details:\n\n"
message += f"- IP Address: {ip_address}\n"
message += f"- Current Time: {current_time}\n"
message += f"- Operating System: {os_info}\n"
message += f"- Processor: {processor}\n"
message += f"- Architecture: {architecture[0]} {architecture[1]}\n"
message += f"- Total RAM: {memory_info} GB\n\n"
message += "It appears that your laptop is actively in use. If you have any questions or need assistance, please don't hesitate to reach out. Enjoy your day!\n\n"
message += "Best regards,\nYour Laptop Monitoring System"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

msg.attach(MIMEText(message, "plain"))

# Attach the screenshot to the email
with open(screenshot_filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {screenshot_filename}")
    msg.attach(part)

# Attach the user activity log to the email
msg.attach(MIMEText(activity_log, "plain"))

# Connect to the SMTP server (Gmail in this case) and send the email
try:
    time.sleep(10)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Email sending failed: {str(e)}")

# Clean up the screenshot file
os.remove(screenshot_filename)

'''
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import socket
from datetime import datetime
import platform
import psutil
import subprocess
import time

# Define your Gmail account credentials
sender_email = "ahsantariq0724@gmail.com"
sender_password = "ifym fpod yonw mbki "  # Use an "App Password" if you have two-factor authentication enabled

# Define the recipient's email address
recipient_email = "ahsantariq0724@gmail.com"

# Get your laptop's IP address
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

# Log user activity
activity_log = subprocess.check_output("who", shell=True).decode("utf-8")

# Get additional laptop information
os_info = platform.platform()
processor = platform.processor()
architecture = platform.architecture()
memory_info = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Total RAM in GB

# Create the email message
subject = "Laptop Status Update"
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

message = f"Hello,\n\nI wanted to inform you that your laptop is currently powered on. Here are the details:\n\n"
message += f"- IP Address: {ip_address}\n"
message += f"- Current Time: {current_time}\n"
message += f"- Operating System: {os_info}\n"
message += f"- Processor: {processor}\n"
message += f"- Architecture: {architecture[0]} {architecture[1]}\n"
message += f"- Total RAM: {memory_info} GB\n\n"
message += "It appears that your laptop is actively in use. If you have any questions or need assistance, please don't hesitate to reach out. Enjoy your day!\n\n"
message += "Best regards,\nYour Laptop Monitoring System"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

msg.attach(MIMEText(message, "plain"))

# Attach the user activity log to the email
msg.attach(MIMEText(activity_log, "plain"))

# Connect to the SMTP server (Gmail in this case) and send the email
try:
    time.sleep(10)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Email sending failed: {str(e)}")

'''
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import socket
from datetime import datetime
import platform
import psutil
import subprocess
import time

# Define your Gmail account credentials
sender_email = "ahsantariq0724@gmail.com"
sender_password = "ifym fpod yonw mbki "  # Use an "App Password" if you have two-factor authentication enabled

# Define the recipient's email address
recipient_email = "ahsantariq0724@gmail.com"

# Get your laptop's IP address
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

# Get system information
os_info = platform.platform()
processor = platform.processor()

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)  # Calculate CPU usage over 1 second

# Get disk usage
disk_usage = psutil.disk_usage("/")
total_disk_space = disk_usage.total / (1024 ** 3)  # Total disk space in GB
used_disk_space = disk_usage.used / (1024 ** 3)  # Used disk space in GB

# Get battery status (if available)
battery_info = "Battery status: Not available"
battery = psutil.sensors_battery()
if battery:
    percent = battery.percent
    power_plugged = "Plugged in" if battery.power_plugged else "Unplugged"
    battery_info = f"Battery status: {percent}% ({power_plugged})"

# Create the email message
subject = "Laptop Status Update Code By Engr.Ahsan Tariq"
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

message = f"Hello,\n\nI wanted to inform you that your laptop is currently powered on. Here are the details:\n\n"
message += f"- IP Address: {ip_address}\n"
message += f"- Current Time: {current_time}\n"
message += f"- Operating System: {os_info}\n"
message += f"- Processor: {processor}\n"
message += f"- CPU Usage: {cpu_usage}%\n"
message += f"- Disk Space: Total {total_disk_space:.2f} GB, Used {used_disk_space:.2f} GB\n"
message += f"- {battery_info}\n\n"
message += "It appears that your laptop is actively in use. If you have any questions or need assistance, please don't hesitate to reach out. Enjoy your day!\n\n"
message += "Best regards,\nYour Laptop Monitoring System\nEngr.Ahsan Tariq"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

msg.attach(MIMEText(message, "plain"))

# Connect to the SMTP server (Gmail in this case) and send the email
try:
    time.sleep(10)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Email sending failed: {str(e)}")

'''
'''
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import socket
from datetime import datetime
import platform
import psutil
import subprocess
import time

# Define your Gmail account credentials
sender_email = "ahsantariq0724@gmail.com"
sender_password = "ifym fpod yonw mbki "  # Use an "App Password" if you have two-factor authentication enabled

# Define the recipient's email address
recipient_email = "ahsantariq0724@gmail.com"

# Get your laptop's IP address
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

# Get system information
os_info = platform.platform()
processor = platform.processor()

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)  # Calculate CPU usage over 1 second

# Get disk usage
disk_usage = psutil.disk_usage("/")
total_disk_space = disk_usage.total / (1024 ** 3)  # Total disk space in GB
used_disk_space = disk_usage.used / (1024 ** 3)  # Used disk space in GB

# Get battery status (if available)
battery_info = "Battery status: Not available"
battery = psutil.sensors_battery()
if battery:
    percent = battery.percent
    power_plugged = "Plugged in" if battery.power_plugged else "Unplugged"
    battery_info = f"Battery status: {percent}% ({power_plugged})"

# Create the email message
subject = "Laptop Status Update"
current_time = datetime.now().strftime("%Y-%m-d %H:%M:%S")

message = f"Hello,\n\nI wanted to inform you that your laptop is currently powered on. Here are the details:\n\n"
message += f"- IP Address: {ip_address}\n"
message += f"- Current Time: {current_time}\n"
message += f"- Operating System: {os_info}\n"
message += f"- Processor: {processor}\n"
message += f"- CPU Usage: {cpu_usage}%\n"
message += f"- Disk Space: Total {total_disk_space:.2f} GB, Used {used_disk_space:.2f} GB\n"
message += f"- {battery_info}\n\n"
message += "It appears that your laptop is actively in use. If you have any questions or need assistance, please don't hesitate to reach out.\n\n"

# Prompt the user for input
user_input = input("Enter a number: ")

# Check if the user's input matches a specific number
if user_input == "12345":
    message += "Congratulations, your input matched the secret number. Special message for you!"
else:
    message += "Sorry, your input did not match the secret number. Logging out..."

    # Trigger a logout request (Linux-specific, may vary based on the desktop environment)
    os.system("gnome-session-quit --force")

message += "\nBest regards,\nYour Laptop Monitoring System"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

msg.attach(MIMEText(message, "plain"))

# Connect to the SMTP server (Gmail in this case) and send the email
try:
    time.sleep(10)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Email sending failed: {str(e)}")

'''
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
from datetime import datetime
import platform
import psutil
import cv2
import os
import time

# Function to send an email with laptop status
def send_status_email():
    # Your email configuration
    sender_email = "ahsantariq0724@gmail.com"
    sender_password = "ifym fpod yonw mbki "
    recipient_email = "ahsantariq0724@gmail.com"

    # Get laptop status information
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    os_info = platform.platform()
    processor = platform.processor()
    cpu_usage = psutil.cpu_percent(interval=1)
    disk_usage = psutil.disk_usage("/")
    total_disk_space = disk_usage.total / (1024 ** 3)
    used_disk_space = disk_usage.used / (1024 ** 3)
    battery_info = "Battery status: Not available"
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        power_plugged = "Plugged in" if battery.power_plugged else "Unplugged"
        battery_info = f"Battery status: {percent}% ({power_plugged})"
    
    # Create the email message
    subject = "Laptop Status Update Code By Engr.Ahsan Tariq"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"Hello,\n\nI wanted to inform you that your laptop is currently powered on. Here are the details:\n\n"
    message += f"- IP Address: {ip_address}\n"
    message += f"- Current Time: {current_time}\n"
    message += f"- Operating System: {os_info}\n"
    message += f"- Processor: {processor}\n"
    message += f"- CPU Usage: {cpu_usage}%\n"
    message += f"- Disk Space: Total {total_disk_space:.2f} GB, Used {used_disk_space:.2f} GB\n"
    message += f"- {battery_info}\n\n"
    message += "It appears that your laptop is actively in use. If you have any questions or need assistance, please don't hesitate to reach out. Enjoy your day!\n\n"
    message += "Best regards,\nYour Laptop Monitoring System\nEngr.Ahsan Tariq"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Connect to the SMTP server (Gmail) and send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Email sending failed: {str(e)}")

# Function to capture and save a photo using the laptop's camera
def capture_and_save_photo():
    # Open the camera (you may need to adjust the camera index)
    cap = cv2.VideoCapture(0)

    # Capture a photo
    ret, frame = cap.read()

    # Save the photo with date and time
    if ret:
        current_time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        photo_filename = f"person_photo_{current_time_str}.jpg"
        cv2.imwrite(photo_filename, frame)
        print(f"Photo captured and saved: {photo_filename}")

    # Release the camera
    cap.release()

if __name__ == "__main__":
    # Send laptop status email
    send_status_email()

    # Capture and save a photo
    capture_and_save_photo()
'''
'''
import face_recognition
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
from datetime import datetime
import platform
import psutil
import cv2
import os
from pathlib import Path
import time
import requests
# Function to check internet connectivity using requests library
def is_internet_connected():
    try:
        # Attempt to make a simple HTTP request to a known server (Google's public DNS)
        response = requests.get("http://www.google.com", timeout=5)
        response.raise_for_status()
        return True
    except requests.RequestException:
        return False

# Function to send an email with laptop status
def send_status_email():
    # Your email configuration
    sender_email = "ahsantariq0724@gmail.com"
    sender_password = "ifym fpod yonw mbki "  # Use an "App Password" if you have two-factor authentication enabled
    recipient_email = "ahsantariq0724@gmail.com"

    # Get laptop status information
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    os_info = platform.platform()
    processor = platform.processor()
    cpu_usage = psutil.cpu_percent(interval=1)
    disk_usage = psutil.disk_usage("/")
    total_disk_space = disk_usage.total / (1024 ** 3)
    used_disk_space = disk_usage.used / (1024 ** 3)
    battery_info = "Battery status: Not available"
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        power_plugged = "Plugged in" if battery.power_plugged else "Unplugged"
        battery_info = f"Battery status: {percent}% ({power_plugged})"

    # Create the email message
    subject = "Laptop Status Update Code By Engr.Ahsan Tariq"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"Hello,\n\nI wanted to inform you that your laptop is currently powered on. Here are the details:\n\n"
    message += f"- IP Address: {ip_address}\n"
    message += f"- Current Time: {current_time}\n"
    message += f"- Operating System: {os_info}\n"
    message += f"- Processor: {processor}\n"
    message += f"- CPU Usage: {cpu_usage}%\n"
    message += f"- Disk Space: Total {total_disk_space:.2f} GB, Used {used_disk_space:.2f} GB\n"
    message += f"- {battery_info}\n\n"
    message += "It appears that your laptop is actively in use. If you have any questions or need assistance, please don't hesitate to reach out. Enjoy your day!\n\n"
    message += "Best regards,\nYour Laptop Monitoring System\nEngr.Ahsan Tariq"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Connect to the SMTP server (Gmail) and send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Email sending failed: {str(e)}")


def capture_image():
    # Use a webcam or other methods to capture an image
    # Example:
    video_capture = cv2.VideoCapture(0)
    _, image = video_capture.read()
    video_capture.release()
    return image


def unlock_pc(matched_face):
    # Display the matched face on the laptop screen
    cv2.imshow("Matched Face", cv2.cvtColor(matched_face, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("PC unlocked.")

def load_known_faces():
    # Load known faces and their encodings
    known_face_image = face_recognition.load_image_file("ahsan.png")
    known_face_encoding = face_recognition.face_encodings(known_face_image)[0]
    return [known_face_encoding]


def recognize_faces(known_faces, unknown_face):
    # Find face locations and encodings in the unknown image
    face_locations = face_recognition.face_locations(unknown_face)
    face_encodings = face_recognition.face_encodings(unknown_face, face_locations)

    for unknown_encoding in face_encodings:
        # Compare the face encodings
        results = face_recognition.compare_faces(known_faces, unknown_encoding, tolerance=0.6)
        
        # Use the face distance for a more nuanced decision
        face_distances = face_recognition.face_distance(known_faces, unknown_encoding)
        best_match_index = int(np.argmin(face_distances))

        if results[best_match_index]:
            return True  # Match found
    return False  # No match found
# Function to capture and save a photo using the laptop's camera
def capture_and_save_photo():
    # Open the camera (you may need to adjust the camera index)
    cap = cv2.VideoCapture(0)

    # Capture a photo
    ret, frame = cap.read()

    # Get the user's desktop folder
    desktop_folder = "/home/ahsan/Desktop"

    # Create a subfolder named "LaptopMonitoringPhotos" if it doesn't exist
    subfolder_name = "L
'''
'''
import face_recognition
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
from datetime import datetime
import platform
import psutil
import cv2
import os
import time
import requests

# Function to check internet connectivity using requests library
def is_internet_connected():
    try:
        # Attempt to make a simple HTTP request to a known server (Google's public DNS)
        response = requests.get("http://www.google.com", timeout=5)
        response.raise_for_status()
        return True
    except requests.RequestException:
        return False

# Function to send an email with laptop status
def send_status_email():
    # Your email configuration
    sender_email = "ahsantariq0724@gmail.com"
    sender_password = "ifym fpod yonw mbki "  # Use an "App Password" if you have two-factor authentication enabled
    recipient_email = "ahsantariq0724@gmail.com"

    # Get laptop status information
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    os_info = platform.platform()
    processor = platform.processor()
    cpu_usage = psutil.cpu_percent(interval=1)
    disk_usage = psutil.disk_usage("/")
    total_disk_space = disk_usage.total / (1024 ** 3)
    used_disk_space = disk_usage.used / (1024 ** 3)
    battery_info = "Battery status: Not available"
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        power_plugged = "Plugged in" if battery.power_plugged else "Unplugged"
        battery_info = f"Battery status: {percent}% ({power_plugged})"

    # Create the email message
    subject = "Laptop Status Update Code By Engr.Ahsan Tariq"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"Hello,\n\nI wanted to inform you that your laptop is currently powered on. Here are the details:\n\n"
    message += f"- IP Address: {ip_address}\n"
    message += f"- Current Time: {current_time}\n"
    message += f"- Operating System: {os_info}\n"
    message += f"- Processor: {processor}\n"
    message += f"- CPU Usage: {cpu_usage}%\n"
    message += f"- Disk Space: Total {total_disk_space:.2f} GB, Used {used_disk_space:.2f} GB\n"
    message += f"- {battery_info}\n\n"
    message += "It appears that your laptop is actively in use. If you have any questions or need assistance, please don't hesitate to reach out. Enjoy your day!\n\n"
    message += "Best regards,\nYour Laptop Monitoring System\nEngr.Ahsan Tariq"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Connect to the SMTP server (Gmail) and send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Email sending failed: {str(e)}")

# Function to capture image and save photo
def capture_and_save_photo():
    # Open the camera (you may need to adjust the camera index)
    cap = cv2.VideoCapture(0)

    # Capture a photo
    ret, frame = cap.read()

    # Get the user's desktop folder
    desktop_folder = "/home/ahsan/Desktop"

    # Create a subfolder named "LaptopMonitoringPhotos" if it doesn't exist
    subfolder_name = "LaptopMonitoringPhotos"
    subfolder_path = os.path.join(desktop_folder, subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)

    # Save the photo in the subfolder with date and time
    if ret:
        current_time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        photo_filename = f"person_photo_{current_time_str}.jpg"
        photo_path = os.path.join(subfolder_path, photo_filename)
        cv2.imwrite(photo_path, frame)
        print(f"Photo captured and saved: {photo_path}")

    # Release the camera
    cap.release()

    return frame  # Return the captured frame (image)

def unlock_pc(matched_face):
    # Display the matched face on the laptop screen
    cv2.imshow("Matched Face", cv2.cvtColor(matched_face, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("PC unlocked.")

def show_warning_message():
    # Display a warning message on the laptop screen for non-matching faces
    warning_message = "You are not Ahsan. Your actions are being monitored."
    cv2.imshow("Warning", np.ones((100, 500, 3), dtype=np.uint8) * 255)  # White background
    cv2.putText(cv2.waitKey(0), warning_message, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Capture and save photo
    captured_image = capture_and_save_photo()

    # Check if an internet connection is available
    while not is_internet_connected():
        print("Waiting for internet connection...")
        time.sleep(5)  # Wait for 5 seconds before checking again

    print("Internet connection established. Capturing photo and sending email...")

    # Send laptop status email
    send_status_email()

    # Load known faces
    known_faces = load_known_faces()

    # Check for a match
    match_found, matched_face = recognize_faces(known_faces, captured_image)

    if match_found:
        print("Match found!")
        unlock_pc(matched_face)  # Call the function to unlock the PC
    else:
        print("No match found.")
        show_warning_message()  # Display a warning message for non-matching faces
'''
import face_recognition
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
from datetime import datetime
import platform
import psutil
import cv2
import os
import time
import requests

# Function to check internet connectivity using requests library
def is_internet_connected():
    try:
        # Attempt to make a simple HTTP request to a known server (Google's public DNS)
        response = requests.get("http://www.google.com", timeout=5)
        response.raise_for_status()
        return True
    except requests.RequestException:
        return False


def recognize_faces(known_faces, unknown_face):
    # Find face locations and encodings in the unknown image
    face_locations = face_recognition.face_locations(unknown_face)
    face_encodings = face_recognition.face_encodings(unknown_face, face_locations)

    for unknown_encoding in face_encodings:
        # Compare the face encodings
        results = face_recognition.compare_faces(known_faces, unknown_encoding, tolerance=0.6)
        
        # Use the face distance for a more nuanced decision
        face_distances = face_recognition.face_distance(known_faces, unknown_encoding)
        best_match_index = int(np.argmin(face_distances))

        if results[best_match_index]:
            return True, unknown_face  # Match found, return the matched face
    return False, None  # No match found
# Function to send an email with laptop status
def send_status_email():
    # Your email configuration
    sender_email = "ahsantariq0724@gmail.com"
    sender_password = "ifym fpod yonw mbki "  # Use an "App Password" if you have two-factor authentication enabled
    recipient_email = "ahsantariq0724@gmail.com"

    # Get laptop status information
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    os_info = platform.platform()
    processor = platform.processor()
    cpu_usage = psutil.cpu_percent(interval=1)
    disk_usage = psutil.disk_usage("/")
    total_disk_space = disk_usage.total / (1024 ** 3)
    used_disk_space = disk_usage.used / (1024 ** 3)
    battery_info = "Battery status: Not available"
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        power_plugged = "Plugged in" if battery.power_plugged else "Unplugged"
        battery_info = f"Battery status: {percent}% ({power_plugged})"

    # Create the email message
    subject = "Laptop Status Update Code By Engr.Ahsan Tariq"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"Hello,\n\nI wanted to inform you that your laptop is currently powered on. Here are the details:\n\n"
    message += f"- IP Address: {ip_address}\n"
    message += f"- Current Time: {current_time}\n"
    message += f"- Operating System: {os_info}\n"
    message += f"- Processor: {processor}\n"
    message += f"- CPU Usage: {cpu_usage}%\n"
    message += f"- Disk Space: Total {total_disk_space:.2f} GB, Used {used_disk_space:.2f} GB\n"
    message += f"- {battery_info}\n\n"
    message += "It appears that your laptop is actively in use. If you have any questions or need assistance, please don't hesitate to reach out. Enjoy your day!\n\n"
    message += "Best regards,\nYour Laptop Monitoring System\nEngr.Ahsan Tariq"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Connect to the SMTP server (Gmail) and send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Email sending failed: {str(e)}")

# Function to load known faces
def load_known_faces():
    known_face_image = face_recognition.load_image_file("ahsan.png")
    known_face_encoding = face_recognition.face_encodings(known_face_image)[0]
    return [known_face_encoding]

# Function to capture image and save photo
def capture_and_save_photo():
    # Open the camera (you may need to adjust the camera index)
    cap = cv2.VideoCapture(0)

    # Capture a photo
    ret, frame = cap.read()

    # Get the user's desktop folder
    desktop_folder = "/home/ahsan/Desktop"

    # Create a subfolder named "LaptopMonitoringPhotos" if it doesn't exist
    subfolder_name = "LaptopMonitoringPhotos"
    subfolder_path = os.path.join(desktop_folder, subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)

    # Save the photo in the subfolder with date and time
    if ret:
        current_time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        photo_filename = f"person_photo_{current_time_str}.jpg"
        photo_path = os.path.join(subfolder_path, photo_filename)
        cv2.imwrite(photo_path, frame)
        print(f"Photo captured and saved: {photo_path}")

    # Release the camera
    cap.release()

    return frame  # Return the captured frame (image)

# Function to unlock PC
def unlock_pc(matched_face):
    # Display the matched face on the laptop screen
    cv2.imshow("Matched Face", matched_face)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("PC unlocked.")

# Function to show warning message for non-matching faces
def show_warning_message():
    # Display a warning message on the laptop screen for non-matching faces
    warning_message = "You are not Ahsan. Your actions are being monitored."
    cv2.imshow("Warning", np.ones((100, 500, 3), dtype=np.uint8) * 255)  # White background
    cv2.putText(cv2.waitKey(0), warning_message, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Capture and save photo
    captured_image = capture_and_save_photo()

    # Check if an internet connection is available
    while not is_internet_connected():
        print("Waiting for internet connection...")
        time.sleep(5)  # Wait for 5 seconds before checking again

    print("Internet connection established. Capturing photo and sending email...")

    # Send laptop status email
    send_status_email()

    # Load known faces
    known_faces = load_known_faces()

    # Check for a match
    match_found, matched_face = recognize_faces(known_faces, captured_image)

    if match_found:
        print("Match found!")
        unlock_pc(matched_face)  # Call the function to unlock the PC
    else:
        print("No match found.")
        show_warning_message()  # Display a warning message for non-matching faces
