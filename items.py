"""
Author: Rawley Collins
Program: shoppingCart.py

make a list of items
"""


class Items:
	def __init__(self, item, no_of_items, item_price, description):
		self.itemId = item
		self.quantity = no_of_items
		self.price = item_price
		self.item = description


# make a save cart option? only has to update once or when the button is clicked?
