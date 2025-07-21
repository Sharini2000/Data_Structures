class StackImplementation:
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
        
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else: 
            return -1
    
    def isEmpty(self):
        return len(self.stack) == 0

st = StackImplementation()


while True:
    ele = input("Enter the operation you want to perform:\n1. Push\n2. Pop\n3. Peek\n4.Display\n5. Exit\n")

    if ele == "Push" or ele == "1":
        value = int(input("Enter the value to push: "))
        st.push(value)
        print(f"Pushed {value} onto the stack.")

    elif ele == "Pop" or ele == "2":
        result = st.pop()
        if result == -1:
            print("Stack is empty. Cannot pop.")
        else:
            print(f"Popped value: {result}")

    elif ele == "Peek" or ele == "3":
        result = st.peek()
        if result == -1:
            print("Stack is empty.")
        else:
            print(f"Top of stack: {result}")
    elif ele == "Display" or ele == "4":
        if st.isEmpty():
            print("Stack is empty")
        else:  
            for elements in st.stack:
                print(str(elements) +"\n")

    elif ele == "Exit" or ele == "5":
        print("Exiting...")
        break

    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")
