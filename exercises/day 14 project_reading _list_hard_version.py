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
        while True:
                try:
                        choice = context_menu()
                        if  choice == 1:
                                addBook()
                                continue
                        elif choice==2:
                                books = retrieveBooks()
                                if books:
                                        showBooks(books)
                                continue
                        elif choice == 3:
                                results = searchBooks()
                                if results:
                                        showBooks(results)
                                else:
                                        print(' no matching records')
                                continue
                        elif choice ==4:
                               update_reading_list(deleteBook)

                        elif choice == 5:
                               update_reading_list(markRead)
                               continue
                                
                        elif choice == 6:
                               print('exiting module...\nsession ended!')
                               break
                        
                        else:
                                print('select a valid option from (1-6)')


                except ValueError:
                        print('ll')
               

def addBook():
        with open('booksFile.csv','a') as books_file:
                title = input('input book title:\n>>> ').strip().lower()
                author = input("add author name:\n>>> ").lower().strip()
                year_of_publication = input("add year of publication:\n>>> ").lower().strip()
                readStatus = 'Unread'
                book = f"{title}, {author}, {year_of_publication}, {readStatus}\n"

                books_file.write(book.lower())
        print('New Book Added')


def retrieveBooks():
        books = []
        with open('./booksFile.csv','r') as books_file:
                book_data = books_file.readlines()
                for book in book_data:
                        title,author,year,readStatus = book.strip().split(',')
                        books.append({
                                'title':title,
                                'author':author,
                                'year':year,
                                'status':readStatus
                        })
        return books


def showBooks(booksList):
        print()
        print(f'showing {len(booksList)} saved book(s)')
        print()
        for index, book in enumerate(booksList,1):
                details =(f"{index}). {book['title']} - ({book['year']}) by {book['author']} --{book['status']}")
                print(details.title())
                print()


def searchBooks():
        books = retrieveBooks()
        matches = []
        query = input('Enter a search term:\n>>> ').strip().lower()
        print()
        for book in books:
                if query in book['title']:
                        matches.append(book)
        return matches

      
# function called to perform an action[delete/mark] on a book                 
def update_reading_list(function):
        books = retrieveBooks()
        matching_books = searchBooks()

        if matching_books:
                function(books, matching_books[0])
                with open("booksFile.csv", "w") as reading_list:
                        for book in books:
                                reading_list.write(f"{book['title']},{book['year']},{book['author']},{book['status']}\n")
        else:
                print("No matching results. Search for another book.\n")

# mark as read
def markRead(booksList,toUpdate):
        match_index = booksList.index(toUpdate)
        confirm = input(f'are you sure you want to delte {toUpdate["title"]}? Y/N\n>>> ').strip().lower()
        if confirm == 'y':
                booksList[match_index]['status'] = 'Read'
                print(f'{toUpdate["title"]} marked as read!\n')
        elif confirm == 'n':
                print('book not updated\n')

# delete a book
def deleteBook(booksList, toDelete):
        confirm = input(f'are you sure you want to delte {toDelete["title"]}? Y/N\n>>> ').strip().lower()
        if confirm == 'y':
                booksList.remove(toDelete)
                print("book removed successfully!\n")
        elif confirm == 'n':
                print('book not deleted\n')



def context_menu(): # function to display the menu items
        menu_item = int(input("""Welcome to the book keeper!\nchoose an option from the menu (1-3).
            1. add new book
            2. view my books
            3. search books
            4. delete books(s)
            5. mark book as read
            6. exit \n>>> """).strip())
        return menu_item

main()