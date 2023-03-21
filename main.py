def read_file():
    file_name = input("What is the name of the file you would like to read (text files only) ")
    file = open(file_name, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip('\n')
        print(line)

    file.close()
def add_file_to_list():
    file_name = input("Please enter the name of the file: ")
    new_list=[]
    file = open(file_name, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip('\n')
        new_list.append(line)

    print('ready to print off the list now :)')
    print(new_list)

    for i in new_list:
        print(i)



if __name__ == '__main__':
    choice = int(input('please press 1 for print, 2 for adding to list'))
    if choice == 1:
        read_file()
    elif choice == 2:
        add_file_to_list()
    else:
        print('you have chose an invalid choice')
