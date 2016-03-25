import CoreFoundation
from Foundation import NSMutableDictionary, NSMutableArray


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
		new_item = dict(
			Name=label,
			URL=uri
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
		pass

	def swap(self, label1, label2):
		pass

	def write(self):
		self.favoriteservers["CustomListItems"] = self.items
		CoreFoundation.CFPreferencesSetAppValue("favoriteservers", self.favoriteservers,  self.id)
		CoreFoundation.CFPreferencesAppSynchronize(self.id)