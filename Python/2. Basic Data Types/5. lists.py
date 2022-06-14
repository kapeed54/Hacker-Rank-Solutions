# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.


N = int(input())
l = []
for _ in range(N):
    arr = input().split();
                   
    #insert i e : insert integer e at positon i.
    if arr[0] == "insert":
        l.insert(int(arr[1]),int(arr[2]))
        
    #print list
    elif arr[0] == "print":
        print(l)
        
    #remove e: delete the first occurance of e
    elif arr[0] == "remove":
        l.remove(int(arr[1]))

    #append e: insert integer e at the end of the list
    elif arr[0] == "append":
        l.append(int(arr[1]))
    
    #sort the list
    elif arr[0] == "sort":
        l.sort()
    
    #pop : pop the last element from the list
    elif arr[0] == "pop":
        l.pop()
    
    #reverse: reverse the list
    else:
        l.reverse()
