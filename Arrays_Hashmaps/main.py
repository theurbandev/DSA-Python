class Solution:
    
    # Problem 1
    # O(n2)

    def algo1(self) -> list[int]:
        my_list = [1, 2, 3, 4, 4]
        for pointer1 in range(len(my_list)):
            for pointer2 in range(pointer1+1, len(my_list)):
                print(my_list[pointer1],my_list[pointer2])
                if my_list[pointer1] == my_list[pointer2]:
                    print("Found em'")
                    return [my_list[pointer1], my_list[pointer2]]

    # ------------------------------------------------------------------------------------------------------------

    # Problem 2
    # Given 2 arrays calculate the sum of each index at the same position in each array and add the last digit of the
    # sum to a new array. For example:
        # a = [23,15,9]
        # b = [2,5,1]
        # output = [2,5,0,0]

    def calculate_array_sum(self):
        list_a = [3, 5, 9]
        list_b = [2, 5, 1]

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

    # Explanation:
    # Using a hashset is the optimal data structure because it has a O(1) lookup, vs an array O(n)
    # Sorting the array would have been another solution but that is O(n log n), slower.

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

    # ------------------------------------------------------------------------------------------------------------

    # Problem 4: Valid Anagram
    # Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
    # An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

    # Examples:
        # Input: s = "racecar", t = "carrace"
        # Output: true

        #Input: s = "jar", t = "jam"
        # Output: false

    # Explanation:
    # hashmap: {"r":2, "a": 2} adding one string to a map ( O(n) for insert and O(1) for lookup )
    # return False early if the two strings have different lengths
    # loop through the first string and update the map with the number of instances of the character ( O(n) for the iteration )
    # loop through the second string and check:
        # is the char in the map ? decrement : return False
    # if we get through that second loop, return True
    # overall O(n)

    def isAnagram(self):
        s = "racecar"
        t = "carrace"

        map = {}

        if len(s) != len(t):
            return False

        for s_chars in s:
           if s_chars in map:
               map[s_chars] += 1
           else:
               map[s_chars] = 1

        for t_chars in t:
            if t_chars in map:
                map[t_chars] -= 1
            else:
                return False

        return True



solution = Solution()
solution.has_duplicates()