


# def leftequalright(arr):
    
#     leftsum = 0
#     rightsum = 0
#     for n in range(len(arr)):

#         leftarr = arr[:n]
#         rightarr = arr[n+1:]

#         for i in range(len(leftarr)):
#             leftsum = leftarr[i] + leftsum

#         for j in range(len(rightarr)):
#             rightsum = rightarr[j] + rightsum

#         if leftsum == rightsum:
#             return n
        
#     return 0


# listx = [2, 2, 4, 2, 2]
# print(leftequalright(listx))

#This is a better way to do things, since the time complexity becomes O(n)
class Solution:
    def equilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(len(arr)):
            # Right sum is total_sum minus left_sum minus the current element
            right_sum = total_sum - left_sum - arr[i]
            
            if left_sum == right_sum:
                return True  # Return the index
            
            # Update left_sum to include the current element
            left_sum += arr[i]
        
        return 0  # Return -1 if no equilibrium index is found

# Example usage
sol = Solution()
arr = [1, 3, 5, 2, 2]
print(sol.equilibrium(arr))  # Output: 2
