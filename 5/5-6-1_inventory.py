def _display_inventory(_inventory):
    print('持ち物リスト:')
    _item_total = 0
    for _k, _v in _inventory.items():
        print(_v, _k)
        _item_total = _item_total +  _v
    print("アイテム総数: " + str(_item_total))

_stuff = {'ロープ': 1,
          'たいまつ': 6,
          '金貨': 42,
          '手裏剣': 1,
          '矢': 12}

_display_inventory(_stuff)
