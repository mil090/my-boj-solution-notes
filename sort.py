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

# 10989번: 수 정렬하기 3
# 문제
'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 
수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
'''
# 출력
'''
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
# 해법
'''
지난 두 문제(2750, 2751)와 다른 점은, 입력되는 숫자가 중복될 수 있다는 것(입력 
부분을 읽어 보면, 앞 두 문제와는 달리 수가 중복되지 않는다는 말이 없음)
-> 계수 정렬을 이용
1. 모든 원소가 0이고 길이가 10000인 리스트 counts를 생성
2. N을 입력받음
3. N개의 줄에 걸쳐 자연수 n을 입력받음
4. counts[n-1]의 값을 1 증가시킴
5. 0부터 9999까지의 자연수 i에 대하여 counts[i]의 값이 k일 때, i+1을 k번 출력
이때, 효율 증대를 위해 print 함수 대신 sys.stdout.write 함수를 사용
'''
from sys import stdin, stdout
counts=[0 for _ in range(10000)]
N=int(stdin.readline())
for _ in range(N):
    counts[int(stdin.readline())-1]+=1
for i in range(len(counts)):
    for _ in range(counts[i]):
        stdout.write(str(i+1)+'\n')

# 1427번: 소트인사이드
# 문제
'''
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
'''
# 입력
'''
첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
'''
# 출력
'''
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
'''
# 해법
'''
1. 정렬할 자연수를 문자열 s_N으로 입력받음
2. s_N을 토큰화하여 리스트 s_digits에 저장
3. s_digits의 모든 원소들을 정수형으로 변환한 리스트 digits를 생성
4. digits를 내림차순으로 정렬
5. 결과로 반환할 빈 문자열 result를 생성
6. result에 digit의 각 원소를 순서대로 더함(문자열 포매팅 이용)
7. result를 정수형으로 변환하여 출력
'''
s_N=input()
s_digits=list(s_N)
digits=list(map(int, s_digits))
digits.sort(reverse=True)
result=''
for d in digits:
    result+=f'{d}'
print(int(result))

# 11650번: 좌표 정렬하기
# 문제
'''
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 
y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 
i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 
정수이고, 위치가 같은 두 점은 없다.
'''
# 출력
'''
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''
# 해법
'''
리스트의 정렬 함수 sort의 인자 key
정렬의 기준이 되는 함수를 설정 가능. 예를 들어 숫자로 이루어진 리스트를 정렬할 때
key로 abs를 설정하면 절댓값이 작은 순서대로 정렬함
익명 함수(람다 함수)를 이용하여 구체적인 정렬 기준을 정할 수 있음. 리스트의 각 원소가
2개의 숫자로 이루어진 리스트일 때, 그 합이 큰 순서대로 정렬하고 싶다면
lambda x: x[0]+x[1]이 key 함수의 기능을 함
1. N을 입력받음. 좌표들을 저장할 빈 리스트 coordinates를 생성
2. N개의 줄에 걸쳐 x좌표와 y좌표를 입력받음. 이 두 좌표로 이루어진 리스트를
coordinates에 삽입
3. coordinates를 정렬. key로는 리스트의 첫 번째 원소와 두 번째 요소를 튜플 형태로
반환하는 람다 함수를 이용. 이렇게 입력하면, 먼저 리스트의 첫 번째 요소를 기준으로 정렬한
다음, 두 번째 요소를 기준으로 정렬하게 됨
4. 정렬된 결과를 형식에 맞게 출력
'''
import sys
N=int(sys.stdin.readline())
coordinates=[]
for _ in range(N):
    c=list(map(int, sys.stdin.readline().split()))
    coordinates.append(c)
coordinates.sort(key=lambda x: (x[0], x[1]))
for coor in coordinates:
    print(coor[0], coor[1])
# 정보: 튜플은 정렬 함수를 실행할 경우 알아서 맨 처음 요소부터 비교하여 정렬
l=[(3, 4), (1, 1), (1, -1), (2, 2), (3, 3)]
l.sort()
for i in l:
    print(i[0], i[1])
# 튜플을 이용하여 효율을 늘리면?
import sys
N=int(sys.stdin.readline())
coordinates=[]
for _ in range(N):
    c=tuple(map(int, sys.stdin.readline().split()))
    coordinates.append(c)
coordinates.sort()
for coor in coordinates:
    print(coor[0], coor[1])

# 11651번: 좌표 정렬하기 2
# 문제
'''
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 
x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 
i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 
정수이고, 위치가 같은 두 점은 없다.
'''
# 출력
'''
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''
# 해법
'''
1. N을 입력받음. 좌표를 저장할 빈 리스트 coordinates를 생성
2. N개의 줄에 걸쳐 좌표를 입력받고, 이를 coordinates에 저장
3. 람다 함수를 이용하여 각 좌표들을 y좌표, x좌표를 기준으로 정렬
4. 정렬 결과를 출력
'''
import sys
N=int(sys.stdin.readline())
coordinates=[]
for _ in range(N):
    c=list(map(int, sys.stdin.readline().split()))
    coordinates.append(c)
coordinates.sort(key=lambda x: (x[1], x[0]))
for coor in coordinates:
    print(coor[0], coor[1])

# 1181번: 단어 정렬
# 문제
'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 
프로그램을 작성하시오.
1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.
'''
# 입력
'''
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 
알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 
넘지 않는다.
'''
# 출력
'''
조건에 따라 정렬하여 단어들을 출력한다.
'''
# 해법
'''
Python에서는 문자열 간의 대소 비교도 가능
1. N을 입력받음. 단어를 입력받을 빈 집합 words를 생성
2. N개의 줄에 걸쳐 단어를 입력받아 words에 저장하고, words를 집합으로 변환
3. 중복된 단어를 없앤 후 다시 리스트로 변환한 words를 정렬 -> 기수 정렬 매커니즘
낮은 우선순위에 따라 먼저 정렬하고, 순차적으로 우선순위를 높임
먼저 사전식으로 정렬
그 다음으로 길이 순으로 정렬. 이렇게 하면 길이가 같은 단어에 대해서는 사전식 정렬이 유지
4. 정렬 결과를 출력
'''
import sys
N=int(sys.stdin.readline())
words=set()
for _ in range(N):
    words.add(sys.stdin.readline().strip())
words=list(words)
words.sort()
words.sort(key=len)
for w in words:
    print(w)
# 정보: input과 달리 sys.stdin.readline은 입력받을 때 기본적으로 줄 바꿈 기호가
# 뒤에 따라 붙는다

# 10814번: 나이순 정렬
# 문제
'''
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 
나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 
프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 
1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 
있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.
'''
# 출력
'''
첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 
한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.
'''
# 해법
'''
기본적으로 가입 순서대로 입력되므로, 나이 순으로 정렬하기만 하면 같은 나이의 회원 간에는 
가입 순서가 유지됨
1. N을 입력받음. 각 회원의 나이와 이름을 저장할 빈 리스트 users를 생성
2. N개의 줄에 걸쳐 회원의 나이와 이름을 (가입 순서대로) 입력받고, 이를 users에 저장
3. users를 나이 순서대로 정렬
4. users의 원소들을 하나씩 출력
'''
import sys
N=int(sys.stdin.readline())
users=[]
for _ in range(N):
    age, name=sys.stdin.readline().split()
    users.append([int(age), name])
users.sort(key=lambda x: x[0])
for u in users:
    print(u[0], u[1])

# 18870번: 좌표 압축
# 문제
'''
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
'''
# 입력
'''
첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.
'''
# 출력
'''
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
'''
# 해법
'''
1. N을 입력받음
2. 압축할 좌표 N개를 입력받아 리스트 coordinates로 저장
3. coordinates의 사본 copy_coor를 생성
4. copy_coor를 정렬
5. coordinates의 각 원소 coor에 대하여 copy_coor.index(coor)가 coor의 좌표
압축 결과가 됨
'''
import sys
N=int(sys.stdin.readline())
coordinates=list(map(int, sys.stdin.readline().split()))
copy_coor=coordinates.copy()
copy_coor.sort()
result=''
for coor in coordinates:
    result+=f'{copy_coor.index(coor)} '
print(result.strip())
# 시간 초과. 다른 방법을 생각해 보자
'''
1. N을 입력받음
2. 압축할 좌표 N개를 입력받아 리스트 coordinates로 저장
3. set을 이용하여 중복 값을 없앤 다음, 다시 리스트로 만들어 coordinates를 정렬
4. 빈 딕셔너리 order를 생성
5. order의 key를 coordinates의 좌표로, value를 인덱스로 지정하여 삽입
6. order의 values를 key 순서대로 출력
'''
import sys
N=int(sys.stdin.readline())
coordinates=list(map(int, sys.stdin.readline().split()))
unique_coor=list(set(coordinates))
unique_coor.sort()
rank_dict={value: index for index, value in enumerate(unique_coor)}
print(' '.join(str(rank_dict[coor]) for coor in coordinates))