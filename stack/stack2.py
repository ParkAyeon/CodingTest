#백준 28278번 (스택2)
import sys

stack = [] #stack 초기화

#반복문으로 여러줄을 입력받을 때 사용
n = int(sys.stdin.readline()) #(\n)이 같이 저장되기 때문에 형변환 필요

for i in range(n):
    cm = list(map(int, sys.stdin.readline().split()))

    #1. 정수 x를 stack에 넣는다
    if cm[0] == 1:
        stack.append(cm[1])

    #2. 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다
    elif cm[0] == 2:
        print(stack.pop() if stack else -1)
    
    #3. 스택에 들어있는 정수의 개수를 출력한다
    elif cm[0] == 3:
        print(len(stack))
    
    #4. 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif cm[0] == 4:
        print(1 if not stack else 0)
    
    #5. 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif cm[0] == 5:
        print(stack[-1] if stack else -1)
