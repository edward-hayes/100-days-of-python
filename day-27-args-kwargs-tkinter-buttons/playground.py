def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return(sum)


print(add(1,2,3))
# list = []

# while True:
#     numbers = input("enter numbers then type add to add:")
    
#     if numbers.isnumeric():
#         list.append(int(numbers))
#     elif numbers.lower() == "add":
#         print(list)
#         result = add(list)
#         print(result)
#         list.clear()
#     else:
#         print("not valid argument")
    
    