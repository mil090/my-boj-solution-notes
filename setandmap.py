# 집합과 맵
# 10815번: 숫자 카드
# 문제
'''
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 
구하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 
-10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 
적혀있는 경우는 없다. 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 
상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 
공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 
작거나 같다.
'''
# 출력
'''
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 
있으면 1을, 아니면 0을 공백으로 구분해 출력한다.
'''
# 해법
'''
1. N을 입력받음
2. N개의 숫자를 입력받아 집합 cards로 저장
3. M을 입력받음
4. M개의 숫자를 입력받아 리스트 numbers로 저장
5. 결과로 반환할 빈 문자열 result를 생성
6. numbers의 각 원소 n에 대하여 n이 cards에 포함되어 있는지 검사. 만약 포함되어
있다면 1, 포함되어 있지 않다면 0을 추가
7. result.strip()을 출력
'''
import sys
N=int(sys.stdin.readline())
cards=set(map(int, sys.stdin.readline().split()))
M=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split()))
result=''
for n in numbers:
    if n in cards:
        result+='1 '
    else:
        result+='0 '
print(result.strip())
# 시간 초과 발생. 더 효율적인 방법은?
'''
집합의 discard 함수를 사용해 보자
1. 현재 반복문에서 사용되는 numbers의 요소는 n
2. cards의 길이는 N
3. cards.discard(n)을 실행
4. cards의 길이가 n이면 n은 cards의 요소가 아니므로 0을 추가하고, cards의 길이가
n이 아니면 n은 cards의 요소이므로 1을 추가하고 n을 다시 삽입
5. result를 출력
'''
import sys
N=int(sys.stdin.readline())
cards=set(map(int, sys.stdin.readline().split()))
M=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split()))
result=''
for n in numbers:
    cards.discard(n)
    if len(cards)==N:
        result+='0 '
    else:
        result+='1 '
        cards.add(n)
print(result.strip())
# 또다시 시간 초과 발생. 효율을 더 올려야 함
'''
map은 입력받은 값을 반복 객체로 만들어 줌. 값을 변경하지 않는다면 굳이 set이나 list로
변환할 필요는 없음
"이진 탐색"을 사용해 보자
1. N을 입력받고, 상근이가 가지고 있는 카드의 숫자들을 입력받아 cards로 저장
2. cards를 정렬
3. M을 입력받고, 상근이가 가지고 있는지 검사할 숫자들을 입력받아 numbers로 저장
4. 이진 탐색 함수 binary_search(A, key, low, high)를 구현
low는 A의 첫 번째 인덱스(0), high는 A의 마지막 인덱스(len(A)-1)
탐색은 low가 high보다 작거나 같은 동안만 진행
middle은 (low+high)//2로 정의. 만약 A[middle]이 key일 경우, key가 A에 있는
것이므로 True를 반환
만약 key가 A[middle]보다 작을 경우, middle보다 오른쪽 인덱스에 있는 원소들은 더
이상 탐색할 필요가 없으므로 high를 middle-1로 하여 순환 호출
만약 key가 A[middle]보다 클 경우, middle보다 왼쪽 인덱스에 있는 원소들은 더 이상
탐색할 필요가 없으므로 low를 middle+1로 하여 순환 호출
만약 순환 호출을 반복한 결과 key가 A에 없다면 False를 반환
5. 결과로 반환할 빈 문자열 result를 생성
6. numbers의 각 원소 n에 대하여 이진 탐색을 진행. 만약 True이면 result에 1을 추가,
False이면 result에 0을 추가
7. result.strip()을 출력
'''
import sys
N=int(sys.stdin.readline())
cards=list(map(int, sys.stdin.readline().split()))
cards.sort()
M=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split()))
def binary_search(A: list, key: int, low: int, high: int):
    if low<=high:
        middle=(low+high)//2
        if key==A[middle]:
            return True
        elif key<A[middle]:
            return binary_search(A, key, low, middle-1)
        else:
            return binary_search(A, key, middle+1, high)
    return False
result=''
for n in numbers:
    if binary_search(cards, n, 0, N-1):
        result+='1 '
    else:
        result+='0 '
print(result.strip())
# 완전히 헛짚고 있었다
'''
시간 초과의 진짜 원인은 탐색 과정이 아니라 문자열 result+= 연산에 있었다
결과 리스트 result를 모든 원소가 '0'이고 길이가 M인 리스트로 생성한 다음, numbers의
각 원소 numbers[i]에 대하여 이것이 cards에 있을 때 result[i]를 '1'로 대체
이 과정이 끝나면 ' '.join(result)를 출력
'''
import sys
N=int(sys.stdin.readline())
cards=set(map(int, sys.stdin.readline().split()))
M=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split()))
result=['0' for _ in range(M)]
for i in range(M):
    if numbers[i] in cards:
        result[i]='1'
print(' '.join(result))
# join을 이용한 결과 출력 방법을 숙지하도록 하자. 
# 문자열과 같은 불변 객체서 += 연산을 반복문에서 사용하는 것은 자제하도록 하자

# 14425번: 문자열 집합
# 문제
'''
총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 
프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.
다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.
다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.
입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 
집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.
'''
# 출력
'''
첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.
'''
# 해법
'''
1. N과 M을 입력받음. 빈 집합 S와 검사할 단어들을 저장할 빈 리스트 words를 생성
2. N개의 줄에 걸쳐 S의 원소를 입력받아 S에 삽입
3. M개의 줄에 걸쳐 검사할 단어를 입력받아 words에 삽입
주의: 위 과정에서 모두 strip 함수를 이용하여 줄 바꾸기 기호를 없애야 함
4. 결과로 반환할 변수 result를 생성하여 0으로 초기화
5. words의 각 원소 w에 대하여, w가 S에 있으면 result에 1을 더함
6. 위 반복문이 끝나면 result를 출력
'''
import sys
N, M=map(int, sys.stdin.readline().split())
S=set()
words=[]
for _ in range(N):
    S.add(sys.stdin.readline().strip())
for _ in range(M):
    words.append(sys.stdin.readline().strip())
result=0
for w in words:
    if w in S:
        result+=1
print(result)

# 7785번: 회사에 있는 사람
# 문제
'''
상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 
출퇴근 시간이다. 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.
각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다.
상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 
들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 
구하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 106) 다음 n개의 줄에는 
출입 기록이 순서대로 주어지며, 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다. 
"enter"인 경우는 출근, "leave"인 경우는 퇴근이다.
회사에는 동명이인이 없으며, 대소문자가 다른 경우에는 다른 이름이다. 사람들의 이름은 
알파벳 대소문자로 구성된 5글자 이하의 문자열이다.
'''
# 출력
'''
현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.
'''
# 해법
'''
입력 데이터의 수가 많을수록, 삽입/삭제 연산은 집합이 리스트에 비해 빨라진다.
1. n을 입력받음. 현재 회사에 있는 직원의 이름을 저장하기 위한 빈 집합 office를 생성
2. n개의 줄에 걸쳐 직원의 이름과 출퇴근 기록을 입력받음
만약 출근(enter)이면 해당 직원의 이름을 office에 삽입하고, 퇴근(leave)이면 해당
직원의 이름을 office에서 제거(remove 함수를 이용)
3. office를 리스트로 변환한 result를 생성하여 내림차순으로 정렬
4. result의 원소들을 한 줄에 하나씩 출력
'''
import sys
n=int(sys.stdin.readline())
office=set()
for _ in range(n):
    name, io=sys.stdin.readline().split()
    if io=='enter':
        office.add(name)
    else:
        office.remove(name)
result=list(office)
result.sort(reverse=True)
print('\n'.join(result))
