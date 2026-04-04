class Solution:
    
    # Problem 1
    my_list = [1,2,3,4,4]

    # O(n2)
    def algo1(my_list: list[int]) -> list[int]:
        for pointer1 in range(len(my_list)):
            for pointer2 in range(pointer1+1, len(my_list)):
                print(my_list[pointer1],my_list[pointer2])
                if my_list[pointer1] == my_list[pointer2]:
                    print("Found em'")

    # algo1()

    # ------------------------------------------------------------------------------------------------------------

    # Problem 2
    # Given 2 arrays calculate the sum of each index at the same position in each array and add the last digit of the
    # sum to a new array. For example:
        # a = [23,15,9]
        # b = [2,5,1]
        # output = [2,5,0,0]


    list_a = [3,5,9]
    list_b = [2,5,1]

    def calculate_array_sum(self, list_a, list_b):
        output = []
        carry = 0
        i = len(list_a) - 1
        j = len(list_b) - 1

        while i >= 0 or j >= 0 or carry: # Process from right to left until we either reach the end of the array (i & j = -1) or carry is falsey
            val_a = list_a[i] if i >= 0 else 0 # val_a is the value of index we're on in the array if the index were on is greater than or 0, otherwise it's 0 (if we go out of bounds)
            val_b = list_b[j] if j >= 0 else 0 # val_b is the value of index we're on in the array if the index were on is greater than or 0, otherwise it's 0 (if we go out of bounds)

            if carry > 0 and i < 0:
                output.append(carry)
                output.reverse()# If carry exists and val_b exists but val_a is 0, we can just append the carry to the output (e.g. carry=1, val_b=5, val_a=0 becomes 15, so we can just append the carry of 1 to the output)
                return output

            val_a = carry * 10 + val_a if carry > 0 else val_a # If carry exists, prepend it to val_a (e.g. carry=1, val_a=5 becomes 15)
            total = val_a + val_b # Calculate the total
            carry = total // 10  # Update carry for the next iteration

            output.append(total % 10)  # Append ones digit

            i -= 1
            j -= 1

        output.reverse()  # Reverse to get correct order
        return output

    # ------------------------------------------------------------------------------------------------------------

    # Problem 3: Contains Duplicate
    # Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

    # Input: nums = [1, 2, 3, 3]
    # Output: true

    # Input: nums = [1, 2, 3, 4]
    # Output: false

    def has_duplicates(self) -> bool:
        nums = [1, 2, 3, 3]
        hashset = set()

        for i in range(len(nums)):
            if nums[i] in hashset:
                print(f"Found duplicate: {nums[i]}")
                return True
            else:
                hashset.add(nums[i])

        print("No duplicates ")
        return False

    # Using a hashset is the optimal data structure because it has a O(1) lookup, vs an array O(n)
    # Sorting the array would have been another solution but that is O(n log n), slower.


solution = Solution()
solution.has_duplicates()