import re

def valid_value(value, expected_type):
	return value if isinstance(value, expected_type) else None

def get_average_for_list(lst):
	num = 0
	total = .0
	for value in lst:
		total += value
		num += 1
	return total / num

class User:
	"""
	>>> users = []
	>>> for i in range(5): users.append(User("Name" + str(i), "e" + str(i) + "@mail.com"))
	
	>>> users
	[User: Name0, email: e0@mail.com, books read: {}, User: Name1, email: e1@mail.com, books read: {}, User: Name2, email: e2@mail.com, books read: {}, User: Name3, email: e3@mail.com, books read: {}, User: Name4, email: e4@mail.com, books read: {}]

	>>> user = users[0]
	>>> user.get_email()
	'e0@mail.com'
	
	>>> user.change_email("eZero@mail.com")
	Email address has been updated successfully.

	>>> user.get_email()
	'eZero@mail.com'

	>>> user == users[0]
	True

	>>> user == users[1]
	False

	>>> book = Book("Book1", 100000, 10)
	>>> user == book
	Object on the right side of the equality has incompatible type <class '__main__.Book'> (should be of type User)

	>>> user.read_book(book, 5)
	Invalid Rating
	>>> user.read_book(book, 4)

	>>> user.get_average_rating()
	4.0

	"""

	def __init__(self, name, email):
		self.name = valid_value(name, str)
		self.email = valid_value(email, str)
		self.books = {}

	def get_email(self):
		return self.email

	def change_email(self, address):
		self.email = address
		print('Email address has been updated successfully.')

	def __repr__(self):
		return 'User: {name}, email: {email}, books read: {books}'.format(
			name = self.name, email = self.email, books = self.books)

	def __eq__(self, other_user):
		if isinstance(other_user, User):
			return True if self.name == other_user.name and self.email == other_user.email else False
		else:
			print("Object on the right side of the equality has incompatible type {type} (should be of type User)".format(type=type(other_user)))

	def read_book(self, book, rating = None):
		if rating is not None and 0 <= rating <= 4:
			self.books[book] = rating
		else:
			print("Invalid Rating")

	def get_average_rating(self):
		return get_average_for_list(self.books.values()) if len(self.books) > 0 else 0.0

class Book:
	"""
	>>> books = []
	>>> for i in range(5): books.append(Book("Book" + str(i), i + 100000, i + 10))

	>>> books # doctest:+ELLIPSIS
	[<__main__.Book object at 0x...>, <__main__.Book object at 0x...>, <__main__.Book object at 0x...>, <__main__.Book object at 0x...>, <__main__.Book object at 0x...>]

	>>> book = books[0]
	>>> book.get_title()
	'Book0'

	>>> book.get_isbn()
	100000

	>>> book.set_isbn(book.get_isbn() + 10000)
	ISBN has been updated successfully.

	>>> book.get_isbn()
	110000

	>>> book.get_price()
	10

	>>> book == books[0]
	True

	>>> book == books[1]
	False

	>>> book.add_rating(1)
	>>> book.add_rating(3)
	>>> book.add_rating(-1)
	Invalid Rating

	>>> book.get_average_rating()
	2.0


	"""

	def __init__(self, title, isbn, price):
		self.title = valid_value(title, str)
		self.isbn = valid_value(isbn, int)
		self.price = valid_value(price, int)
		self.ratings = []

	def get_title(self):
		return self.title

	def get_isbn(self):
		return self.isbn

	def get_price(self):
		return self.price

	def set_isbn(self, isbn):
		isbn_new = valid_value(isbn, int)
		if isbn_new is not None:
			self.isbn = isbn_new
			print('ISBN has been updated successfully.')

	def add_rating(self, rating):
		if rating is not None and 0 <= rating <= 4:
			self.ratings.append(rating)
		else:
			print("Invalid Rating")

	def get_average_rating(self):
		return get_average_for_list(self.ratings)

	def __eq__(self, other_book):
		if isinstance(other_book, Book):
			return True if self.title == other_book.title and self.isbn == other_book.isbn else False
		else:
			print("Object on the right side of the equality has incompatible type {type} (should be of type Book)".format(type=type(other_book)))

	def	__hash__(self):
		return hash((self.title, self.isbn))

class Fiction(Book):
	"""
	>>> fiction_books = []
	>>> for i in range(5): fiction_books.append(Fiction("Fiction" + str(i), "Author" + str(i), i + 100000, i + 10))

	>>> fiction_books # doctest:+ELLIPSIS
	[Fiction0 by Author0, Fiction1 by Author1, Fiction2 by Author2, Fiction3 by Author3, Fiction4 by Author4]

	>>> fiction_book = fiction_books[0]
	>>> fiction_book.get_author()
	'Author0'

	"""

	def __init__(self, title, author, isbn, price):
		super().__init__(title, isbn, price)
		self.author = valid_value(author, str)

	def __repr__(self):
		return '{title} by {author}'.format(
			title = self.title, author = self.author)

	def get_author(self):
		return self.author

class NonFiction(Book):
	"""
	>>> non_fiction_books = []
	>>> for i in range(5): non_fiction_books.append(NonFiction("NonFiction" + str(i), "Food", "Beginner", i + 100000, i + 10))

	>>> non_fiction_books # doctest:+ELLIPSIS
	[NonFiction0, a Beginner manual on Food, NonFiction1, a Beginner manual on Food, NonFiction2, a Beginner manual on Food, NonFiction3, a Beginner manual on Food, NonFiction4, a Beginner manual on Food]

	>>> non_fiction_book = non_fiction_books[0]
	>>> non_fiction_book.get_subject()
	'Food'

	>>> non_fiction_book.get_level()
	'Beginner'

	"""

	def __init__(self, title, subject, level, isbn, price):
		super().__init__(title, isbn, price)
		self.subject = valid_value(subject, str)
		self.level = valid_value(level, str)

	def __repr__(self):
		return '{title}, a {level} manual on {subject}'.format(
			title = self.title, subject = self.subject, level = self.level)

	def get_subject(self):
		return self.subject

	def get_level(self):
		return self.level

class TomeRater:
	"""
	>>> tome_rater = TomeRater()
	>>> tome_rater
	Tome Rater: 0 users, 0 books.

	>>> tome_rater.users
	{}

	>>> tome_rater.books
	{}

	>>> tr_books = []
	>>> for i in range(5): tr_books.append(tome_rater.create_book("Book" + str(i), i + 100000, i + 10))
	>>> tr_books # doctest:+ELLIPSIS
	[<__main__.Book object at 0x...>, <__main__.Book object at 0x...>, <__main__.Book object at 0x...>, <__main__.Book object at 0x...>, <__main__.Book object at 0x...>]

	>>> tr_fiction_books = []
	>>> for i in range(5): tr_fiction_books.append(tome_rater.create_novel("Fiction" + str(i), "Author" + str(i), i + 100000, i + 10))
	>>> tr_fiction_books
	[Fiction0 by Author0, Fiction1 by Author1, Fiction2 by Author2, Fiction3 by Author3, Fiction4 by Author4]

	>>> tr_non_fiction_books = []
	>>> for i in range(5): tr_non_fiction_books.append(tome_rater.create_non_fiction("NonFiction" + str(i), "Food", "Beginner", i + 100000, i + 10))
	>>> tr_non_fiction_books
	[NonFiction0, a Beginner manual on Food, NonFiction1, a Beginner manual on Food, NonFiction2, a Beginner manual on Food, NonFiction3, a Beginner manual on Food, NonFiction4, a Beginner manual on Food]

	>>> book = tr_books[0]
	>>> tome_rater.add_book_to_user(book, "e@mail.com", 5)
	Invalid Rating
	No user with email e@mail.com!

	>>> tome_rater.books # doctest:+ELLIPSIS
	{<__main__.Book object at 0x...>: 1}

	>>> tome_rater.add_user("User", "e@mail")
	The email has wrong format, please check

	>>> tome_rater.add_user("User", "e@mail.com")
	>>> tome_rater.add_book_to_user(book, "e@mail.com", 4)
	>>> tome_rater.users # doctest:+ELLIPSIS
	{'e@mail.com': User: User, email: e@mail.com, books read: {<__main__.Book object at 0x...>: 4}}

	>>> tome_rater.add_user("User", "e@mail.com")
	User with email 'e@mail.com' already exists

	>>> tome_rater.print_catalog() # doctest:+ELLIPSIS
	<__main__.Book object at 0x...>

	>>> tome_rater.print_users()
	e@mail.com

	>>> tome_rater.most_read_book() # doctest:+ELLIPSIS
	<__main__.Book object at 0x...>

	>>> tome_rater.highest_rated_book() # doctest:+ELLIPSIS
	<__main__.Book object at 0x...>

	>>> tome_rater.most_positive_user() # doctest:+ELLIPSIS
	User: User, email: e@mail.com, books read: {<__main__.Book object at 0x...>: 4}

	>>> tome_rater.get_n_most_read_books(3) # doctest:+ELLIPSIS
	[<__main__.Book object at 0x...>]


	>>> tome_rater.get_n_most_prolific_readers(3) # doctest:+ELLIPSIS
	[User: User, email: e@mail.com, books read: {<__main__.Book object at 0x...>: 4}]

	>>> tome_rater
	Tome Rater: 1 users, 1 books.
	"""

	def __init__(self):
		self.users = {}
		self.books = {}

	def is_isbn_unique(self, isbn):
		isbns = [book.get_isbn() for book in self.books.keys()]
		if isbn in isbns:
			print("The isbn {isbn} is not unique (it already used for another book). Please give a unique isbn.".format(isbn=isbn))
			return False
		else:
			return True

	def create_book(self, title, isbn, price):
		if self.is_isbn_unique(isbn):
			return Book(title, isbn, price)
		return None

	def create_novel(self, title, author, isbn, price):
		if self.is_isbn_unique(isbn):
			return Fiction(title, author, isbn, price)
		return None

	def create_non_fiction(self, title, subject, level, isbn, price):
		if self.is_isbn_unique(isbn):
			return NonFiction(title, subject, level, isbn, price)
		return None

	def add_book_to_user(self, book, email, rating = None):
		book.add_rating(rating)

		if email not in self.users:
			print("No user with email {email}!".format(
				email = email))
		else:
			self.users[email].read_book(book, rating)

		self.books[book] = 1 if book not in self.books else self.books[book] + 1

	def add_user(self, name, email, user_books = None):
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			print("The email has wrong format, please check")
			return
		elif email not in self.users:
			self.users[email] = User(name, email)
		else:
			print("User with email '{email}' already exists".format(email=email))
			return

		if user_books is not None:
			for book in user_books:
				self.add_book_to_user(book, email)

	def print_catalog(self):
		for book in self.books:
			print(book)

	def print_users(self):
		for user in self.users:
			print(user)

	def most_read_book(self):
		read_cnt_max = 0
		popular_book = None
		for book, read_cnt in self.books.items():
			if read_cnt_max < read_cnt:
				popular_book = book
				read_cnt_max = read_cnt
		return popular_book

	def highest_rated_book(self):
		average_rating_max = 0
		highest_rated_book = None
		for book in self.books:
			average_rating = book.get_average_rating()
			if average_rating_max < average_rating:
				highest_rated_book = book
				average_rating_max = average_rating
		return highest_rated_book

	def most_positive_user(self):
		average_rating_max = 0
		positive_user = None
		for user in self.users.values():
			average_rating = user.get_average_rating()
			if average_rating_max < average_rating:
				positive_user = user
				average_rating_max = average_rating
		return positive_user

	def get_n_most_read_books(self, n):
		if type(n) == int:
			books_sorted = [book for book in sorted(self.books, key=self.books.get, reverse=True)]
			return books_sorted[:n]
		else:
			print("Please specify integer argument (the provided argument has type {type})".format(type=type(n)))

	def get_n_most_prolific_readers(self, n):
		if type(n) == int:
			users = [(user, len(user.books)) for user in self.users.values()]
			prolific_readers = [user[0] for user in sorted(users, key=lambda user: user[1], reverse=True)]
			return prolific_readers[:n]
		else:
			print("Please specify integer argument (the provided argument has type {type})".format(type=type(n)))

	def get_n_most_expensive_books(self, n):
		if type(n) == int:
			books = {book: book.get_price() for book in self.books}
			most_expensive_books = [book for book in sorted(books, key=books.get, reverse=True)]
			return most_expensive_books[:n]
		else:
			print("Please specify integer argument (the provided argument has type {type})".format(type=type(n)))

	def __repr__(self):
		return 'Tome Rater: {num_of_users} users, {num_of_books} books.'.format(
			num_of_users = len(self.users), num_of_books = len(self.books))

	def __eq__(self, other_tome_rater):
		# very primitive version of the comparison ... to be modified further based on real use cases
		if isinstance(other_tome_rater, TomeRater):
			return True if len(self.users) == len(other_tome_rater.users) and len(self.books) == len(other_tome_rater.books) else False
		else:
			print("Object on the right side of the equality has incompatible type {type} (should be of type TomeRater)".format(type=type(other_tome_rater)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
