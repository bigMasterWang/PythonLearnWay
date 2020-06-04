import collections
from random import choice

# collections.namedtuple被用来构建一个只有少数属性但是没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = '红桃 方片 黑桃 梅花'.split()
    suit_values = dict(黑桃=3, 红桃=2, 方片=1, 梅花=0)

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    # python的长度的方法默认都是调用__len__()
    def __len__(self):
        return len(self._cards)

    # python的collection[]的方法默认就是调用__getitem__()方法
    # 这个是[]的操作权限
    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(FrenchDeck.suit_values) + FrenchDeck.suit_values[card.suit]


deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
print(deck.__getitem__(0))

print(choice(deck))
print(deck.ranks)

# __len__()方法把len()操作也交给了self._cards
# __getitem__方法把[]操作交给了self._cards，直接支持切片操作和迭代

print(deck[12:13:1])
print(deck[12::13])

# for item in deck:
#     print(item)
#
# for item in reversed(deck):
#     print(item)

# 如果一个集合类型没有实现__contains__()方法，那么in操作就会
# 按顺序做一次迭代搜索，所以in就可以用在FrenchDeck类上
print(Card('A', "红桃") in deck)

for card in sorted(deck, key=spades_high):
    print(card)
