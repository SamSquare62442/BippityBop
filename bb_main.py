from itertools import permutations
from math import factorial

primary_string = input("Enter your word : ")
print("The word is ",len(primary_string)," characters long and it has ",factorial(len(primary_string)),"possible combinations")
primary_input = input("Do you want to see the combinations for the word?(y/n) : ")
primary_input = primary_input.lower()

if primary_input == "y":
    result = list(permutations(primary_string))
    total_output = []
    for x,item in enumerate(result):
        final_prod = "".join(item)
        print(x,".",final_prod)
        total_output.append(final_prod)

else:
    print("Ok!Got it!")

saving_prompt = input("Do you want to save the output from the program?(y/n) : ")
saving_prompt = saving_prompt.lower()

if saving_prompt == "y":
    with open("Output.txt","w",encoding="utf-8") as file:
        file.writelines(str(total_output))
    print("\nHave a good day!")

else:
    print("Ok!Have a good day!")


exit_prompt = input("\nPress any key to exit the program. ")
    