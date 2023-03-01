# For this harder version of the project, the application needs to have the following functionality:

# Users should be able to add a book to their reading list by providing a book title, an author's name, a year of
# publication, and whether or not the book has been read.
# The program should store information about all of these books in a file called books.csv,
# and this data should be stored in CSV format.
# Users should be able to retrieve the books in their reading list, and these books should be printed out in a
# user-friendly format.
# Users should be able to search for a specific book by providing a book title.
# Users should be able to mark a book as read by entering a book title. If there are multiple books with the same title,
# you can just mark the first matching book as read.
# Users should be able to delete books from their reading list by providing the book title for the book they want to
# delete. Once again, you can just delete the first matching book.
# Users should be able to select these options from a text menu, and they should be able to perform multiple operations
# without restarting the program. You can see an example of a working menu in the post on while loops (day 8).# Day 14 

# Project: Reading List (Hard Version)

def main():
        pass


def addBook():
        with open('booksFile.csv','a') as books_file:
                title = input().strip('input book title').lower()
                author = input("add author name:\n>>> ").lower().strip()
                year_of_publication = input("add year of publication:\n>>> ").lower().strip()
                readStatus = False
                book = f"{title}, {year_of_publication}, {author}, {readStatus}, {readStatus}\n"

                books_file.write(book)
        print('New Book Added')

                

def retrieveBooks():
        books = []
        with open('./booksFile.csv','r') as books_file:
                book_data = books_file.readlines()
                for book in book_data:
                        title,author,year = book.strip().split(',')
                        books.append({
                                'title':title,
                                'author':author,
                                'year':year
                        })
        return books


def update_book():
        books =retrieveBooks()
        showBooks()
        edit = []
        choice = print('enter the title of the book you want to update:\n')

        for book in books:
                if choice in books['title']:
                        print(f'you are about to update the status of "{book}"\n')
                        edit.append(book)
                        
        
        
        
        pass

def showBooks():
        pass

def searchBooks():
        pass

def deleteBooks():
        pass



def context_menu(): # function to display the menu items
        menu_item = int(input("""Welcome to the book keeper!\nchoose an option from the menu (1-3).
            1. add new book
            2. view my books
            3. search books
            4. delete book(s)
            n. exit \n>>> """).strip())
        return menu_item
main()