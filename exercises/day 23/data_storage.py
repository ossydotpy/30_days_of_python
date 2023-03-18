
def read_column(col_num):
    column_data = []
    with open('./iris.csv','r') as irisFile:
        try:
            for row in irisFile.readlines()[1:]:
                data = row.strip().split(',')
                column_data.append(data[col_num])
        except IndexError:
            print('invalid index')
    return column_data