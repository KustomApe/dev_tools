class Body:

    def __init__(self, name, parts):
        self.name = name
        self.parts = parts

    def favorite(self):
        print('NAME', self.name, '俺のお気に入りの筋肉部位', self.parts)

# インスタンス生成
mochida = Body('Mochida', '大胸筋')
mochida.favorite()

class Item(Body):
    def __init__(self, name, parts, items):
        super().__init__(name, parts)
        self.items = items

    def favorite(self):
        super().favorite()
        print('この部位を鍛えるにはこのアイテムだ！', self.items)

Futa = Item('Futa', '大胸筋', 'ダンベル')
Futa.favorite()
