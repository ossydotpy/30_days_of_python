# This time we're going to be creating a reading list application so that users can store information about books they want to read.
# This should help solidify the concepts we've been learning about over the past week.

# There are actually two versions of today's project, with different levels of difficulty.

# I'd recommend you have a go at the regular version first, because the harder version builds on the regular version,
# adding some more complex functionality.

# Good luck and happy coding!

def main():
    while True:
        try:
                option = context_menu()
                if option == 1:
                      add_book()
                      continue
                elif option ==2:
                      books = get_books()
                      if books:
                            print(f'You have saved {len(books)} books!\n')
                            show_books(books)
                            continue
                elif option == 3:
                      search_results = search_book()
                      if search_results:
                             if len(search_results) ==1:
                                    print('1 item match your query\n')
                             else:
                                    print(f'{len(search_results)} items match your query\n')
                             show_books(search_results)
                      else:
                              print("No matching records found!\nTry a new term.\n")
                      continue
                elif option == 4:
                      print("exiting module...\nSession Ended!")
                      break
                else:
                      print('out of bounds. please select an option between (1-3).\n')
        except ValueError:
              print('invalid input. please select an option between (1-3).\n')
              continue




def add_book(): # function to create a book and save to our output file
        book_title =input("add new book title:\n>>> ").lower().strip()
        author =input("add author name:\n>>> ").lower().strip()
        year_of_publication =input("add year of publication:\n>>> ").lower().strip()
        book = f"{book_title},{year_of_publication},{author}\n"
        with open('books.csv','a') as books_file:
                books_file.write(book)
        print('book saved successfully!')
        print()

def get_books(): # function to retrieve the book list from our file.
       books = []
       with open('./books.csv','r') as books_file:
              book_list = books_file.readlines() # read icontent of the file by line and save to  book_list
              for index, row in enumerate(book_list,1):
                     title, author, date = row.strip().split(',')
                     books.append({     # saves retrieved books in a dictionary format
                            'book_title':title,
                            'book_author':author,
                            'release_date':date
                     })
              return books

def show_books(books): # function to display the saved books.
        for index,book in enumerate(books,1):
               print(f"{index}). {book['book_title']} - ({book['release_date']}) by {book['book_author']}")
        print()

def search_book(): #search function
       books = get_books() # gets the books dictionary from get_books() function
       matching_books = [] # list to store matching books
       keyword =  input("Search for a book title: \n-> ").strip().lower()
       print()
       for book in books:
              if keyword in book['book_title'].lower():
                     matching_books.append(book)
       return matching_books


def context_menu(): # function to display the menu items
        menu_item = int(input("""Welcome to the book keeper!
            choose an option from the menu (1-3).
            1. add new book
            2. view my books
            3. search books
            4. exit \n>>> """).strip())
        return menu_item

main()