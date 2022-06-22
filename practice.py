prompt = "Enter the name of the city you visited "
prompt += "(Enter 'quit' to end the program)"

# ex 7-4
prompt = "Enter your age "
prompt += "(Enter 'quit' to end the program)"
age = ""
while age != 'quit':
    if age != 'quit':
        age = input(prompt)
        age = int(age)
        if age < 3:
            print("Ticket is free")
        elif age < 12:
            print("ticket is $10")
        elif age > 12:
            print("ticket is $15")
    else:
        break
