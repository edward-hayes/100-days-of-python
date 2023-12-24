# choices = []

# # def repeat(character):
    
# string = ""
# character = "A"
# for num in range(0,5):
#     string = character*(num+1)
#     choices.append(string)

# print(choices)
def choices(character,amount):
    return [character*(num+1) for num in range(0,amount)]

print(choices("👌",5))

list1 = ['1']
list2 = choices("👌",5)
print(list1.extend(list2))