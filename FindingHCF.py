

def hcf(a, b):
    divisor = min(a, b)
    dividend = max(a, b)

    while dividend%divisor != 0:
        temp = dividend
        dividend = divisor
        divisor = temp%divisor
    
    return divisor

HCF = hcf(10, 5)
print(HCF)