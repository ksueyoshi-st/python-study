import pprint

_message = 'It was a brigth cold day in April, and the clock were striking thirteen'
_count = {}

for _character in _message:
    _count.setdefault(_character, 0)
    _count[_character] = _count[_character] + 1

pprint.pprint(_count)
