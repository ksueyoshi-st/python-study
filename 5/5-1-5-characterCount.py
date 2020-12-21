_message = 'the was brigth cold day in April, and the colocks were striking thirteen'
_count = {}

for _character in _message:
    _count.setdefault(_character, 0)
    _count[_character] = _count[_character] + 1

print(_count)
