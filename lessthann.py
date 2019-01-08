a = [1,2,3,4,4,3,56,6,48,32]

num = int(input("Choose a number: "))

new_list = []

for i in a:
    if i < num: 
        new_list.append(i)

print(new_list)