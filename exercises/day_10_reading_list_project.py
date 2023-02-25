# #QUESTION
# For this project the application needs to have the following functionality:

# Users should be able to add a book to their reading list by providing a book title,
# an author's name, and a year of publication.
# The program should store information about all of these books in a Python list.
# Users should be able to display all the books in their reading list, 
# and these books should be printed out in a user-friendly format.
# Users should be able to select these options from a text menu, 
# and they should be able to perform multiple operations without restarting the program.


# SOLUTION

readng_list =[]

def main():
    while True:
        try:
            mode = int(input("""Welcome to the book keeper!
            choose an option from the menu (1-3).
            1. add new book
            2. view my books
            3. exit \n>>>
            """))
        

            if mode == 1:
                add_book()
                continue

            elif mode == 2:
                if readng_list:
                    show_book()
                else:
                    print("\nIt's empty in here. Go back and save some books :)\n")
                continue

            elif mode == 3:
                print("exiting book keeper")
                break

            else:
                print("invalid entry\nPlease select a valid option from the menu\n")
                continue
        except ValueError:
                print("invalid entry\nPlease select a valid option from the menu\n")

def add_book():
    book_title =input("add new book title:\n>>> ").lower().strip()
    author =input("add author name:\n>>> ").lower().strip()
    year_of_publication =input("add year of publication:\n>>> ").lower().strip()

    book_details = (book_title,author,year_of_publication)
    book_tuple = tuple(book_details)
    readng_list.append(book_tuple)

    print("new book added successfully")

def show_book():
    for index, book in enumerate(readng_list,1):
        title, author, date = book
        print(f"{index}). {title} -({date}), by {author}\n--------------------\n")



main()