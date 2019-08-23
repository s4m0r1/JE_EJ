import requests
import os
import sys
from os.path import join, dirname
from dotenv import load_dotenv
import json

#環境変数読み込み
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

VERSION = "0.1.2"

URL = os.environ.get("URL")

args = sys.argv

option1 = ""
option2 = ""
trance_word = ""

request_contents = ""

missing_message = """
引数が不正です以下の通りに入力してください

翻訳する場合
    jeej <翻訳する単語の言語> <翻訳後単語> <翻訳する単語>

    例
        jeej ja en こんにちは

    出力例
        Hello

対応言語の確認
    jeej -c

バージョンのチェック
    jeej -v
"""

check_message = """
対応言語
日本語    ja
英語      en
"""

# 国別コード
LAUNGUAGE=["ja","en","kr","cn"]


def main():
    option1, option2, trance_word = args_Check(args)
    other_Message(option1)
    judge = check_Language(option1,option2)
    if judge:
        trancelation_result = request_TranceWord(option1, option2, trance_word)
        print(trancelation_result)

def args_Check(args) -> str:
    global option1
    global option2
    global trance_word
    global missing_message
    global check_message


# ここ冗長だからなんとかする

    if len(sys.argv) == 4:
        option1 = args[1]
        option2 = args[2]
        trance_word = args[3]
    elif len(sys.argv) <= 2:
        option1 = args[1]
    else:
        print(missing_message)
        exit(0)
    
    
    return option1, option2, trance_word


def request_TranceWord(word_launguage: str, trance_launguage: str, trance_word: str) -> str:
    response_url = (URL + "text=" + trance_word + "&source=" + word_launguage + "&target=" + trance_launguage)
    response = requests.get(response_url)
    return response.text


def other_Message(option1: str) -> str:
    global missing_message
    global check_message

    if option1 == "-c":
        print(check_message)
        exit(0)
    elif option1 == "-v":
        print(VERSION)
        exit(0)

def check_Language(option1: str, option2: str) -> bool:
    global LAUNGUAGE
    check_flag = 0
    
    for i in LAUNGUAGE:
        if i == option1:
            check_flag = check_flag + 1
            break
    for j in LAUNGUAGE:
        if j == option2:
            check_flag = check_flag + 1
            break
    
    if check_flag != 2:
        print("言語設定が不正です")
        print(check_message)
        exit(1)
    
    return True
    
if __name__ == '__main__':
    main()

