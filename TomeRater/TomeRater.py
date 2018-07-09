# TomeRater by Martin Hedén, martin.heden@gmail.com
# Implemented some extra error handling and a change email method to TomeRater.

# Function to check if email is on the correct format and not already included in users.
def check_email(email, users = None):
    email_OK = True
    # Check that email contains @ and .com, .edu or .org
    if not '@' in email or not any(x in email for x in ['.com', '.edu', '.org']):
        print('The email ' + email + ' lacks @ or does not contain .com, .edu or .org')
        email_OK = False
    # Check if email already exists in users (if users are provided).
    if users != None and email in users:
        print('A user with the email ' + email + ' already exists!')
        email_OK = False
    return email_OK

#### Class definitions ####
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
    def get_email(self):
        return self.email
    def change_email(self, address):
        self.email = address
        print('The email address of user ' + self.name + ' has been changed to: ' + self.email)
    def __repr__(self):
        return 'User ' + self.name + ', email: ' + self.email + ', no of books read: ' + str(len(self.books))
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
    def read_book(self, book, rating = None):
        self.books[book] = rating                  
    def get_average_rating(self):
        ratings = []
        for rating in self.books.values():
            if rating != None:
                ratings.append(rating)
        if len(ratings) == 0:
            return -1 # How should we handle users that have given no ratings?
        else:
            return sum(ratings)/len(ratings) # Average of ratings


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    def __repr__(self):
        return self.title + ' with ISBN ' + str(self.isbn)
    def get_title(self):
       return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self, isbn):
        self.isbn = isbn
        print('The ISBN of ' + self.title + ' has been updated to ' + str(self.isbn))
    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print('Invalid Rating')
    def __eq__(self, other_book):
        if self.title == other_book.get_title and self.isbn == other_book.get_isbn:
            return True
        else:
            return False
    def get_average_rating(self):
        if len(self.ratings) == 0:
            return -1 # How should we handle users that have given no ratings?
        else:
            return sum(self.ratings)/len(self.ratings)
    def __hash__(self):
        return hash((self.title, self.isbn))
            
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    def get_author(self):
        return self.author
    def __repr__(self):
        return self.title + ' by ' + self.author
    
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        return self.title + ', a ' + self.level + ' manual on ' + self.subject

    
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
    def create_book(self, title, isbn):
        isbn_unique = True
        for book in self.books:
            # Check if book with this ISBN already exists.
            if isbn == book.isbn:
                isbn_unique = False
                break
        if not isbn_unique:
            print('A book with the ISBN '+ str(isbn) + ' already exists!')
        else:
            return Book(title, isbn)
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            user = self.users[email]
            user.read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print('No user with email ' + email + '!')
    def add_user(self, name, email, books = None):
        if check_email(email, self.users):
            self.users[email] = User(name, email)
            if books != None:
                for book in books:
                    self.add_book_to_user(book, email)
    def change_email(self, old_email, new_email):
        # Implemented a change email method  which was not in the specification.
        if check_email(new_email, self.users):
            self.users[old_email].change_email(new_email) # Change email in the user object.
            self.users[new_email] = self.users.pop(old_email) # Change the key for the user in self.users (since the key is the email).
    def print_catalog(self):
        for book in self.books:
            print(book)
    def print_users(self):
        for user in self.users:
            print(user)
    def most_read_book(self):
        most_read_book = Book('dummy', 0)
        most_readings = 0
        # The keys of self.books are Books, and the values are how many times they’ve been read.
        for key in self.books:
            if self.books[key] > most_readings:
                most_read_book = key
                most_readings = self.books[key]
        return most_read_book
    def highest_rated_book(self):
        highest_rated = Book('dummy', 0)
        # The keys of self.books are Books.
        for key in self.books:
            if key.get_average_rating() > highest_rated.get_average_rating():
                highest_rated = key
        return highest_rated
    def most_positive_user(self):
        positive_user = User('dummy', 'dummy')
        # The values of self.users are Users
        for key in self.users:
            if self.users[key].get_average_rating() > positive_user.get_average_rating():
                positive_user = self.users[key]
        return positive_user
        
