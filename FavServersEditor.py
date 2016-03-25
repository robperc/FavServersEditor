import os
import uuid
import CoreFoundation
from Foundation import NSMutableDictionary


class FavoriteServers(object):

	def __init__(self):
		self.id              = "com.apple.sidebarlists"
		self.favoriteservers = NSMutableDictionary.alloc().initWithDictionary_copyItems_(CoreFoundation.CFPreferencesCopyAppValue("favoriteservers", self.id), True)
		self.items           = self.favoriteservers["CustomListItems"] if self.favoriteservers.get("CustomListItems") is not None else list()
		self.labels          = [server["Name"] for server in self.servers]

	def add(self, label, uri):
		pass

	def remove(self, label):
		pass

	def removeAll(self):
		pass

	def move(self, label, index):
		pass

	def swap(self, label1, label2):
		pass

	def write(self):
		CoreFoundation.CFPreferencesSetAppValue("favoriteservers", self.favoriteservers,  self.id)
		CoreFoundation.CFPreferencesAppSynchronize(self.id)