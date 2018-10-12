class Author:
	"""docstring for Author"""
	def __init__(self, firstname,lastname):
		self.firstname = firstname
		self.lastname = lastname

	def __str__(self):
		return str(self.firstname) + ' ' + self.lastname 
		
class Book:

	def __init__(self, bookname, author, pagenumbers, isbn):
		self.bookname = bookname
		self.author = []
		self.author.append(author)
		self.pagenumbers = pagenumbers
		self.isbn = isbn

	def add_author(self, firstname, lastname):
		self.author.append(Author(firstname, lastname))

	def name(self):
		return self.bookname

	def __str__(self):
		res = "bookname: " + self.bookname
		for n in self.author:
			res = res + "\n" + str(n)
		return res

	def __gt__(self, other):
		return self.pagenumbers > other.pagenumbers

	def __eq__(self, other):
		return self.pagenumbers == other.pagenumbers
		