#This is the basic logic that we may go with 
#but it has several constraint issues, like it cannot handle negative numbers ""
# x = 87654;
# y = list(str(x));

# for i in range(len(y)//2):
#     xyz = y[i]
#     y[i] = y[len(y)-i-1]
#     y[len(y)-i-1] = xyz

# reverseofY = "".join(y)
# print("The reversed number is ", reverseofY)

#The best way to do it is below

class Solution(object):
    def reverse(self, x):
        
        is_neg = x<0
        x = abs(x)

        ans = 0

        while x>0:
            ans = ans*10+x%10
            x = x//10

        if is_neg:
            ans = -ans

        if ans<-2**31 or ans>(2**31-1):
            return 0

        return ans        

        
        





