# IP Flex Cam Configuration Tool

## Overview

This Python script configures the date, time, and timezone settings for an IP Flex Cam camera using HTTP requests. It can also open the camera web interface in your default browser.

The script:

* Connects to the IP camera using HTTP Basic Authentication
* Configures timezone and daylight savings settings
* Synchronizes the camera clock with your computer's current date/time
* Opens the camera webpage for verification

---

# Requirements

* Python 3.10 or newer
* Network access to the IP Flex Cam
* Valid camera username/password

---

# Install Python

Download Python from:

[Python Official Website](https://www.python.org/downloads/?utm_source=chatgpt.com)

During installation on Windows:

* Check **"Add Python to PATH"**
* Complete the installation

Verify installation:

```bash
python --version
```

or

```bash
py --version
```

---

# Download Dependencies

This project requires the `requests` library.

Install it using pip:

```bash
pip install requests
```

If pip is unavailable:

```bash
python -m pip install requests
```

---

# Save the Script

Save the script as:

```text
ip_flex_cam_config.py
```

---

# How to Run

Open a terminal or command prompt in the folder containing the script.

Run the script using:

```bash
python ip_flex_cam_config.py -u USERNAME -p PASSWORD -i CAMERA_IP
```

Example:

```bash
python ip_flex_cam_config.py -u admin -p password123 -i 192.168.1.100
```

---

# Program Commands

After the script starts successfully, it waits for commands.

## Configure Camera Time/Timezone

Type:

```text
-r
```

This will:

* Configure timezone settings
* Sync the camera date/time with your computer

Expected output:

```text
Configuration successful...
```

---

## Open Camera Webpage

Type:

```text
-v
```

This opens the camera web interface in your default browser.

Expected output:

```text
Loading webpage...
```

---

## Quit the Program

Type:

```text
-q
```

Expected output:

```text
Closing program...
```

---

# Full Example Session

```bash
python ip_flex_cam_config.py -u admin -p password123 -i 192.168.1.100
```

Then enter:

```text
-r
```

To open the camera webpage:

```text
-v
```

To quit:

```text
-q
```

---

# Troubleshooting

## Authentication Failed

If the program exits immediately:

* Verify the username/password
* Confirm the camera IP address
* Ensure the camera is reachable on the network

Test connectivity:

```bash
ping 192.168.1.100
```

---

## Python Not Found

If you see:

```text
'python' is not recognized
```

Reinstall Python and ensure:

* "Add Python to PATH" is enabled

Or use:

```bash
py ip_flex_cam_config.py
```

---

# Notes

* The script uses HTTP Basic Authentication.
* The timezone values are currently hardcoded in the script.
* The synchronized time is pulled from the computer running the script.

---

# Example Project Structure

```text
project-folder/
│
├── ip_flex_cam_config.py
└── README.md
```
