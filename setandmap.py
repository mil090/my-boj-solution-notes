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
