# 정렬
# 2750번: 수 정렬하기
# 문제
'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 
주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
'''
# 출력
'''
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
# 해법
'''
1. N을 입력받음. 정렬 대상이 되는 숫자들을 저장할 빈 리스트 numbers를 생성
2. N개의 줄에 걸쳐 정렬 대싱이 되는 숫자들을 입력받고, 이들을 numbers에 삽입
3. numbers를 정렬(sort 함수)
4. numbers의 각 원소들을 출력
'''
N=int(input())
numbers=[]
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
for n in numbers:
    print(n)

# 2587번: 대표값2
# 문제
'''
어떤 수들이 있을 때, 그 수들을 대표하는 값으로 가장 흔하게 쓰이는 것은 평균이다. 
평균은 주어진 모든 수의 합을 수의 개수로 나눈 것이다. 예를 들어 10, 40, 30, 60, 30의 
평균은 (10 + 40 + 30 + 60 + 30) / 5 = 170 / 5 = 34가 된다.
평균 이외의 또 다른 대표값으로 중앙값이라는 것이 있다. 중앙값은 주어진 수를 크기 
순서대로 늘어 놓았을 때 가장 중앙에 놓인 값이다. 예를 들어 10, 40, 30, 60, 30의 
경우, 크기 순서대로 늘어 놓으면 10 30 30 40 60이 되고 따라서 중앙값은 30이 된다.
다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄부터 다섯 번째 줄까지 한 줄에 하나씩 자연수가 주어진다. 주어지는 자연수는 100보다 
작은 10의 배수이다.
'''
# 출력
'''
첫째 줄에는 평균을 출력하고, 둘째 줄에는 중앙값을 출력한다. 평균과 중앙값은 모두 
자연수이다.
'''
# 해법
'''
0. 5개의 자연수를 저장할 빈 리스트 numbers를 생성
1. 5줄에 걸쳐 자연수 5개를 입력받아 numbers에 삽입
2. 평균은 numbers의 총합을 numbers의 길이(5)로 나눈 값
3. 중위수는 numbers를 정렬한 후, 가운데에 있는 값. 즉 정렬된 numbers에서 인덱스 2에
해당하는 값
'''
numbers=[]
for _ in range(5):
    numbers.append(int(input()))
mean=sum(numbers)//len(numbers)
numbers.sort()
median=numbers[2]
print(mean)
print(median)

# 25305번: 커트라인
# 문제
'''
2022 연세대학교 미래캠퍼스 슬기로운 코딩생활에 N명의 학생들이 응시했다. 이들 중 점수가 
가장 높은 k명은 상을 받을 것이다. 이 때, 상을 받는 커트라인이 몇 점인지 구하라.
커트라인이란 상을 받는 사람들 중 점수가 가장 가장 낮은 사람의 점수를 말한다.
'''
# 입력
'''
첫째 줄에는 응시자의 수 N과 상을 받는 사람의 수 k가 공백을 사이에 두고 주어진다.
둘째 줄에는 각 학생의 점수 x가 공백을 사이에 두고 주어진다.
'''
# 출력
'''
상을 받는 커트라인을 출력하라.
'''
# 제한
'''
1≤N≤1000
1≤k≤N
0≤x≤10000
'''
# 해법
'''
1. N과 k를 입력받음
2. N개의 점수를 입력받아 이들을 원소로 갖는 리스트 scores를 생성
3. scores를 정렬
4. scores[-k]를 출력
'''
N, k=map(int, input().split())
scores=list(map(int, input().split()))
scores.sort()
print(scores[-k])

# 2751번: 수 정렬하기 2
# 문제
'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 
주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
'''
# 출력
'''
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
# 해법
'''
기본적으로 리스트의 sort 함수는 병합 정렬과 삽입 정렬을 섞은 알고리즘을 사용
이번 문제에서는 알고리즘 복습을 위해 병합 정렬을 구현해 보도록 하자
1. N을 입력받음. 정렬 대상이 되는 숫자들을 저장할 빈 리스트 numbers를 생성
2. N개의 줄에 걸쳐 정렬 대싱이 되는 숫자들을 입력받고, 이들을 numbers에 삽입
3. 병합 정렬 함수 merge_sort를 구현
3-0. 탈출 조건: 입력 리스트 L의 길이가 1일 경우 그 자체로 이미 정렬된 것이므로,
별다른 작업 없이 L을 그대로 반환
3-1. L의 길이가 2 이상이면 L을 두 부분 리스트로 분할. L의 길이가 n일 때, n/2보다 
작거나 같은 인덱스는 왼쪽 부분 리스트, 나머지는 오른쪽 부분 리스트로
3-2. 위와 같은 분할은 각 부분 리스트의 길이가 1이 될 때까지 반복
3-3. 두 부분 리스트의 길이가 1이 되었다면, 모두 정렬된 것이므로 이들을 병합
병합 결과가 될 빈 리스트 result를 생성
3-4. left와 right의 현재 인덱스를 각각 i, j라고 할 때, i와 j가 각각 left와
right의 길이보다 작은 동안 left[i]와 right[j] 중 크지 않은 값을 result에 삽입
left와 right 중 어느 하나의 삽입이 완료되면 나머지 한 쪽의 원소들을 result에 삽입
result를 반환
'''
def merge_sort(L: list):
    n=len(L)
    if n==1:
        return L
    left=merge_sort(L[:n//2])
    right=merge_sort(L[n//2:])
    i=j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
N=int(input())
numbers=[]
for _ in range(N):
    numbers.append(int(input()))
r=merge_sort(numbers)
for e in r:
    print(e)
# 병합 정렬에 관해 확실하게 이해하도록 하자
N=int(input())
numbers=[]
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
for e in numbers:
    print(e)
# 퀵 정렬
def quick_sort(L: list):
    if len(L)<=1:
        return L
    pivot=0
    left=[]
    right=[]
    for n in L[pivot+1:]:
        if n<L[pivot]:
            left.append(n)
        else:
            right.append(n)
    r_left=quick_sort(left)
    r_right=quick_sort(right)
    result=r_left+[L[pivot]]+r_right
    return result
N=int(input())
numbers=[]
for _ in range(N):
    numbers.append(int(input()))
r=quick_sort(numbers)
for e in r:
    print(e)
# 시간 복잡도 개선을 위해 input 대신 sys.stdin.readline을 사용하자
from sys import stdin
N=int(stdin.readline())
numbers=[]
for _ in range(N):
    numbers.append(int(stdin.readline()))
r=quick_sort(numbers)
for e in r:
    print(e)
'''
입력받는 횟수가 많을 때에는 input과 sys.stdin.readline의 차이가 커진다는 점을
명심하도록 하자
'''
from sys import stdin
def merge_sort(L: list):
    n=len(L)
    if n==1:
        return L
    left=merge_sort(L[:n//2])
    right=merge_sort(L[n//2:])
    i=j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
N=int(stdin.readline())
numbers=[]
for _ in range(N):
    numbers.append(int(stdin.readline()))
r=merge_sort(numbers)
for e in r:
    print(e)
# 추가적인 효율 개선: print의 잦은 호출이 알고리즘의 효율을 저하시킴
# 줄 바꿈 기호를 구분자로 하여 numbers의 숫자들을 출력
from sys import stdin
N=int(stdin.readline())
numbers=[]
for _ in range(N):
    numbers.append(int(stdin.readline()))
numbers.sort()
print('\n'.join(map(str, numbers)))
