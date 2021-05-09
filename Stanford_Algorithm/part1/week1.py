num1 = "3141592653589793238462643383279502884197169399375105820974944592"
num2 = "2718281828459045235360287471352662497757247093699959574966967627"

from itertools import zip_longest


def add(a, b):
    out = []
    arra = [int(c) for c in a]
    arrb = [int(c) for c in b]
    carry = 0
    for ca, cb in zip_longest(reversed(arra), reversed(arrb), fillvalue=0):
        carry, digit = divmod(ca + cb + carry, 10)
        out.append(str(digit))
    if carry == 1:
        out.append(str(1))
    return "".join(reversed(out)).lstrip("0")

def isSmaller(a, b):
    if len(a) < len(b):
        return True
    if len(a) > len(b):
        return False
    for i in range(len(a)):
        if a[i] < b[i]:
            return True
        elif a[i] > b[i]:
            return False
    return False

def sub(a, b):
    maxlen = max(len(a),len(b))
    a = leftPad(a,maxlen)
    b = leftPad(b,maxlen)
    res = ""
    lessThan0 = False
    if isSmaller(a, b):
        tmp = a
        a = b
        b = tmp
        lessThan0 = True
        
    a = a[::-1]
    b = b[::-1]
    carry = 0
    for i in range(len(b)):
        sub = ((ord(a[i])-ord('0'))-(ord(b[i])-ord('0')) - carry)
        if sub < 0:
            sub = sub + 10
            carry = 1
        else:
            carry = 0
        res += str(sub)
    for i in range(len(b), len(a)):
        sub = ((ord(a[i])-ord('0')) - carry)
        if sub < 0:
            sub += 10
            carry = 1
        else:
            carry = 0
        res += str(sub)
    res = res[::-1]
    if lessThan0:
        res = "-" + res
    return res

def leftPad(num, maxlen):
    addZero = ""
    if len(num) < maxlen:
        addZero = "0"*(maxlen-len(num))
    return addZero + num

def rightPad(num, n):
    if n <= 0:
        return num
    addZero = "0"*n
    return num + addZero

def kara(num1, num2):
    if num1[0] == "-":
        return "-" + kara("-"+num1,num2)
    if num2[0] == "-":
        return "-" + kara(num1, "-"+num2)

    if len(num1) < 3 or len(num2) < 3:
        if int(num1) < 10 or int(num2) < 10:
            return str(int(num1) * int(num2))
    maxlen = max(len(num1), len(num2))

    # left padding with 0
    num1 = leftPad(num1, maxlen)
    num2 = leftPad(num2, maxlen)

    mid = maxlen // 2
    hi1, lo1 = num1[:-mid], num1[-mid:]
    hi2, lo2 = num2[:-mid], num2[-mid:]
    z0, z2 = kara(lo1, lo2), kara(hi1, hi2)
    z1 = kara(add(lo1,hi1), add(lo2,hi2))
    
    left = rightPad(z2, 2*mid)
    right = sub(z1,z2)
    right = sub(right,z0)
    right = rightPad(right, mid)
    res = add(left,right)
    res = add(res,z0)

    return res


def main():
    print(kara(num1,num2))

if __name__ == "__main__":
    main()
