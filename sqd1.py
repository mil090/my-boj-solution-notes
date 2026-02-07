# 스택, 큐, 덱 1
# 28278번: 스택 2
# 문제
'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 다섯 가지이다.
1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
3: 스택에 들어있는 정수의 개수를 출력한다.
4: 스택이 비어있으면 1, 아니면 0을 출력한다.
5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
'''
# 입력
'''
첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)
둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.
출력을 요구하는 명령은 하나 이상 주어진다.
'''
# 출력
'''
출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.
'''
# 해법
'''
각각의 연산은 1-push, 2-pop, 3-size, 4-is_empty, 5-peek
1. push 연산 구현
2. pop 연산 구현
3. size 연산 구현
4. is_empty 연산 구현
5. peek 연산 구현
6. 스택 객체 stack1을 생성
7. N을 입력받음
8. N개의 줄에 걸쳐 명령을 입력받음. 이때 명령이 1일 때만 추가 요소 e가 발생. 이를
try-except로 구분해 보자
try에서 command, element=map(int, sys.stdin.readline().split())를 실행
만약 여기서 오류가 발생하지 않는다면 command는 1(즉 push 연산)이고, 상단에 추가할
원소는 element이므로 stack1.push(element)를 실행
만약 command와 element를 입력받는 과정에서 오류가 발생한다면, 이는 push 연산이
아니므로 element가 없음. 따라서 command만을 입력받아 알맞은 연산을 수행
'''
import sys
class Stack:
    def __init__(self):
        self.s=[]
    def push(self, e):
        self.s.append(e)
    def is_empty(self):
        if len(self.s)==0:
            return 1
        else:
            return 0
    def pop(self):
        if self.is_empty()==0:
            result=self.s.pop()
            return result
        else:
            return -1
    def size(self):
        return len(self.s)
    def peek(self):
        if self.is_empty()==0:
            return self.s[-1]
        else:
            return -1
stack1=Stack()
commands={1: stack1.push, 2: stack1.pop, 3: stack1.size, 
          4: stack1.is_empty, 5: stack1.peek}
N=int(sys.stdin.readline())
result=[]
for _ in range(N):
    C=list(map(int, sys.stdin.readline().split()))
    if C[0]==1:
        commands[C[0]](C[1])
    else:
        result.append(str(commands[C[0]]()))
print('\n'.join(result))
