import itertools

primary_string = input("Enter your word : ")
print("The word is ",len(primary_string)," characters long and it has ", 2**len(primary_string) - 2,"possible combinations")
primary_input = input("Do you want to see the combinations for the word?(y/n) : ")
primary_input = primary_input.lower()

if primary_input == "y":
    result = list(itertools.permutations(primary_string))

    for x,item in enumerate(result):
        final_prod = "".join(item)
        print(x,final_prod)
    print("Made by SamSquare")

else:
    print("Made by SamSquare")








