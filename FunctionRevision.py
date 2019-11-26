# e)You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm. Return the total number of legs on your farm. (CREATE A FUNCTION)
# def animals(chicken, cow, pigs):
#     total_legs=2*chicken+4*cow+4*pigs
#     return total_legs
# print(animals(2,3,5))
# print(animals(1,2,3))
# print(animals(5,2,8))


# f)Create a function that takes a list of numbers. Return the largest number in the list.
# def findLargestNum(no1,no2,no3,no4):
#     return max(no1,no2,no3,no4)
# print(findLargestNum(4,5,1,3))
# print(findLargestNum(300,200,600,150))
# print(findLargestNum(1000,1001,857,1))



# g)Given a list of integers, return the difference between the largest and smallest integers in the list.
# def difference (alist):
#     dif=max(alist)-min(alist)
#     return dif
# print(difference([10, 15, 20, 2, 10, 6]))
# print(difference([-3, 4, -9, -1, -2, 15]))



# h) Create a function to concatenate two integer lists.
# def concat(list1,list2):
#     new_list=list1+list2
#     return new_list
# print(concat([1, 3, 5], [2, 6, 8]))
# print(concat([7, 8], [10, 9, 1, 1, 2]))
# print(concat([4, 5, 1], [3, 3, 3, 3, 3]))


# i)Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
# def comp(str1,str2):
#   if len(str1)==len(str2):
#       return "True"
#   else:
#       return "False"
#
# print(comp("AB", "CD"))
# print(comp("ABC", "DE"))
# print(comp("hello", "edabit"))



# j)Write a function that converts a dictionary into a list, where each element represents a key-value pair.

def convert_to_array(dict1):
    alist=[]
    for k,v in dict1.items():
        alist.append([k,v])
        return alist

print(convert_to_array({ "a": 1, "b": 2 }))