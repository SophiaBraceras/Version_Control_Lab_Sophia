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


# This function was written by Ethan Gomez
def decode(encoded_pass):
    print(f"Entered Pass: {encoded_pass}")
    encoded_pass = list(encoded_pass)

    # Loops through every index in the encoded password
    for index in range(len(encoded_pass)):
        encoded_pass[index] = int(encoded_pass[index]) - 3
        # If the -3 made it negative, add 10.
        if encoded_pass[index] < 0:
            encoded_pass[index] += 10
        encoded_pass[index] = str(encoded_pass[index])

    return "".join(encoded_pass)

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
            # encoded variable created by Ethan for the decoder to work
            encoded = encoder(num)
            print("Your password has been encoded and stored!")

        if option == "2":
            # num = input("Please enter your password to encode: ")
            print(f"The encoded password is {encoder(num)} and the original password is {decoder(encoded)}") # decoder(num) changed by Ethan to decoder(encoded)


        if option == "3":
            break



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

