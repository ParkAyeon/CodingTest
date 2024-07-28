#백준 10828번 (스택1)
import sys

stack = [] #stack 초기화

#반복문으로 여러줄을 입력받을 때 사용
n = int(sys.stdin.readline()) #(\n)이 같이 저장되기 때문에 형변환 필요

for i in range(n):
    cm = sys.stdin.readline().split()

    #1. push X: 정수 X를 스택에 넣는 연산이다.
    if cm[0] == "push":
        stack.append(cm[1])

    #2. pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
    # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif cm[0] == "pop":
        print(stack.pop() if stack else -1)
    
    #3. size: 스택에 들어있는 정수의 개수를 출력한다.
    elif cm[0] == "size":
        print(len(stack))
    
    #4. empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif cm[0] == "empty":
        print(1 if not stack else 0) #if not List는 List가 비어있는지 확인하는 문법
    
    #5. top: 스택의 가장 위에 있는 정수를 출력한다. 
    # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif cm[0] == "top":
        print(stack[-1] if stack else -1)
