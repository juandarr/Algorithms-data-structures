def isBalanced(s):
    inB = {'(': True, '[': True, '{':True}
    outB = {')':'(', ']':'[', '}':'{'}
    brackets = []
    for st in s:
        if st in inB:
            brackets.append(st)
        elif st in outB:
            if brackets==[]:
                return 'NO'
            if outB[st]==brackets[-1]:
                brackets.pop()
            else:
                return 'NO'
    if brackets == []:
        return 'YES'
    else:
        return 'NO'

s_ar = ['{[()]}', '{[(])}', '{{[[(())]]}}']
for s in s_ar:
    print(isBalanced(s))
