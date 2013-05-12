#/usr/bin/python

class Fruit(object):
	pass

class GiftMixin(object):
	def is_gift_fruit(self):
		return True

class NotGiftMixin(object):
	def is_gift_fruit(self):
		return False

class PareMixin(object):
	def eat_method(self):
		return "Pare"

class HuskMixin(object):
	def eat_method(self):
		return "Husk"

class Apple(GiftMixin, PareMixin, Fruit):
	pass

class Pear(NotGiftMixin, PareMixin, Fruit):
	pass

class Orange(GiftMixin, HuskMixin, Fruit):
	pass

class Banana(NotGiftMixin, HuskMixin, Fruit):
	pass

