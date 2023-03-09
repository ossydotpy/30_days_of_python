# in this module, we are going to tweak our code from day 14 to save our files in JSON format.
# we should also be able to read the data stored as a JSON.

# we will only make changes to the:
# retrieve function
# add_book function
# update function.
import json

def main():
        createfile()
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
                        pass


def retrieveBooks():
        with open('./booksFile.json','r') as books_file:
            return json.load(books_file)         


def addBook():
        books = retrieveBooks()
        
        title = input('input book title:\n>>> ').strip().lower()
        author = input("add author name:\n>>> ").lower().strip()
        year_of_publication = input("add year of publication:\n>>> ").lower().strip()
        readStatus = 'Unread'

        books.append({
        "title": title,
        "author": author,
        "year": year_of_publication,
        "read": "Unread"
        })

        with open('booksFile.json','w') as books_file:
                json.dump(books,books_file)
        print('New Book Added')


def showBooks(booksList):
        print()
        print(f'showing {len(booksList)} saved book(s)')
        print()
        for book in booksList:
                print("{title} - ({year}) by {author} --{read}".format(**book).title())
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
                with open("booksFile.json", "w") as reading_list:
                        json.dump(books,reading_list)
                        

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

def createfile():
        try:
            with open('booksFile.json','x') as booksFile:
                    json.dump([],booksFile)
        except FileExistsError:
                pass

main()