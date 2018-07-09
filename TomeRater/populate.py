from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)
novel3_copy = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", [book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)



#Uncomment these to test your functions:
print('\nChange email of a user:')
Tome_Rater.change_email('marvin@mit.edu', 'marvin@google.com')

print('\nTry to change email of a user to a faulty email:')
Tome_Rater.change_email('marvin@mit.edu', 'marvingoogle.com')
    
print('\nTry to add user with faulty email:')
Tome_Rater.add_user('Jeffery Lebowski','theDude@abide')

print('\nTry to add user with email that already exist.')
Tome_Rater.add_user('Jeffery Lebowski','david@computation.org')

print('\nTry to add a book with an ISBN that already exists.')
book2 = Tome_Rater.create_book("The Bible", 12345678)
    
print('\nCatalog:')
Tome_Rater.print_catalog()
print('\nUsers:')
Tome_Rater.print_users()

print("\nMost positive user:")
print(Tome_Rater.most_positive_user())
print("\nHighest rated book:")
print(Tome_Rater.highest_rated_book())
print("\nMost read book:")
print(Tome_Rater.most_read_book())
print('\nAre novel3 and novel3_copy the same book?')
print(novel3_copy == novel3_copy)