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

# 12789번: 도키도키 간식드리미
# 문제
'''
인하대학교 학생회에서는 중간, 기말고사 때마다 시험 공부에 지친 학우들을 위해 간식을 
나눠주는 간식 드리미 행사를 실시한다. 승환이는 시험 기간이 될 때마다 간식을 받을 생각에 
두근두근 설레서 시험 공부에 집중을 못 한다. 이번 중간고사에서도 역시 승환이는 설레는 
가슴을 안고 간식을 받기 위해 미리 공지된 장소에 시간 맞춰 도착했다. 그런데 이게 무슨 
날벼락인가! 그 곳에는 이미 모든 학생들이 모여있었고, 승환이는 마지막 번호표를 받게 
되었다. 설상가상으로 몇몇 양심에 털이 난 학생들이 새치기를 거듭한 끝에 대기열의 순서마저 
엉망이 되고 말았다. 간식을 나눠주고 있던 인규는 학우들의 터져 나오는 불만에 번호표 
순서로만 간식을 줄 수 있다고 말했다. 
그제야 학생들이 순서대로 줄을 서려고 했지만 공간이 너무 협소해서 마음대로 이동할 수 
없었다. 다행히도 대기열의 왼쪽에는 1열로 설 수 있는 공간이 존재하여 이 공간을 잘 
이용하면 모두가 순서대로 간식을 받을 수 있을지도 모른다. 자칫 간식을 못 받게 될지도 
모른다는 위기감을 느낀 승환이는 자신의 컴퓨터 알고리즘적 지식을 활용해 과연 모든 사람들이 
순서대로 간식을 받을 수 있는지 확인하는 프로그램을 만들기로 했다. 만약 불가능 하다면 
승환이는 이번 중간고사를 망치게 될 것 이고 가능하다면 힘을 얻어 중간고사를 잘 볼 수 
있을지도 모른다.
사람들은 현재 1열로 줄을 서있고, 맨 앞의 사람만 이동이 가능하다. 인규는 번호표 
순서대로만 통과할 수 있는 라인을 만들어 두었다. 이 라인과 대기열의 맨 앞 사람 사이에는 
한 사람씩 1열이 들어갈 수 있는 공간이 있다. 현재 대기열의 사람들은 이 공간으로 올 수 
있지만 반대는 불가능하다. 승환이를 도와 프로그램을 완성하라.
현재 간식 배부 공간을 그림으로 나타내면 다음과 같다.
(그림 생략)
위 예제는 다음 그림과 같이 움직였을 때 모두가 순서대로 간식을 받을 수 있다..
(그림 생략)
'''
# 입력
'''
입력의 첫째 줄에는 현재 승환이의 앞에 서 있는 학생들의 수 N(1 ≤ N ≤ 1,000,자연수)이 
주어진다. 다음 줄에는 승환이 앞에 서있는 모든 학생들의 번호표(1,2,...,N) 순서가 
앞에서부터 뒤 순서로 주어진다.
'''
# 출력
'''
승환이가 무사히 간식을 받을 수 있으면 "Nice"(따옴표는 제외)를 출력하고 그렇지 않다면 
"Sad"(따옴표는 제외)를 출력한다.
'''
# 해법
'''
현재 서 있는 줄이 간식을 모두 나눠줄 수 있는지 검사하는 함수 is_valid(line)을 구현
1. 왼쪽에 있는 '한 명씩만 설 수 있는 공간'을 빈 리스트(스택) stay로 생성
2. 승환이의 앞에 서 있는 사람의 수 N은 line의 길이와 같음
3. 현재 번호표 순서를 cur로 지정
4. 만약 cur이 line에 있다면, 해당 번호가 가장 앞으로 올 때까지 그 앞에 있는 번호들을
stay로 이동한 후 line에서 cur을 삭제
5. 만약 cur이 stay에 있다면, stay의 최상단 원소(맨 마지막 원소)와 cur을 비교.
만약 cur이 stay의 최상단 원소가 아니라면 더 이상 간식을 나눠줄 수 없으므로 False를 반환
cur이 stay의 최상단 요소라면 stay에서 cur을 삭제
6. 위 과정이 N번의 반복문 동안 모두 실행되었다면 간식을 모두 나눠준 것이므로 True를 반환
7. N을 입력받음
8. 현재 서 있는 순서를 리스트 L로 입력받음
9. is_valid(order)가 True이면 'Nice', False이면 'Sad'를 출력
'''
def is_valid(line: list[int]):
    stay=[]
    N=len(line)
    for cur in range(1, N+1):
        if cur in line:
            while line[0]!=cur:
                stay.append(line.pop(0))
            r=line.pop(0)
        elif stay[-1]!=cur:
            return False
        else:
            r=stay.pop()
    return True
N=int(input())
L=list(map(int, input().split()))
if is_valid(L):
    print('Nice')
else:
    print('Sad')

# 18258번: 큐 2
# 문제
'''
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 여섯 가지이다.
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
# 입력
'''
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 
줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 
같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
'''
# 출력
'''
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''
# 해법
'''
push를 제외한 모든 명령어는 반환값이 존재
1. 각 명령어에 대응하는 함수를 구현
2. N을 입력받음
3. N개의 줄에 걸쳐 명령어를 입력받고 실행
'''
class Q:
    def __init__(self):
        self.q=[]
    def push(self, e):
        self.q.append(e)
    def pop(self):
        if self.empty()!=1:
            result=self.q.pop(0)
            return result
        else:
            return -1
    def size(self):
        return len(self.q)
    def empty(self):
        if len(self.q)==0:
            return 1
        else:
            return 0
    def front(self):
        if self.empty()!=1:
            return self.q[0]
        else:
            return -1
    def back(self):
        if self.empty()!=1:
            return self.q[-1]
        else:
            return -1
queue1=Q()
commands={'push': queue1.push, 'pop': queue1.pop, 'size': queue1.size,
          'empty': queue1.empty, 'front': queue1.front, 'back': queue1.back}
import sys
N=int(sys.stdin.readline())
result=[]
for _ in range(N):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='push':
        commands[cmd[0]](cmd[1])
    else:
        result.append(str(commands[cmd[0]]()))
print('\n'.join(result))
# 시간 초과 발생
'''
각 함수를 따로 만드는 수밖에 없다
'''
import sys
queue=[]
def push(e):
    queue.append(e)
def empty():
    if len(queue)==0:
        return '1'
    else:
        return '0'
def pop():
    if empty()!='1':
        result=queue.pop(0)
        return result
    else:
        return '-1'
def size():
    return str(len(queue))
def front():
    if len(queue)!=0:
        return queue[0]
    else:
        return '-1'
def back():
    if len(queue)!=0:
        return queue[-1]
    else:
        return '-1'
N=int(sys.stdin.readline())
commands={'push': push, 'pop': pop, 'size': size, 'empty': empty,
          'front': front, 'back': back}
result=[]
for _ in range(N):
    C=sys.stdin.readline().split()
    if C[0]=='push':
        commands[C[0]](C[1])
    else:
        result.append(commands[C[0]]())
print('\n'.join(result))
# 다시 시간 초과
'''
pop(0)은 맨 앞 원소를 제거하는 연산인데, 이 경우 뒤 원소들이 모두 한 칸씩 당겨지며
비효율성이 발생한다.
'''
import sys
queue=[]
def push(e):
    queue.append(e)
def empty():
    if len(queue)==0:
        return '1'
    else:
        return '0'
def pop():
    if empty()!='1':
        queue.reverse()
        result=queue.pop()
        queue.reverse()
        return result
    else:
        return '-1'
def size():
    return str(len(queue))
def front():
    if len(queue)!=0:
        return queue[0]
    else:
        return '-1'
def back():
    if len(queue)!=0:
        return queue[-1]
    else:
        return '-1'
N=int(sys.stdin.readline())
commands={'push': push, 'pop': pop, 'size': size, 'empty': empty,
          'front': front, 'back': back}
result=[]
for _ in range(N):
    C=sys.stdin.readline().split()
    if C[0]=='push':
        commands[C[0]](C[1])
    else:
        result.append(commands[C[0]]())
print('\n'.join(result))
# reverse 두 번을 수행해도 별 성과가 없다. deque 자료구조를 사용해 보면?
'''
collections.deque는 queue.Queue보다 속도가 빠르다
'''
from collections import deque
import sys
dq1=deque()
def push(e):
    dq1.append(e)
def empty():
    if len(dq1)==0:
        return '1'
    else:
        return '0'
def pop():
    if len(dq1)!=0:
        result=dq1.popleft()
        return result
    else:
        return '-1'
def size():
    return str(len(dq1))
def front():
    if len(dq1)!=0:
        return dq1[0]
    else:
        return '-1'
def back():
    if len(dq1)!=0:
        return dq1[-1]
    else:
        return '-1'
commands={'push': push, 'pop': pop, 'size': size, 'empty': empty,
          'front': front, 'back': back}
N=int(sys.stdin.readline())
result=deque()
for _ in range(N):
    C=sys.stdin.readline().split()
    if C[0]=='push':
        commands[C[0]](C[1])
    else:
        result.append(commands[C[0]]())
print('\n'.join(result))

# 2164번: 카드2
# 문제
'''
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 
제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 
카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 
1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 
되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.
'''
# 출력
'''
첫째 줄에 남게 되는 카드의 번호를 출력한다.
'''
# 해법
'''
1. N을 입력받음
2. 1부터 N까지의 자연수를 원소로 갖는 덱 numbers를 생성
3. numbers의 길이가 1이 될 때까지 아래 과정을 반복 수행
popleft 연산으로 맨 앞 숫자를 제거
한 번 더 popleft로 맨 앞 숫자를 제거하여 이를 n으로 저장한 다음 append를 이용하여
맨 뒤에 삽입
'''
from collections import deque
N=int(input())
numbers=deque([x for x in range(1, N+1)])
while len(numbers)>1:
    r1=numbers.popleft()
    r2=numbers.popleft()
    numbers.append(r2)
print(numbers[0])

# 11866번: 요세푸스 문제 0
# 문제
'''
요세푸스 문제는 다음과 같다.
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 
따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 
(7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)
'''
# 출력
'''
예제와 같이 요세푸스 순열을 출력한다.
'''
# 해법
'''
1. N, K를 입력받음. 결과를 저장할 빈 덱 result를 생성
2. '1'부터 'N'까지의 문자열 자연수를 원소로 갖는 덱 numbers를 생성하고, 각 자연수가
result에 포함되었는지 표시할 덱 included를 모든 원소가 False이고 길이가 N인 리스트로
초기화
3. 변수 idx를 K-1로 초기화
무한 루프 반복문을 생성
4. cur을 numbers[idx]로 저장한 후 numbers에서 cur을 제거. result에 cur을 삽입
4가 종료된 후 result의 길이가 N이면 반복문을 탈출
5. idx를 (idx-1+K)%len(numbers)로 대체
6. result의 원소들을 쉼표와 공백 간격으로 출력하고, 이들을 <>로 묶음
'''
from collections import deque
N, K=map(int, input().split())
result=deque()
numbers=deque([f'{x}' for x in range(1, N+1)])
idx=K-1
while True:
    cur=numbers[idx]
    numbers.remove(cur)
    result.append(cur)
    if len(result)==N:
        break
    idx=(idx-1+K)%len(numbers)
print('<'+', '.join(result)+'>')
