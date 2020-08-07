primary_string = input("Enter your word : ")
print("The word is ",len(primary_string)," characters long and it has ", 2**len(primary_string) - 1,"possible combinations")
primary_input = input("Do you want to see the combinations for the word?(y/n) : ")
primary_input = primary_input.lower()

if primary_input == "y":
    #print("Working on it boss!Come back later!")
    new_char = "u"
    position = 1
    internal_string = primary_string[:position] + new_char + primary_string[position+1:]
    print(internal_string)
elif primary_input == "n":
    print("""
          Made by SamSquare.All rights reserved by Sentra Inc.""")


