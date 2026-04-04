# Problem 1
myList = [1,2,3,4,4]

# O(n2)
def algo1():
    for pointer1 in range(len(myList)):
        for pointer2 in range(pointer1+1, len(myList)):
            print(myList[pointer1],myList[pointer2])
            if myList[pointer1] == myList[pointer2]:
                print("Found em'")
# O(n long n)
def algo2():
    for pointer1 in range(len(myList)):
        for pointer2 in range(pointer1+1, len(myList)):
            if myList[pointer1] != myList[pointer2]:
                pointer2 = pointer2+1

# algo1()
# algo2()

# ------------------------------------------------------------------------------------------------------------

# Problem 2
# Given 2 arrays calculate the sum of each index at the same position in each array and add the last digit of the
# sum to a new array. For example:
    # a = [23,15,9]
    # b = [2,5,1]
    # output = [2,5,0,0]
    

listA = [3,5,9]
listB = [2,5,1]

def calculate_array_sum(listA, listB):
    output = []
    carry = 0
    i = len(listA) - 1
    j = len(listB) - 1
    
    while i >= 0 or j >= 0 or carry: # Process from right to left until we either reach the end of the array (i & j = -1) or carry is falsey
        val_a = listA[i] if i >= 0 else 0 # val_a is the value of index we're on in the array if the index were on is greater than or 0, otherwise it's 0 (if we go out of bounds)
        val_b = listB[j] if j >= 0 else 0 # val_b is the value of index we're on in the array if the index were on is greater than or 0, otherwise it's 0 (if we go out of bounds)

        total = val_a + val_b # Calculate the total first
        carry = total // 10  # Update carry

        if carry > 0: # If the carry is greater than 0, we need to add it to the value of the current index in listA before adding it to the value of the current index in listB
            val_c = val_a + carry
            total = val_c + val_a

        output.append(total % 10)  # Append ones digit

        i -= 1
        j -= 1
    
    output.reverse()  # Reverse to get correct order
    return output

# Test the function
print(calculate_array_sum(listA, listB))  # Should output [1, 5, 0, 0]

# ------------------------------------------------------------------------------------------------------------

