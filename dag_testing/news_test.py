import os
import stat
import logging
import paramiko
from dotenv import load_dotenv

load_dotenv()


def create_sftp_connection():
    host = os.getenv("SFTP_HOST")
    port = int(os.getenv("SFTP_PORT", 22))
    username = os.getenv("SFTP_USER")
    password = os.getenv("SFTP_PASSWORD")
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    return paramiko.SFTPClient.from_transport(transport)


def is_directory(sftp, path):
    try:
        return stat.S_ISDIR(sftp.stat(path).st_mode)
    except IOError:
        return False


def list_files(sftp, folder):
    sftp.chdir(folder)
    return [f for f in sftp.listdir() if not is_directory(sftp, f)]


import io
import pandas as pd

sftp = create_sftp_connection()

sftp.chdir("/course/ITM327/news")
dates = sftp.listdir()
print("Date folders:", dates[:5])

# Grab the first file in the first date folder
first_date = dates[0]
sftp.chdir(f"/course/ITM327/news/{first_date}")
files = sftp.listdir()
print("Files:", files[:5])

# Read first file into a dataframe
with sftp.open(files[0], "r") as f:
    df = pd.read_csv(f)

print("\nColumns:", df.columns.tolist())
print("\nSample row:")
print(df.head(1).to_string())

sftp.close()
