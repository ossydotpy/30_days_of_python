from data_storage import read_column
from graphing import scatter


def main():
    choice = int(input("""
        choose an option from the list below:
        1. create chart
        2. quit
    """).strip())

    while True:
        choice
        if choice==1:
            try:
                col_num = int(input('enter the number of the column you want to chart?:'))
                file_name = input("enter your desired filename: ")
                chart(col_num,filename=file_name)
            except (IndexError,ValueError):
                print('invalid column')
                continue
        elif choice == 2:
             break
        print('done')
        break

def chart(col,filename):
        y = [float(n) for n in read_column(col)]
        x = read_column(-1)
        scatter(x,y,filename)


main()