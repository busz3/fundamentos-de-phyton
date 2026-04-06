# my_list = [] # Criando uma lista vazia.

# for i in range(21):
#    my_list.append (i)

# print (my_list)

###
# my_list2 = []  # Criando uma lista vazia.
 
# for i in range(21):
#     my_list2.insert(0, i)
 
# print(my_list2)

###
# my_list = [10, 1, 8, 3, 5]
# total = 0
 
# for i in my_list:
#     total += i
 
# print(total)
 
###
length = 0
my_list = [0]
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)
 
