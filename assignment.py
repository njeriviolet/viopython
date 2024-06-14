#a program that prompts a user to enter a letter then checks whether it is a consonant or a vowel .

def check_letter_type(letter):
    vowels = "aeiouAEIOU"

    if len(letter) != 1:
        print("Please enter exactly one letter.")
        return

    if letter.isalpha() == False:
        print("Please enter a valid alphabet letter.")
        return

    if letter in vowels:
        print(f"The letter '{letter}' is a vowel.")
    else:
        print(f"The letter '{letter}' is a consonant.")


# Prompt the user to enter a letter
letter = input("Enter a letter: ")

# Call the function to check the type of the entered letter
check_letter_type(letter)




