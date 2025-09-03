def parenthesis(s):
    brackets = {']':'[','}':'{',')':'('}
    stack = []
    for ch in s:
        if ch in '{[(':
            stack.append(ch)
        elif ch in '}])':
            if not stack or brackets[ch]!=stack[-1] :
                return False
            stack.pop()
            
    return len(stack)==0
    
s = input("Enter the string: ")
print(parenthesis(s))