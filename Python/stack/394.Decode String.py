'''
Method - Stack
Steps:
    1. set a empty stack, empty str(A), 0 digit(D)
    2. traverse the str(i)
        if i is digit, D = i + D * 10
        if i is '[', append D into stack and then D = 0
        if i is Alpa, A += i
        if i is ']', pop D and String from stack, append (D * A + String) into stack

'''


def decodeString(s) -> str:

    if s == '':
        return ''
    
    stack = []
    A = ''
    D = 0
    
    for i in s:
        if i.isdigit():
            D = int(i) + 10 * D
        elif i == '[':
            stack.append(D)
            stack.append(A)
            D = 0
            A = ''
        elif i.isalpha():
            A += i
        elif i == ']':
            preA = stack.pop()
            num = stack.pop()
            A = preA + num * A
        print(stack)
    return A
                
res = decodeString('2[abc]3[cd]ef')
print(res)