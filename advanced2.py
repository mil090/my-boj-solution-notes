# 심화 2
# 1037번: 약수
# 문제
'''
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 
둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 
자연수이고, 중복되지 않는다.
'''
# 출력
'''
첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.
'''
# 해법
'''
1. N의 진짜 약수의 개수를 입력받음
2. N의 진짜 약수들을 입력받아 리스트 factors로 저장
3. factors의 최댓값과 최솟값의 곱이 N이 됨
'''
count=int(input())
factors=list(map(int, input().split()))
print(max(factors)*min(factors))

# 25192번: 인사성 밝은 곰곰이
# 문제
'''
알고리즘 입문방 오픈 채팅방에서는 새로운 분들이 입장을 할 때마다 곰곰티콘을 사용해 인사를 
한다. 이를 본 문자열 킬러 임스는 채팅방의 기록을 수집해 그 중 곰곰티콘이 사용된 횟수를 
구해 보기로 했다.
ENTER는 새로운 사람이 채팅방에 입장했음을 나타낸다. 그 외는 채팅을 입력한 유저의 
닉네임을 나타낸다. 닉네임은 숫자 또는 영문 대소문자로 구성되어 있다.
새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다. 
그 외의 기록은 곰곰티콘을 쓰지 않은 평범한 채팅 기록이다.
채팅 기록 중 곰곰티콘이 사용된 횟수를 구해보자!
'''
# 입력
'''
첫 번째 줄에는 채팅방의 기록 수를 나타내는 정수 N이 주어진다. (1<=N<=100,000)
두 번째 줄부터 N개의 줄에 걸쳐 새로운 사람의 입장을 나타내는 ENTER, 혹은 채팅을 
입력한 유저의 닉네임이 문자열로 주어진다. (1<={문자열 길이}<=20)
첫 번째 주어지는 문자열은 무조건 ENTER이다.
'''
# 출력
'''
채팅 기록 중 곰곰티콘이 사용된 횟수를 출력하시오.
'''
# 해법
'''
1. N을 입력받음. 채팅을 입력한 사람의 이름을 저장할 빈 집합 names를 생성하고, 결과로
반환할 변수 result를 생성하여 0으로 초기화
2. N개의 줄에 걸쳐 ENTER 또는 사람의 이름 chat을 입력받음
3. chat이 ENTER일 경우, names의 모든 원소를 삭제
4. chat이 사람 이름일 경우, 기존 names의 길이를 n으로 저장한 다음 chat을 names에
추가. 새로운 names의 길이가 n보다 클 경우 그 사람은 처음으로 채팅을 친 것이므로
result에 1을 추가
5. result를 출력
'''
import sys
N=int(sys.stdin.readline())
names=set()
result=0
for _ in range(N):
    chat=sys.stdin.readline().strip()
    if chat=='ENTER':
        names.clear()
    else:
        n=len(names)
        names.add(chat)
        if len(names)>n:
            result+=1
print(result)

# 26069번: 붙임성 좋은 총총이
# 문제
'''
총총이는 친구 곰곰이의 소개로 제2회 곰곰컵에 출연할 기회를 얻었다!

총총이는 자신의 묘기인 무지개 댄스를 선보여, 여러분의 환심을 사려 한다. 이 댄스는 
중독성이 강하기 때문에, 한번 보게 된 사람은 모두 따라 하게 돼버린다.
사람들이 만난 기록이 시간 순서대로 N개 주어진다. (총총이는 토끼이지만 이 문제에서는 
편의상 사람이라고 가정한다.)무지개 댄스를 추지 않고 있던 사람이 무지개 댄스를 추고 있던 
사람을 만나게 된다면, 만난 시점 이후로 무지개 댄스를 추게 된다.
기록이 시작되기 이전 무지개 댄스를 추고 있는 사람은 총총이 뿐이라고 할 때, 마지막 기록 
이후 무지개 댄스를 추는 사람이 몇 명인지 구해보자!
'''
# 입력
'''
첫번째 줄에는 사람들이 만난 기록의 수 N(1<=N<=1,000)이 주어진다.
두번째 줄부터 N개의 줄에 걸쳐 사람들이 만난 기록이 주어진다. 
i + 1번째 줄에는 i번째로 만난 사람들의 이름 A_i와 B_i가 공백을 사이에 두고 주어진다. 
A_i와 B_i는 숫자와 영문 대소문자로 이루어진 최대 길이 20의 문자열이며, 서로 같지 않다.
총총이의 이름은 ChongChong으로 주어지며, 기록에서 1회 이상 주어진다.
동명이인은 없으며, 사람의 이름은 대소문자를 구분한다. (ChongChong과 chongchong은 
다른 이름이다.)
'''
# 출력
'''
마지막 기록 이후 무지개 댄스를 추는 사람의 수를 출력하라.
'''
# 해법
'''
1. N을 입력받음. 현재 무지개 댄스를 추고 있는 사람의 이름을 저장할 집합 dance를
생성하고 ChongChong을 삽입
2. N개의 줄에 걸쳐 서로 만난 두 사람의 이름을 입력받음. 만약 두 사람 중 한 명이라도
dance에 있을 경우(isdisjoint 함수를 이용), 두 사람의 이름을 모두 dance에 삽입
3. dance의 길이를 출력
'''
import sys
N=int(sys.stdin.readline())
dance={'ChongChong'}
for _ in range(N):
    meet=set(sys.stdin.readline().split())
    if not dance.isdisjoint(meet):
        dance.update(meet)
print(len(dance))

# 2108번: 통계학
# 문제
'''
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 
기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 
N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
'''
# 출력
'''
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.
'''
# 해법
'''
round 함수는 일반 반올림 함수와는 다르다. 반올림 연산을 사용하기 위해서는 decimal
모듈의 ROUND_HALF_UP을 사용해야 한다.
0. 반올림 함수 traditional_round(num, digit)을 구현
반올림할 값 num을 Decimal 객체로 변환하여 d로 저장
d를 소수점 첫째 자리에서 반올림하고, 이를 정수형으로 변환하여 반환
1. N을 입력받음. 변량을 저장할 빈 덱 x를 생성
2. N개의 줄에 걸쳐 변량을 입력받아 x에 저장
3. x를 리스트로 변환
4. x의 산술 평균을 구하여 avg로 저장
5. x를 정렬한 후, (N-1)//2에 해당하는 인덱스의 원소가 중앙값이므로 median으로 저장
6. Counter 함수를 이용하여 각 변량의 빈도를 구하고, 그 결과를 딕셔너리로 변환
최대 빈도를 most_freq으로 저장하고, 최대 빈도를 가지는 변량만을 모아 리스트로 저장
이 리스트를 정렬한 후 두 번째로 작은 값을 mode로 저장
7. x는 이미 정렬되어 있으므로 x[-1]이 최대, x[0]이 최소. 따라서 두 값의 차를 구하여
R로 저장
8. avg를 반올림하여 출력
9. 나머지 세 값들은 모두 정수형이므로 그냥 출력
'''
from decimal import Decimal, ROUND_HALF_UP
from collections import deque, Counter
import sys
def traditional_round(num: int|float, digit: int=0):
    d=Decimal(str(num))
    return float(d.quantize(Decimal(10)**-digit, rounding=ROUND_HALF_UP))
N=int(sys.stdin.readline())
x=deque()
for _ in range(N):
    x.append(int(sys.stdin.readline()))
x=list(x)
avg=sum(x)/N
x.sort()
median=x[(N-1)//2]
freq=dict(Counter(x))
most_freq=max(freq.values())
modes=[key for key, value in freq.items() if value==most_freq]
modes.sort()
if len(modes)>=2:
    mode=modes[1]
else:
    mode=modes[0]
R=x[-1]-x[0]
result=list(map(str, [int(traditional_round(avg)), median, mode, R]))
print('\n'.join(result))
