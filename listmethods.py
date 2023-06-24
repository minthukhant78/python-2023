list1 = [3,5,2,6,1,4]
list1.sort()
print(list1)
# out [1, 2, 3, 4, 5, 6]
list2 = ['a','b','c','d']
list2.insert(1,'e')
print(list2)
# out ['a', 'e', 'b', 'c', 'd']
list3 = list2.copy()
print (list3)
# out ['a', 'e', 'b', 'c', 'd']
list2.remove('c')
print(list2)
# out ['a', 'e', 'b', 'd']
del list1
print(list1)
# NameError: name 'list1' is not defined. Did you mean: 'list2'?

