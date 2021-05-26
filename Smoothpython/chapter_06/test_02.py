# -*- coding: utf-8 -*-
# @Time     : 2020/9/13 21:41
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

"""使用函数实现策略模式"""

# 看了网上很多博客在写这个东西,看了很多,最后总结一句话"都是在放屁"
# 现在我们从python2.7的API里面去看,到底这个select.select()到底是怎么回事



from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')


class ShopCart(object):
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price

class Order(object):

    def __init__(self, customer, shop_carts, promotion):
        self.customer = customer
        self.shop_carts = list(shop_carts)
        self.promotion = promotion

    def total(self):
        return sum([cart.total() for cart in self.shop_carts])

    def due(self):
        return self.total() - self.promotion(self)

    def __repr__(self):
        return 'total: '+str(self.total())+', due: '+str(self.due())

def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """为单个商品20个以上时提供10%折扣"""
    return sum([cart.total() * .1 for cart in order.shop_carts if cart.quantity >= 20])

def larger_order_promo(order):
    """订单中的不同商品数目打到10个或者以上提供7%折扣"""
    if len([card.product for card in order.shop_carts]) >= 10:
        return order.total() * .07
    return 0

c1 = Customer('c1', 0)
c2 = Customer('c2', 1200)

cards_list_one = [ShopCart('apple', 1000, 5)]

print Order(customer=c2, shop_carts=cards_list_one, promotion=fidelity_promo)
print Order(customer=c2, shop_carts=cards_list_one, promotion=bulk_item_promo)
print Order(customer=c2, shop_carts=cards_list_one, promotion=larger_order_promo)


# 说白了就是因为函数可以赋给其他变量而已


# 选择最佳策略
promos = [fidelity_promo, bulk_item_promo, larger_order_promo]
def best_promo(order):
    return max(promo(order) for promo in promos)

print Order(customer=c2, shop_carts=cards_list_one, promotion=best_promo)


x = [globals()[name] for name in globals() if name.endswith('_promo') and name != 'best_promo']