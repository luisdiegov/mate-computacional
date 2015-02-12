def decToBin(num):
    assert -128 <= num < 128, "overflow"
    
    s = []
    num = (num + 256) % 256
    
    for i in range(8):
        s.append(num % 2)
        num /= 2
    
    for d in reversed(s):
        print d,