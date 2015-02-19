#Con complemento base 2
def decimalToBinaryB2(num):  
    assert -128 <= num < 128, "overflow"
    
    s = []
    num = (num + 256) % 256
    
    for i in range(8):
        s.append(num % 2)
        num /= 2
    
    for d in reversed(s):
        print d,
        
#Con complemento base 2
def binaryToDecimalB2(num): 
    assert 0 <= num <= 11111111, "Overflow" 
    ans = 0
    pwr = 0
    
    for i in range(7):
        ans += (num % 10) * 2**pwr
        pwr+=1
        num /=10
        
    if num % 10 == 1:
        ans -= 128

    return ans

#Sin complemento base 2
def binaryToDecimal(num): 
    assert 0 <= num <= 11111111, "Overflow" 
    ans = 0
    pwr = 0
    
    for i in range(8):
        ans += (num % 10) * 2**pwr
        pwr+=1
        num /=10

    return ans

#Sin complemento base 2
def decimalToBinary(num):
    ans = 0
    b = 1 
    assert 0 <= num <= 256, "Overflow"    
    while num > 0:
        if num % 2 == 1:
            ans += b
        b *= 10
        num /= 2 
    return ans

#Para enteros no negativos
def binaryToHexadecimal(num): 
    assert 0 <= num <= 11111111, "Overflow" 
    ans = ""
    conv = ["0" , "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    
    while num > 0:
        x = num % 10000
        ans =  conv[binaryToDecimal(x)] + ans
        num /= 10000
        
    print ans
    
#Para enteros no negativos
def hexadecimalToBinary(num): 
    m = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    ans = ""
    
    for i in range(len(num)-1, -1, -1):
        ans = str(decimalToBinary(m[num[i]])) + ans
        
    print ans 