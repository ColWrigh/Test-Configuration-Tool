import argparse
import webbrowser
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth

parser = argparse.ArgumentParser(
    description="A tool for quickly configuring IP cameras with the correct timezone and date/time"
)
parser.add_argument(
    "-u", "--username", required=True, help="Specify the username of the IP camera."
)
parser.add_argument(
    "-p", "--password", required=True, help="Specify the password of the IP camera."
)
parser.add_argument(
    "-i",
    "--ipaddress",
    required=True,
    help="Specify the IPv4 address of the IP camera.",
)
parser.add_argument("-r", "--run", help="Run the configuration script.")

args = parser.parse_args()

camera_ip = args.ipaddress
username = args.username
password = args.password
now = datetime.now()
url = f"http://{camera_ip}/"
query_url = f"{url}appquery.cgi?"
running = False

timezone_payload = {
    "s_s_st": "0",
    "s_dst_1_mon": "3",
    "s_dst_1_day": "14",
    "s_dst_1_hor": "22",
    "s_dst_1_min": "30",
    "s_dst_2_mon": "11",
    "s_dst_2_day": "6",
    "s_dst_2_hor": "5",
    "s_dst_2_min": "0",
    "s_s_tz": "8",
    "btOK": "submit",
}

sync_time_payload = {
    "s_s_uy": now.year,
    "s_s_um": now.month,
    "s_s_ud": now.day,
    "s_s_uh": now.hour,
    "s_s_ui": now.minute,
    "s_s_us": now.second,
    "s_s_synpct": "on",
    "btOK": "submit",
}

request = requests.get(
    url=url, auth=HTTPBasicAuth(username=username, password=password)
)

if request.status_code == 200:
    running = True

session = requests.Session()
session.auth = HTTPBasicAuth(username, password)


def configure():
    try:
        session.get(url=query_url, params=timezone_payload)
        session.get(url=query_url, params=sync_time_payload)
        print("Configuration successful...")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def view_cam():
    print("Loading webpage...")
    try:
        webbrowser.open(url)
    except webbrowser.Error as e:
        print(f"Error with browser: {e}")


while running:
    try:
        user_input = input()

        match user_input:
            case "-r":
                configure()
            case "-v":
                view_cam()
            case "-q":
                print("Closing program...")
                running = False

    except ValueError:
        print("Invalid input, please enter '-r' to run the program, or '-q' to quit.")
