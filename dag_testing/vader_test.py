import os
import stat
import logging
import paramiko
import pandas as pd
import nltk
from dotenv import load_dotenv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon", quiet=True)
load_dotenv()


def create_sftp_connection():
    host = os.getenv("SFTP_HOST")
    port = int(os.getenv("SFTP_PORT", 22))
    username = os.getenv("SFTP_USER")
    password = os.getenv("SFTP_PASSWORD")
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    return paramiko.SFTPClient.from_transport(transport)


sftp = create_sftp_connection()
sftp.chdir("/course/ITM327/news")
dates = sorted(sftp.listdir())
sftp.close()

print(f"Total dates: {len(dates)}")
print("\n".join(dates))
