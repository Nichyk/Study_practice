# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book
# to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books
class Author:
    def __init__(self, name: str, country: str, birthday: str) -> None:
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = list()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'The Author\'s name is {self.name}. He was born {self.birthday} in {self.country}. ' \
               f'Books that were written by him: {self.books}.'


class Book:
    amount = 0

    def __init__(self, name: str, year: int, author: Author) -> None:
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self.name)
        Book.amount += 1

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'The name of the book is {self.name}. It was written in {str(self.year)} by {self.author.name}.'


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books = list()
        self.authors = list()

    def new_book(self, name: str, year: int, author: Author):
        if not isinstance(author, Author):
            raise ValueError('Not an author')
        self.authors.append(author.name)
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author: Author):
        sorted_list = [book.name for book in self.books if book.author == author]
        return sorted_list

    def group_by_year(self, year: int):
        sorted_list = [book.name for book in self.books if book.year == year]
        return sorted_list

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'The name the library is {self.name}. The list of our books: {self.books}. ' \
               f'The list of authors: {self.authors}.'
