def balance_parens(param):
    direction = -1
    balanced = []
    splitStr = [i for i in param]

    open = 0
    close = 0

    for i in splitStr:
        if(i == ')'):
            close += 1
        elif(i == '('):
            open += 1

    print(open, close)

    for i in range(0, len(splitStr)):
        if(direction == -1):
            if(splitStr[i] != ')'):
                if(splitStr[i] == '('):
                    balanced.append(splitStr[i])
                    direction = 1
                else:
                    balanced.append(splitStr[i])
        else:
            if(splitStr[i] == ')'):
                balanced.append(splitStr[i])
                direction = -1
            else:
                balanced.append(splitStr[i])

    return ''.join(balanced)

print(balance_parens("abc(d)e(fgh))(i)j)k"))
print(balance_parens("abc((d)e(fgh)(i)j(k"))
print(balance_parens("abc(d)(ef(g(h))ij)k)lm()o)p"))