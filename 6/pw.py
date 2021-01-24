#! python3
# pw.py - パスワード管理プログラム(脆弱性あり)


PASSWORDS = {'email': 'emailpassword',
             'blog': 'blogpassword',
             'luggage': 'luggagepassword'}


import sys
import pyperclip

# 引数がない場合終了
if len(sys.argv) < 2:
    print('使い方: python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

# 最初のコマンドライン引数がアカウント名
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account + 'というアカウントはありません')

