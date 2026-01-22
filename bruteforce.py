# 브루트 포스
# 2798번: 블랙잭
# 문제
'''
카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 
한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 
있다.
한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 
모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 
변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 
만들어야 한다.
N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 
3장의 합을 구해 출력하시오.
'''
# 입력
'''
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 
둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
'''
# 출력
'''
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
'''
# 해법
'''
1. N, M을 입력받음
2. N개의 숫자를 입력받아 리스트 numbers에 저장
3. numbers에서 뽑은 세 숫자의 합을 구해 저장하기 위한 빈 리스트 result를 생성
4. itertools 모듈의 combinations 메소드를 이용하여 numbers에서 서로 다른 세 
숫자를 뽑고, 그 합을 result에 저장
5. result의 최댓값을 출력
'''
from itertools import combinations
N, M=map(int, input().split())
numbers=list(map(int, input().split()))
result=[]
for com in combinations(numbers, 3):
    if sum(com)<=M:
        result.append(sum(com))
print(max(result))
# 연산 시간을 줄이기 위해 input 대신 sys.stdin.readline을 이용하면?
from sys import stdin
from itertools import combinations
N, M=map(int, stdin.readline().split())
numbers=list(map(int, stdin.readline().split()))
result=[]
coms=list(combinations(numbers, 3))
for com in coms:
    if sum(com)<=M:
        result.append(sum(com))
print(max(result))

# 2231번: 분해합
# 문제
'''
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 
의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 
분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 
자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 
있다.
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
'''
# 출력
'''
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.
'''
# 해법
'''
1. N을 입력받음. N의 생성자들을 저장할 빈 리스트 result를 생성
2. N의 생성자는 N보다 작으므로, 1부터 N-1까지의 자연수 n에 대하여 n이 N의 생성자인지
검사. n과 그 자리 숫자를 저장할 빈 리스트 e를 생성
3. n을 문자열 strn으로 바꾼 후, e에 strn을 삽입. n을 토큰화하여 각 토큰을 e에 삽입
4. e의 각 원소들을 정수형으로 바꾼 후, 그 합을 구하여 N과 같으면 n을 result에 삽입
5. result의 최솟값을 출력. 만약 result가 빈 리스트일 경우 0을 출력
'''
N=int(input())
result=[]
for n in range(1, N):
    e=[]
    strn=str(n)
    e.append(strn)
    for i in strn:
        e.append(i)
    e=list(map(int, e))
    if sum(e)==N:
        result.append(n)
try:
    print(min(result))
except:
    print(0)
