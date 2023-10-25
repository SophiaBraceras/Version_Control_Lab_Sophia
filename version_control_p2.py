# Sophia Braceras

def encoder(code):
    list = []
    newlist = []
    for letter in code:
        list.append(letter)
    for i in list:
        add = 3
        i = int(i)
        add += i
        #print(add, end="")
        newlist.append(add)

    final = ''.join(map(str, newlist))

    return final

# number = input("Number to encode:")
# print(encoder(number))

def decoder():
    pass
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def main():
    menu()
    # option = input("Please enter an option: ")
    while True:
        option = input("Please enter an option: ")
        if option == "1":
            num = input("Please enter your password to encode: ")
            encoder(num)
            print("Your password has been encoded and stored!")

        if option == "2":
            # num = input("Please enter your password to encode: ")
            print(f"The encoded password is {encoder(num)} and the original password is {decoder(num)}")


        if option == "3":
            break



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

