class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.top = -1
        

    def push(self,a) -> None :
        if type(a) == str:
            self.stack.extend(a)
            self.top += len(a)
        else:
            self.stack.append(a)
            self.top += 1
        
    def pop(self) -> None :
        if self.stack == []:
            print("Stack Underflow.")
        else:
            self.top -= 1
            return self.stack.pop()

    def peek(self) :
        if self.stack == [] :
            print('Stack Underflow.')
        else:
            return self.stack[self.top]

class Main : 
    def reverseStrUsingStack(s : str):
        
        try:
            st = Stack()
            st.push(s)

            s = ''

            while st.top != -1:
                s += st.pop()

            return s
        except TypeError as e:
            return 'Pass only string argument.'
    
    def decimalToNumberSystem(d : int,n : int):
        try:
            st = Stack()
            while d > 0:
                st.push(d%n)
                d //= n
            d = 0
            while st.top != -1:
                d += int(st.pop())*10**(st.top + 1)
            return d
        except TypeError as e:
            return 'Pass only integer argument.'
       
