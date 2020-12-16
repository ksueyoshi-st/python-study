_spam = ['apples', 'bananas', 'tofu', 'cat']

def _show(_name):
    _num = len(_spam)
    for _i in range(_num):
        if _i < 3:
            print(_spam[_i] + ', ', end='')
        else:
            print('and ' + _spam[_i])

_show(_spam)
