import itertools
string = input("Enter the word : ")

result = list(itertools.permutations(string))



for x,item in enumerate(result):
    final_prod = "".join(item)
    print("(",x,")",final_prod)