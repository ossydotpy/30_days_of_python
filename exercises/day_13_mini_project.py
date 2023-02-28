# This time we're going to be creating a reading list application so that users can store information about books they want to read.
# This should help solidify the concepts we've been learning about over the past week.

# There are actually two versions of today's project, with different levels of difficulty.

# I'd recommend you have a go at the regular version first, because the harder version builds on the regular version,
# adding some more complex functionality.

# Good luck and happy coding!

def main():
    while True:
        try:
                menu_item = int(input("""Welcome to the book keeper!
            choose an option from the menu (1-3).
            1. add new book
            2. view my books
            3. exit \n>>> """).strip())
                if menu_item == 1:
                      add_book()
                      continue
                elif menu_item ==2:
                      show_books()
                      continue
                elif menu_item == 3:
                      print("exiting module...\nSession Ended!")
                      break
                else:
                      print('out of bounds. please select an option between (1-3).\n')
        except ValueError:
              print('invalid input. please select an option between (1-3).\n')
              continue


def add_book():
	book_title =input("add new book title:\n>>> ").lower().strip()
	author =input("add author name:\n>>> ").lower().strip()
	year_of_publication =input("add year of publication:\n>>> ").lower().strip()
	book = f"{book_title},{year_of_publication},{author}\n"
	with open('books.csv','a') as books_file:
		books_file.write(book)

def show_books():
	with open('./books.csv','r') as books_file:
              books = books_file.readlines()
              print(f'You have saved {len(books)} books!\n')
              for index, row in enumerate(books,1):
                    title, author, date = row.strip().split(',')
                    print(f'{index}). {title}, {date} by {author}')
              print()
                    
     

    

        


main()