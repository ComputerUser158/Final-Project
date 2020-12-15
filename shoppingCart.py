"""
Author: Rawley Collins
Program: shoppingCart.py

make a class to hold items
"""


class ShoppingCart(object):

	def __init__(self):
		self.subtotal = 0
		self.items = {}
		self.amount_owed = 0

	def add_items(self, item_number, quantity, price):
		self.subtotal += (price * quantity)
		self.items = {item_number: quantity}

	def drop_items(self, item_number, quantity, price):
		self.subtotal -= (price * quantity)
		if quantity > self.items[item_number]:
			del self.items[item_number]
		self.items[item_number] -= quantity

	def checkout(self):
		TAX = .07
		self.amount_owed = self.subtotal + (self.subtotal * TAX)
		return self.amount_owed

