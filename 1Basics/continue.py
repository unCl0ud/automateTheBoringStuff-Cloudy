while True:
    print('Who are you?')
    name = input()
    if name != "Brian":
        continue
    print('Hello, Brian. What is the password? (Hint it is a cloud.)')
    password = input()
    if password == "cirus":
        break

print("Access Granted")