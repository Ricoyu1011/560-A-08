import sys

while True:
    file_variable = input('''
    what file would you like to search for?:
    a) 70s_rock_music file
    b) 60s_music file
    x) to exit
    ''')

    if file_variable == "x" :
        sys.exit()
    elif file_variable == "a" :
        file_variable = "70s_rock_music.csv"
    elif file_variable == "b" :
        file_variable = "60s_music.csv"
    else:
        print("Invalid opion. Please select a, b, or x.")
        continue
    
    search_variable = input(f"Enter the search term for {file_variable} file: ")
    search_variable = search_variable.title()

    def find(file_variable,search_variable):
        with open(file_variable, "r") as file:
            content = file.read()

        if search_variable in content:

            print(f"Your search term {search_variable} exists in the {file_variable} file!")
            see_entries = input("would you like to see the entries? (y or n)?")

            if see_entries.lower() == "y":
                print(f"Here are all of the entries with the term {search_variable}:")
                with open(file_variable,"r") as file:
                    for line in file:
                        if search_variable in line:
                            print(line.strip())

            elif see_entries.lower() == "n":
                print("Goodbye")
                sys.exit()

            else:
                print("Invalid option. Please enter y or n.")
            
        else:
            print(f'{search_variable} does no exist in {file_variable}')

    find(file_variable, search_variable)
