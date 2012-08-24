# store lots of stuff on the filesystem

import cPickle as pickle
import os, hashlib

class Bigdump:
	"""Store lots of stuff on the filesystem"""
	def __init__(self, base, depth=6):
		# TODO use os path seperator
		if not base.endswith('/'):
			base += '/'
			
		self.base = base
		self.depth = depth

	def _resolve(self, key):
		# compute hash, this will be the filename
		h = hashlib.md5(key).hexdigest()
		
		# abcdefgh --> base/a/b/c/d/
		# TODO use os.path.join
		path = self.base + '/'.join(h[0:self.depth]) + '/'
		
		# --> (base/a/b/c/d/, efgh)
		return (path, h[self.depth:])

	def store(self, key, value):
		"""Store single document"""
		# convert key into path and filename
		path, fn = self._resolve(key)

		try:
			# try to create the directories
			os.makedirs(path)
			pass
		except os.error:
			# directory already exists, we don't care
			pass
		
		# open the file for writing
		# TODO use os.path.join
		f = open(path + fn, 'w')

		# store the value
		pickle.dump(value, f)
		f.close()

	def retrieve(self, key):
		"""Retrieve single document"""
		path, fn = self._resolve(key)
		f = open(path + fn, 'r')
		doc = pickle.load(f)
		f.close()
		return doc
		
	def _allFiles(self):
		for root, dirs, files in os.walk(self.base):
			for name in files:
				yield os.path.join(root, name)

	def all(self):
		"""Iterator over all documents"""	

		for fn in self._allFiles():
			f = open(fn, 'r')
			doc = pickle.load(f)
			f.close()

			yield doc

	def size(self):
		i = 0
		for _ in self._allFiles():
			i += 1

		return i
