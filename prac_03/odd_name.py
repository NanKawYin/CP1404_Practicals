def main():
    """NanKawYin"""

    name, name_count = get_name()
    print_name(name, name_count)


def print_name(name, name_count):
    print("Your name is: ", end='')
    print(name[0:name_count:3])


def get_name():
    name = str(input("Enter Your Name: "))
    name_count = len(name)
    while name_count == 0:
        print("User name cannot be empty.")
        name = input("Enter Your Name: ")
        name_count = len(name)
    return name, name_count


main()