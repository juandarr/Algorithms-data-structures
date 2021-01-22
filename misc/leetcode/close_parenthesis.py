'''
A raw, draft solution to the problem of determining whether a string composed by two or more of the characters '([{}])'
always closes the brackets once an open bracked has been added to the sequence (must be same kind) 
Author: Juan Rios
'''
class Solution:
    def isValid(self, s: str) -> bool:
        state = []
        for i in s:
            if i=='(':
                state.append(1)
            elif i=='[':
                state.append(2)
            elif i=='{':
                state.append(3)
            elif i==')':
                if state!=[]:
                    if state[-1]!=1:
                        return False
                else:
                    return False
                state.pop()
            elif i==']':
                if state!=[]:
                    if state[-1]!=2:
                        return False
                else:
                    return False
                state.pop()
            elif i=='}':
                if state!=[]:
                    if state[-1]!=3:
                        return False
                else:
                    return False
                state.pop()
        if state!=[]:
            return False    
        return True

if __name__='__main__':
    tests = ['(((]]', '[]', '(]', '(([{}]))']
    expected = [False, True, False, True]
    solver = Solution()
    for idx, test in enumerate(tests):
        if solver.isValid(test)==expected[idx]:
            print("Solution {0} is {1}".format()) 

