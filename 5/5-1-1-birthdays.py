_birthdays = {'アリス': '4/1', 'ボブ': '12/12', 'キャロル': '4/4' }

while True:
    print('名前を入力してください: (終了するにはEnterだけを押してください)')
    _name = input()
    if _name == '':
        break

    if _name in _birthdays:
        print(_name + 'の誕生日は' + _birthdays[_name])
    else:
        print(_name + 'の誕生日は未登録です。')
        print('誕生日を入力してください。')
        _bday = input()
        _birthdays[_name] = _bday
        print('誕生日データベースを更新しました')
        print('現在の誕生日データベースです')
        print(_birthdays)
