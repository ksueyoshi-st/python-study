def _display_inventory(_inventory):
    print('持ち物リスト:')
    _item_total = 0
    for _k, _v in _inventory.items():
        print(_v, _k)
        _item_total = _item_total + _v
    print('アイテム総数:' + str(_item_total))

        
def _add_to_inventory(_inventory, _added_items):
    # ここに書く
    for _get_item in _added_items:
        _inventory.setdefault(_get_item, 0)
        _inventory[_get_item] += 1
    return _inventory

_inv = {'金貨': 42, 'ロープ': 1}
_dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']

_inv = _add_to_inventory(_inv, _dragon_loot)

_display_inventory(_inv)
