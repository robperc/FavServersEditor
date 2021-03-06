import CoreFoundation
from Foundation import NSMutableDictionary, NSDictionary, NSMutableArray, NSString

class FavoriteServers(object):

	def __init__(self):
		self.id              = "com.apple.sidebarlists"
		self.favoriteservers = NSMutableDictionary.alloc().initWithDictionary_copyItems_(CoreFoundation.CFPreferencesCopyAppValue("favoriteservers", self.id), True)
		self.items           = NSMutableArray.alloc().initWithArray_(self.favoriteservers["CustomListItems"] if self.favoriteservers.get("CustomListItems") else list())
		self.labels          = [item["Name"] for item in self.items]

	def add(self, label, uri, index=-1):
		if label in self.labels:
			return
		if index == -1 or index > len(self.items):
			index = len(self.items)
		elif index < -1:
			index = 0
		new_item = NSDictionary.alloc().initWithDictionary_(
			dict(
				Name=NSString.alloc().initWithString_(label), 
				URL=NSString.alloc().initWithString_(uri)
			)
		)
		self.items.insert(index, new_item)
		self.labels.append(label)

	def remove(self, label):
		if label not in self.labels:
			return
		for item in reversed(self.items):
			if item["Name"] == label:
				self.items.remove(item)
				self.labels.remove(label)
				return

	def removeAll(self):
		self.items[:]  = []
		self.labels[:] = []

	def move(self, label, index):
		if label not in self.labels:
			return
		if index > len(self.items) or index == -1:
			index = len(self.items)
		elif index < -1:
			index = 0
		for item in self.items:
			if item['Name'] == title:
				to_mv = item
				break
		self.items.remove(item)
		self.items.insert(index, to_mv)

	def swap(self, label1, label2):
		if (label1 not in self.labels) or (label2 not in self.labels) or (label1 == label2):
			return
		for index, item in enumerate(self.items):
			if item['Name'] == label1:
				index1 = index
				item1  = item
			if item['Name'] == label2:
				index2 = index
				item2  = item
		self.items[index1] = item2
		self.items[index2] = item1

	def write(self):
		self.favoriteservers["Controller"]      = NSString.alloc().initWithString_("CustomListItems")
		self.favoriteservers["CustomListItems"] = self.items
		CoreFoundation.CFPreferencesSetAppValue("favoriteservers", self.favoriteservers,  self.id)
		CoreFoundation.CFPreferencesAppSynchronize(self.id)