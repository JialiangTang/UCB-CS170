def digit_to_binary(digit):
    """Converts a single digit (or the number 10) in decimal form to binary.

    Args:
        digit (str): a single digit (or the number 10) in decimal form

    Returns:
        str: bitstring corresponding to the binary representation of the digit
    """
    conversion_table = {
        '0': '0',
        '1': '1',
        '2': '10',
        '3': '11',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111',
        '8': '1000',
        '9': '1001',
        '10': '1010',
    }
    return conversion_table[digit]
    
def add_binary(a, b):
    """Adds two binary numbers.

    Args:
        a (str): bitstring representing the first number to add
        b (str): bitstring representing the second number to add

    Returns:
        str: the sum of the two numbers in binary form

    >>> add_binary('101', '11')
    '1000'
    """
    if not (a and b):
        return a or b or '0'
    out = ''
    carry = '0'
    for d1, d2 in zip(a[::-1], b[::-1]):
        # case 1: 0 + 0
        if d1 == '0' and d2 == '0':
            out += carry
            carry = '0'
        # case 2: 1 + 1
        elif d1 == '1' and d2 == '1':
            out += carry
            carry = '1'
        # case 3: 0 + 1 or 1 + 0
        else:
            if carry == '0':
                out += '1'
            else:
                out += '0'

    remaining_bits = a[:-len(out)] or b[:-len(out)]
    if carry == '0':
        return remaining_bits + out[::-1]
    return (add_binary(remaining_bits, carry) + out[::-1]).lstrip('0') or '0'

def sub_binary(a, b):
    """Subtracts two binary numbers. Since we are dealing with unsigned 
    binary numbers, we assume that a >= b.

    Args:
        a (str): bitstring representing the first number to subtract
        b (str): bitstring representing the second number to subtract

    Returns:
        str: Returns the difference between the two numbers, a - b, 
            in binary form.

    >>> sub_binary('101', '11')
    '10'
    """
    if not b:
        return a or '0'
    assert int(a) >= int(b), 'a must be at least as large as b'
    out = ''
    for i in range(1, 1 + min(len(a), len(b))):
        # case 1: 0 - 0 or 1 - 1
        if a[-i] == b[-i]:
            out += '0'
        # case 2: 1 - 0
        elif a[-i] == '1' and b[-i] == '0':
            out += '1'
        # case 3: 0 - 1
        elif a[-i] == '0' and b[-i] == '1':
            out += '1'
            a = sub_binary(a, '1' + '0'*(i))

    remaining_bits = a[:-len(out)]
    return (remaining_bits + out[::-1]).lstrip('0') or '0'

def mul_binary(a, b):
    """Fast multiplication on two binary numbers using Karatsuba's 
        algorithm.

    Args:
        a (str): bitstring representing the first number to multiply
        b (str): bitstring representing the second number to multiply

    Returns:
        str: the product of the two numbers in binary form

    >>> mul_binary('101', '11')
    '1111'
    """
    n = max(len(a), len(b))
    x = '0'*(n-len(a)) + a
    y = '0'*(n-len(b)) + b
    
    if n == 1 and x == y == '1':
        return '1'
    elif n == 1:
        return '0'
    
    xlo = x[n//2:]
    xhi = x[:n//2]
    ylo = y[n//2:]
    yhi = y[:n//2]
    
    A = mul_binary(xhi, yhi)
    B = mul_binary(xlo, ylo)
    E = mul_binary(add_binary(xlo, xhi), add_binary(ylo, yhi))
    
    result = A + '0'*(2*len(xlo))
    result = add_binary(result, sub_binary(E, add_binary(A, B))+'0'*len(xlo))
    result = add_binary(result, B)
    
    return result.lstrip('0') or '0'

def decimal_to_binary(decimal):
    """
    args:
        decimal:string = decimal representation of a number, passed 
            as a string
    returns:
        A string representing the binary representation of the number
    """
    # print(decimal)
    if len(decimal) == 1 or decimal == '10':
        #print(digit_to_binary(decimal))
        return digit_to_binary(decimal)
    if decimal == '100':
        return '1100100'
    n = len(decimal)

    n1 = decimal[:n//2] #higher
    n2 = decimal[n//2:] #lower
    if n%2==0:
        const = str(10**(n//2))
    else:
        const = str(10**(n//2+1))
    n1_b = decimal_to_binary(n1)
    # print(const)
    const_b = decimal_to_binary(const)
    n2_b = decimal_to_binary(n2)
    # print(n1_b)

    hi_b = mul_binary(n1_b, const_b)
    lo_b = n2_b
    #print(hi_b)
    #print(lo_b)
    res = add_binary(hi_b, lo_b)
    #print(res)
    return res

#decimal_to_binary('10')
#decimal_to_binary('100')
print(decimal_to_binary('256'))
print(decimal_to_binary('53'))
print(decimal_to_binary('7798'))
print(decimal_to_binary('1'))
print(decimal_to_binary('45'))
print(decimal_to_binary('671'))
print(decimal_to_binary('17'))