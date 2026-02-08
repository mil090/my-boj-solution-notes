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

# 10773번: 제로
# 문제
'''
나코더 기장 재민이는 동아리 회식을 준비하기 위해서 장부를 관리하는 중이다.
재현이는 재민이를 도와서 돈을 관리하는 중인데, 애석하게도 항상 정신없는 재현이는 돈을 
실수로 잘못 부르는 사고를 치기 일쑤였다.
재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!
'''
# 입력
'''
첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 
정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
'''
# 출력
'''
재민이가 최종적으로 적어 낸 수의 합을 출력한다. 최종적으로 적어낸 수의 합은 231-1보다 
작거나 같은 정수이다.
'''
# 해법
'''
1. K를 입력받음. 현재 적은 수를 저장할 스택 numbers를 빈 리스트로 생성
2. K개의 줄에 걸쳐 숫자 n을 입력받음
3. n이 0이면 pop, 0이 아니면 append 연산을 실행
4. 반복문이 종료되면 sum(numbers)를 출력
'''
import sys
K=int(sys.stdin.readline())
numbers=[]
for _ in range(K):
    n=int(sys.stdin.readline())
    if n==0:
        r=numbers.pop()
    else:
        numbers.append(n)
print(sum(numbers))

# 9012번: 괄호
# 문제
'''
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 '(' 와 ')' 만으로 
구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 
문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 
VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 
"(x)"도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 
문자열 xy도 VPS 가 된다. 예를 들어 "(())()"와 "((()))" 는 VPS 이지만 "(()(", 
"(())()))" , 그리고 "(()" 는 모두 VPS 가 아닌 문자열이다. 
여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 
NO 로 나타내어야 한다. 
'''
# 입력
'''
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 
번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 
줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 
'''
# 출력
'''
출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 
“YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 
'''
# 해법
'''
1. T를 입력받음
2. T개의 줄에 걸쳐 괄호 문자열 brackets를 입력받음
3. 괄호 검사 함수 is_valid_bracket(b)를 구현. b는 (, )로 구성된 문자열
스택으로 사용할 빈 리스트 stack을 생성
b의 각 문자 s에 대하여 s가 (이면 stack에 '('를 삽입
s가 )이면 stack의 맨 마지막 '('를 삭제. 만약 )를 만났는데 stack이 비어 있다면
VPS가 아니므로 NO를 반환
모든 s에 대하여 위 연산을 실행한 후 stack이 공백 상태가 아니면 VPS가 아니므로 NO를
반환하고, 공백 상태이면 VPS이므로 YES를 반환
4. 각 반복문에서 is_valid_bracket(brackets)를 출력
'''
import sys
def is_valid_bracket(b: str):
    stack=[]
    for s in b:
        if s=='(':
            stack.append(s)
        elif len(stack)==0:
            return False
        else:
            r=stack.pop()
    if len(stack)!=0:
        return False
    else:
        return True
T=int(sys.stdin.readline())
result=[]
for _ in range(T):
    brackets=sys.stdin.readline().strip()
    if is_valid_bracket(brackets):
        result.append('YES')
    else:
        result.append('NO')
print('\n'.join(result))

# 4949번: 균형잡힌 세상
# 문제
'''
세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.
정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 
프로그램을 짜는 것이다.
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 
이루는 조건은 아래와 같다.
모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.
'''
# 입력
'''
각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 
이루어져 있으며, 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.
입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.
'''
# 출력
'''
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
'''
# 해법
'''
앞 문제(9012번-괄호)의 두 조건에서 새로운 조건 한 가지가 추가됨
서로 다른 종류의 괄호가 교차하면 안 됨. 즉 닫는 괄호를 만났을 때, stack의 마지막에
있는 여는 괄호가 이 닫는 괄호와 같은 종류이어야 함
1. 입력받은 문자열에 대한 괄호 검사를 수행하는 is_valid(S)를 구현
스택으로 사용할 빈 리스트 stack을 생성
S의 각 원소 s에 대하여 s가 여는 괄호 ( 또는 [이면 이를 stack에 삽입
s가 닫는 괄호 ) 또는 ]이면 유효성 검사를 진행
만약 stack이 공백 상태이면 여는 괄호 없이 닫는 괄호가 나온 것이므로 False를 반환
만약 stack의 맨 마지막 원소가 닫는 괄호와 맞지 않으면 다른 종류의 괄호 쌍이 교차한
것이므로 False를 반환
stack의 맨 마지막 원소가 닫는 괄호와 맞으면 해당 여는 괄호(마지막 원소)를 stack에서 제거
위 반복문이 종료되었을 때 stack이 공백 상태가 아니라면 여는 괄호와 닫는 괄호의 수가
서로 다른 것이므로 False를 반환
위 조건을 모두 통과하면 True를 반환
결과를 저장할 빈 리스트 result를 생성
2. while True로 무한 루프를 생성
3. 검사할 문자열 sen을 입력받음
4. sen이 .이면 반복문을 탈출
5. 우리가 관심 있는 영역은 괄호뿐이므로, 입력받은 문자열에서 괄호만 남김
6. 괄호 검사 함수 is_valid(sen)을 실행하여 True이면 yes, False이면 no를 result
에 삽입
7. result의 원소들을 한 줄에 하나씩 출력
'''
import sys
def is_valid(S: str):
    stack=[]
    for s in S:
        if s in ('(', '['):
            stack.append(s)
        elif s==')':
            if len(stack)==0:
                return False
            elif stack[-1]!='(':
                return False
            else:
                r=stack.pop()
        elif s==']':
            if len(stack)==0:
                return False
            elif stack[-1]!='[':
                return False
            else:
                r=stack.pop()
    if len(stack)!=0:
        return False
    else:
        return True
targets='()[]'
result=[]
while True:
    sen=sys.stdin.readline().rstrip('\n')
    if sen=='.':
        break
    brackets=''.join([char for char in sen if char in targets])
    if is_valid(brackets):
        result.append('yes')
    else:
        result.append('no')
print('\n'.join(result))
