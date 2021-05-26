# -*- coding: utf-8 -*- 
# @Time     : 2020/9/13 15:22 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第六章:使用一等函数实现设计模式

"""重构"策略"模式"""

"""1. 经典例子,购物车"""

from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class CartItem(object):

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order(object):

    def __init__(self, customer, carts, promotion):
        """

        :type customer: Customer
        """
        self.customer = customer
        self.carts = list(carts)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.carts)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<order total:{:.2f} due:{:.2f}>'
        return fmt.format(self.total(), self.due())


from abc import abstractmethod


class Promotion(object):

    @abstractmethod
    def discount(self, order):
        """返回折扣金额"""


class FidelityPromo(Promotion):
    """为积分一千或者以上的顾客提供5%的折扣"""

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """为单个商品为20个以上时提供10%的折扣"""

    def discount(self, order):
        discount = 0
        for item in order.carts:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):
    """订单中的不同商品达到10个或者以上时提供7%折扣"""

    def discount(self, order):
        distinct_items = {item.product for item in order.carts}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


joe = Customer('John Smith', 0)
ann = Customer('Ann Smith', 1100)
cart = [CartItem('banan', 4, .5),
        CartItem('apple', 10, 1.5),
        CartItem('water_mellon', 5, 5.0)]

print Order(joe, cart, FidelityPromo())
print Order(ann, cart, FidelityPromo())

banana_cart = [CartItem('banana', 30, .05),
               CartItem('apple', 10, 1.5)]

print Order(joe, banana_cart, BulkItemPromo())

long_order = [CartItem(str(item_code), 1, 1.0)
              for item_code in range(10)]
print Order(joe, long_order, LargeOrderPromo())


