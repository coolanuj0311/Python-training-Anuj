'''Understanding Copies vs. References:

Assignment (=) doesn't create a new object: It merely creates a new reference to the existing object in memory. Any changes made through either variable will affect the original object.
Copying creates a new, independent object: This allows you to modify one without affecting the other.
Shallow Copy:

Creates a new top-level object, but any nested objects are simply referenced (not copied).
Use the copy() function from the copy module.
Deep Copy:

Creates a completely independent copy, including all nested objects.
Use the deepcopy() function from the copy module:
'''
list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=list1
print("List1 ->",list1)
print("List2 ->",list2)
print("id of List1 ->",id(list1))
print("id of List1 ->",id(list2))
list1.append([10,11,12])
print("List1 ->",list1)
print("List2 ->",list2)

import copy

old_list=[[1,2,3],[4,5,6],[7,8,9]]
new_list=copy.copy(old_list)

print("Old list:", old_list)
print("New list",  new_list)
print("id of old_list ->",id(old_list))
print("id of new_list ->",id(new_list))
old_list.append([4,4,4])
print("Old list:",old_list)
print("New list:",new_list)

old_list[1][1]='AA'
print("Old list:",old_list)
print("New list:",new_list)
old_list[3][1]='BB'
print("Old list:",old_list)
print("New list:",new_list)

import copy
old_list=[[1,1,1],[2,2,2],[3,3,3]]
new_list=copy.deepcopy(old_list)
print("Old list:",old_list)
print("New list:",new_list)
print("id of old_list ->",id(old_list))
print("id of new_list ->",id(new_list))
old_list[1][0]='BB'
print("Old list:",old_list)
print("New list:",new_list)




