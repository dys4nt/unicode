
text = open("./context.enc","rb").read()

n = len(text)
i = 0

res = ""
while i < n-4:
    b1 = text[i]
    b2 = text[i+1]
    b3 = text[i+2]
    b4 = text[i+3]
    num = (((b1 << 4) % 256) // 16) * (2**12) + (((b2<<2) % 256)//4) * (2**6) + (((b3 << 2) % 256)//4)
    if b1 & 2**7 and b1 & 2**6 and b1 & 2**5 and not b1 & 2**4 and b2 & 2**7 and not b2 & 2**6 and b3 & 2**7 and not b3 & 2**6 and num>=0xac00 and num<=0xd7a3:

        res += chr(num)
        i += 3
        
    else:
        if b2*256+b1>=0xac00 and b2*256+b1<=0xd7a3:
            if b3 == 0 and b4 == 0:
                res += chr(b2*256+b1)
                i += 4
            else:
                i += 2
        elif b3 == 0 and b4 == 0:
            res += chr(b2*256+b1)
            i += 4
        elif b2 == 0:
            res += chr(b1)
            i += 2
        else:
            res += chr(b1)
            i += 1

print(res)