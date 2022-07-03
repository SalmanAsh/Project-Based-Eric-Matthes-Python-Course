# Testing your code
# testing a function


def get_formatted_name(first, last):
    """Generate a full name"""
    full_name = f"{first} {last}"
    return full_name.title()


print("Enter q to exit")
while True:
    first = input("\nPlease give first name")
    if first == 'q':
        break
    last = input("Please give second name")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(formatted_name)

# unit test and test cases
