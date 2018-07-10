class Deck:
    def __init__(self):
        #デッキを構築するよ〜
        #ジョーカーを入れるオプションはつけてないよ〜
        card_elem = ["spade","heart","clover","diamond"]
        self.deck = [elem + "_" + str(num) for num in range(1,14) for elem in card_elem]

    def shuffle(self):
        #まぜまぜ〜
        import random
        random.shuffle(self.deck)

    def draw(self,num=1, num_inspect=False):
        #num枚山札から引くよ〜
        #カードに描かれた数値のみ知りたいときはnum_inspectをTrueにして呼び出してね
        cards = []
        for iterate in range(num):
            drawed = self.deck[0]
            cards.append(drawed)
            self.deck.remove(drawed)
        return self.inspect(cards=cards, is_elem=False) if num_inspect == True else cards

    def inspect(self, cards, is_elem=False):
        #カードの属性もしくは数値を調べるよ〜
        #数値を調べたいときはis_elemをFalseにして呼び出してね　int型のリストを返すよ
        idx = 0 if is_elem == True else 1
        inspected = []
        for card in cards:
            inspected.append(card.split("_")[idx])
        if idx == 1:
            inspected = list(map(int, inspected))
        return inspected

    def distribute(self, num=1):
        cards = []
        for dist in range(num):
            self.shuffle()
            cards += self.draw()
        return cards
