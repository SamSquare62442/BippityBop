primary_string = input("Enter your word : ")
print("The word is ",len(primary_string)," characters long and it has ", 2**len(primary_string) - 1,"possible combinations")
primary_input = input("Do you want to see the combinations for the word?(y/n) : ")
primary_input = primary_input.lower()

if primary_input == "y":
    primary_list = list(primary_string)
    primary_list.sort(reverse=True)
    print(primary_list)
    print("".join(primary_list))
    print(primary_list)


