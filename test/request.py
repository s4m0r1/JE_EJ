import requests
import os
import sys
from os.path import join, dirname
from dotenv import load_dotenv
import json

#環境変数読み込み
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL = os.environ.get("URL")

args = sys.argv

def main():
    pass

if __name__ == '__main__':
    main()

