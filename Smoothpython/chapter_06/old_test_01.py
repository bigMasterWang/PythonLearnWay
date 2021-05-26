# -*- coding: utf-8 -*- 
# @Time     : 2021/1/6 19:58 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 复习用

from collections import namedtuple
from abc import abstractmethod

Customer = namedtuple('Customer', 'name, credits')


class ShopCart(object):
	"""购物车"""

	def __init__(self, orders, customer, promotion):
		"""

		:type promotion: Promotion
		:type orders: Order
		"""
		self._orders = orders
		self._customer = customer
		self._promotion = promotion

	@property
	def customer(self):
		return self._customer

	@property
	def orders(self):
		return self._orders

	def total(self):
		if not hasattr(self, '_total'):
			self._total = sum([item.total() for item in self.orders])
		return self._total

	def due(self):
		if self._promotion:
			return self.total() - self._promotion(self)
		return self.total()

	def __repr__(self):
		fmt = '<total: {:.2f} due: {:.2f}>'
		return fmt.format(self.total(), self.due())


class Order(object):

	def __init__(self, production, quantity, price):
		self._production = production
		self._quantity = quantity
		self._price = price

	@property
	def production(self):
		return self._production

	@property
	def quantity(self):
		return self._quantity

	@property
	def price(self):
		return self._price

	def total(self):
		return self.quantity * self.price


class Promotion(object):

	@abstractmethod
	def discount(self, shop_cart):
		"""
		:type shop_cart: ShopCart
		"""



def GoodCustomerPromotion(shop_cart):
	"""1000分以上5%折扣"""
	if shop_cart.customer.credits >= 1000:
		return shop_cart.total() * .05
	return 0

def SigletonProductionPromotion(shop_cart):
	result = 0
	for item in shop_cart.orders:
		if item.production > 20:
			result += (item.quantity * item.price) * 0.1
	return result

def ManyDifferentProductionPromotion(shop_cart):
		if len(shop_cart.orders) >= 7:
			return shop_cart.total() * .07
		return 0


# 三个顾客
customer_william = Customer('william', 2000)
customer_zhang = Customer('张冠举', 0)
customer_long = Customer('龙斌', 0)

# 两种购物车
orders_normal = [Order('香蕉', 4, .5), Order('苹果', 10, 1.5), Order('西瓜', 5, 5.0)]
orders_sigleton= [Order('香蕉', 30, .5), Order('苹果', 10, 1.5)]
orders_different = [Order(str(i), 1, 10) for i in range(10)]

print ShopCart(orders=orders_normal, customer=customer_zhang, promotion=GoodCustomerPromotion)
print ShopCart(orders=orders_normal, customer=customer_long, promotion=GoodCustomerPromotion)
print ShopCart(orders=orders_normal, customer=customer_william, promotion=GoodCustomerPromotion)
print ShopCart(orders=orders_normal, customer=customer_william, promotion=SigletonProductionPromotion)
print ShopCart(orders=orders_normal, customer=customer_william, promotion=ManyDifferentProductionPromotion)
print ShopCart(orders=orders_sigleton, customer=customer_william, promotion=SigletonProductionPromotion)
print ShopCart(orders=orders_different, customer=customer_william, promotion=ManyDifferentProductionPromotion)


def best_promotion(shop_car):
	return max([promotion(shop_car) for promotion in [GoodCustomerPromotion, SigletonProductionPromotion, ManyDifferentProductionPromotion]])

print ShopCart(orders=orders_normal, customer=customer_william, promotion=best_promotion)


# 找出该模块中所有的策略
all_promos = [globals()[name] for name in globals().keys() if name.endswith('Promotion')]
print all_promos