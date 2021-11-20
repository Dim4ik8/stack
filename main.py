class Stack:
    elements = []

    def __init__(self):
        self.elements = []

    def is_empty(self):
        if len(self.elements):
            return True
        else:
            return False

    def push(self, element):
        self.elements.insert(0, element)

    def pop(self):
        self.elements.remove(self.peek())
        return self.elements

    def peek(self):
        return self.elements[0]

    def size(self):
        return len(self.elements)


class BracketsStack(Stack):
    opening_brackets = '[{('
    closing_brackets = ']})'

    def __init__(self, sequence: str):
        for bracket in sequence:
            self.push(bracket)
        if self.is_balanced():
            print('OK\t|\tСтрока сбалансирована.')
        else:
            print('WARNING\t|\tСтрока не сбалансирована!')

    def peek_is_opening(self):

        if self.peek() in self.opening_brackets:
            return True
        else:
            return False

    def peek_is_equal(self, element):

        if element == ']' and self.peek() == '[':
            return True
        elif element == '}' and self.peek() == '{':
            return True
        elif element == ')' and self.peek() == '(':
            return True
        else:
            return False

    def push(self, element):

        if element in self.opening_brackets:
            super().push(element)
        elif element not in self.opening_brackets and element not in self.closing_brackets:
            pass
        elif element in self.closing_brackets:
            if self.peek_is_opening() and self.peek_is_equal(element):
                super().pop()

    def is_balanced(self):
        if self.size():
            return False
        else:
            return True


stack = Stack()

stack.push('2')
stack.push('3')
stack.push('4')
stack.push('abc')
print(stack.elements)
stack.pop()
print(stack.elements)

bracket_stack = BracketsStack('({[([[{}]]))')
print(bracket_stack.size())
