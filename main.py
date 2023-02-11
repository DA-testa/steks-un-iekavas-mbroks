# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i))
            # Process opening bracket, write your code here
            
            #pass

        if next in ")]}":
            # Process closing bracket, write your code here

            #brac = opening_brackets_stack.pop()
            #print(brac)
            #u = are_matching(Bracket(next,i),opening_brackets_stack.pop())
            #print(u)
            if len(opening_brackets_stack)==0 and i==0:
                return i+1

            else:
                brac = opening_brackets_stack.pop()
     
                if are_matching(brac.char,Bracket(next,i).char):
                    break
                else:
                    return i+1
    if len(opening_brackets_stack)!=0:
        return opening_brackets_stack.pop().position + 1

    return 0

def main():
    mode = input()
    if mode[0]=="I":
        text=input()
    elif mode[0]=="F":
        text=input()

    mismatch = find_mismatch(text)
    # Printing answer, write your code here

    if len(text)==1:
        print(1)
    elif mismatch ==0:
        print("Success")
    else:
        print(mismatch)


    #print(text)

if __name__ == "__main__":
    main()
