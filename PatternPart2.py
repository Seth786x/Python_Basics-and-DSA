
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

n=5
for i in range(n):
    for j in range(n-1-i):
        print(" ", end = " ");

    for j in range(2*i+1):
        print("*", end=" ")
    
    print()

print("-----------------------------------------------------------")

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
n=5
for i in range(n):
    for j in range(i):
        print(" ", end = " ");

    for j in range(2*(n-1-i)+1):
        print("*", end=" ")
    
    print()

print("----------------------------------------------------------")

