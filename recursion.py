# 재귀
# 27433번: 팩토리얼 2
# 문제
'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.
'''
# 출력
'''
첫째 줄에 N!을 출력한다.
'''
# 해법
'''
팩토리얼 함수 fac(n)를 만들어 보자
1. n이 1 이하이면 1을 반환
2. n이 2 이상이면 n*fac(n-1)을 반환
3. N을 입력받음
4. fac(N)을 출력
'''
def fac(n: int):
    if n<=1:
        return 1
    else:
        return n*fac(n-1)
N=int(input())
print(fac(N))

# 10870번: 피보나치 수 5
# 문제
'''
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다. 이를 식으로 써보면 
Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다. n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
'''
# 출력
'''
첫째 줄에 n번째 피보나치 수를 출력한다.
'''
# 해법
'''
순환 호출을 이용할 수 있지만, n이 커질수록 호출 횟수가 급격히 커져 효율이 저하되므로
동적 계획법을 이용하자
1. n번째 피보나치 수를 구하는 fib(n) 함수를 구현
메모이제이션 테이블 memoization을 빈 리스트로 생성. 각 인덱스에 해당하는 값이
피보나치 수가 될 예정
0, 1을 memoization에 삽입
2 이상 n 이하의 자연수 i에 대하여, memoization[i-2]+memoization[i-1]을
memoization에 추가
memoization[n]을 반환
2. N을 입력받음
3. fib(N)을 출력
'''
def fib(n: int):
    memoization=[0, 1]
    for i in range(2, n+1):
        memoization.append(memoization[i-2]+memoization[i-1])
    return memoization[n]
N=int(input())
print(fib(N))

# 25501번: 재귀의 귀재
# 문제
'''
정휘는 후배들이 재귀 함수를 잘 다루는 재귀의 귀재인지 알아보기 위해 재귀 함수와 관련된 
문제를 출제하기로 했다.
팰린드롬이란, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열을 말한다. 
팰린드롬의 예시로 AAA, ABBA, ABABA 등이 있고, 팰린드롬이 아닌 문자열의 예시로 
ABCA, PALINDROME 등이 있다.
어떤 문자열이 팰린드롬인지 판별하는 문제는 재귀 함수를 이용해 쉽게 해결할 수 있다. 
아래 코드의 isPalindrome 함수는 주어진 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 
0을 반환하는 함수다.
def recursion(s, l, r):
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)
print('ABBA:', isPalindrome('ABBA'))
print('ABC:', isPalindrome('ABC'))
정휘는 위에 작성된 isPalindrome 함수를 이용하여 어떤 문자열이 팰린드롬인지 여부를 
판단하려고 한다. 구체적으로는, 문자열 S를 isPalindrome 함수의 인자로 전달하여 
팰린드롬 여부를 반환값으로 알아낼 것이다. 더불어 판별하는 과정에서 recursion 함수를 
몇 번 호출하는지 셀 것이다.
정휘를 따라 여러분도 함수의 반환값과 recursion 함수의 호출 횟수를 구해보자.
'''
# 입력
'''
첫째 줄에 테스트케이스의 개수 T가 주어진다. (1<=T<=1,000)
둘째 줄부터 T개의 줄에 알파벳 대문자로 구성된 문자열 S가 주어진다. (1<=|S|<=1,000)
'''
# 출력
'''
각 테스트케이스마다, isPalindrome 함수의 반환값과 recursion 함수의 호출 횟수를 한 
줄에 공백으로 구분하여 출력한다.
'''
# 해법
'''
0. recursion 함수의 해석
s는 팰린드롬인지 확인할 문자열, l은 처음 인덱스, r은 마지막 인덱스
만약 l이 r보다 작은 상태에서, s[l]과 s[r]이 같지 않다면 s는 팰린드롬이 아니므로
0을 반환
만약 l이 r보다 작은 상태에서, s[l]과 s[r]이 같다면, 그 다음 글자를 검사하기 위해
recursion(s, l+1, r-1)을 반환
만약 l이 r보다 크거나 같아졌다면, s는 팰린드롬 조건을 만족한 것이므로 1을 반환
1. recursion 함수의 호출 횟수를 나타내려면?
recursion 함수 인자로 num_import를 생성하여 기본값을 1로 저장
순환이 종료될 때, 즉 0 또는 1을 반환할 때 num_import를 함께 반환하도록 변경
순환 호출을 할 때 num_import의 값을 1 증가시킴
2. T를 입력받음. 결과로 반환할 빈 덱 result를 생성
3. T개의 줄에 걸쳐 문자열을 입력받음
4. 각 문자열의 팰린드롬 여부와 순환 호출 횟수를 튜플 형태로 result에 저장
5. 각 결과를 출력
'''
import sys
from collections import deque
def recursion(s: str, l: int, r: int, num_import: int=1):
    if l >= r:
        return 1, num_import
    elif s[l] != s[r]:
        return 0, num_import
    else:
        return recursion(s, l+1, r-1, num_import+1)
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)
print('ABBA:', isPalindrome('ABBA'))
print('ABC:', isPalindrome('ABC'))
T=int(sys.stdin.readline())
result=deque()
for _ in range(T):
    S=sys.stdin.readline().strip()
    result.append(isPalindrome(S))
for r in result:
    print(' '.join(map(str, r)))

# 24060번: 알고리즘 수업 - 병합 정렬 1
# 문제
'''
오늘도 서준이는 병합 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 
이해했는지 문제를 통해서 확인해보자.
N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 병합 정렬로 배열 A를 오름차순 정렬할 
경우 배열 A에 K 번째 저장되는 수를 구해서 우리 서준이를 도와주자.
크기가 N인 배열에 대한 병합 정렬 의사 코드는 다음과 같다.
merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
    if (p < r) then {
        q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
        merge_sort(A, p, q);      # 전반부 정렬
        merge_sort(A, q + 1, r);  # 후반부 정렬
        merge(A, p, q, r);        # 병합
    }
}
# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
merge(A[], p, q, r) {
    i <- p; j <- q + 1; t <- 1;
    while (i ≤ q and j ≤ r) {
        if (A[i] ≤ A[j])
        then tmp[t++] <- A[i++]; # tmp[t] <- A[i]; t++; i++;
        else tmp[t++] <- A[j++]; # tmp[t] <- A[j]; t++; j++;
    }
    while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
        tmp[t++] <- A[i++];
    while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
        tmp[t++] <- A[j++];
    i <- p; t <- 1;
    while (i ≤ r)  # 결과를 A[p..r]에 저장
        A[i++] <- tmp[t++]; 
}
'''
# 입력
'''
첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 500,000), 저장 횟수 K(1 ≤ K ≤ 10**8)가 주어진다.
다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 10**9)
'''
# 출력
'''
배열 A에 K 번째 저장 되는 수를 출력한다. 저장 횟수가 K 보다 작으면 -1을 출력한다.
'''
# 해법
'''
1. 주어진 유사 코드를 이용하여 병합 정렬 알고리즘을 구현하기
2. '저장 횟수'에 관한 원리를 이해하기
이 문제에서 의미하는 'K번째로 저장되는 수'란 완전히 정렬된 배열에서의 위치를 묻는 것이 
아니라, 비교 후 병합이 K번째 실행될 때 tmp에 저장되는 수를 의미
3. 저장 횟수를 세는 방법을 고안하기
N, K를 입력받음. 저장 횟수 및 결과로 사용할 변수 answer을 생성하여 각각 0, -1로 초기화
merge 함수를 수정. K와 answer을 전역 변수로 사용
i, j를 각각 left와 right의 맨 앞 인덱스인 p, q+1로 초기화
입력 리스트 A를 두 개의 부분 리스트 left와 right로 분할
left=A[p:q+1], right=A[q+1:r+1]
정렬 결과를 저장할 임시 배열 tmp를 빈 리스트로 생성
i와 j가 각각 q+1, r+1보다 작은 동안, left[i]와 right[j]를 비교하여 
left[i]<=right[j]이면 A[i]를 tmp에 삽입하고 i를 1 증가시킴. 그렇지 않다면 
right[j]를 tmp에 삽입하고 j를 1 증가시킴
위 while 반복문이 종료되었을 때, left가 남아 있다면 그 남은 원소들을 tmp에 삽입
right가 남아 있다면 그 남은 원소들을 tmp에 삽입 -> 이렇게 tmp가 완성됨
이렇게 완성된 tmp의 원소를 하나씩 입력 리스트 A에 덮어씀
반복 인덱스 idx는 p에서 r까지 반복됨. 각 반복 루프에서 count의 값을 1 증가시키고,
answer의 값을 tmp[idx]로 대체
위 과정을 반복하다 count의 값이 K와 같아질 경우, answer에 tmp[idx]의 값을 저장
이후 answer의 값을 출력
'''
count, answer=0, -1
def merge(A: list, p: int, q: int, r: int, K: int):
    global count, answer
    i=p
    j=q+1
    temp=[]
    while i<=q and j<=r:
        if A[i]<=A[j]:
            temp.append(A[i])
            i+=1
        else:
            temp.append(A[j])
            j+=1
    if i<=q:
        temp+=A[i:q+1]
    if j<=r:
        temp+=A[j:r+1]
    for idx in range(len(temp)):
        A[p+idx]=temp[idx]
        count+=1
        if count==K:
            answer=A[p+idx]
def merge_sort(A: list, p: int, r: int, K: int):
    if p<r:
        q=(p+r)//2
        merge_sort(A, p, q, K)
        merge_sort(A, q+1, r, K)
        merge(A, p, q, r, K)
        return A
N, K=map(int, input().split())
L=list(map(int, input().split()))
result=merge_sort(L, 0, len(L)-1, K)
print(answer)
# 병합 정렬은 나올 때마다 어려워하므로 반복된 학습이 필요하다!

# 4779번: 칸토어 집합
# 문제
'''
칸토어 집합은 0과 1사이의 실수로 이루어진 집합으로, 구간 [0, 1]에서 시작해서 각 구간을 
3등분하여 가운데 구간을 반복적으로 제외하는 방식으로 만든다.
전체 집합이 유한이라고 가정하고, 다음과 같은 과정을 통해서 칸토어 집합의 근사를 만들어보자.
1. -가 3N개 있는 문자열에서 시작한다.
2. 문자열을 3등분 한 뒤, 가운데 문자열을 공백으로 바꾼다. 이렇게 하면, 선(문자열) 
2개가 남는다.
3. 이제 각 선(문자열)을 3등분 하고, 가운데 문자열을 공백으로 바꾼다. 이 과정은 모든 
선의 길이가 1일때 까지 계속 한다.
예를 들어, N=3인 경우, 길이가 27인 문자열로 시작한다.
---------------------------
여기서 가운데 문자열을 공백으로 바꾼다.
남은 두 선의 가운데 문자열을 공백으로 바꾼다.
---   ---         ---   ---
한번 더
- -   - -         - -   - -
모든 선의 길이가 1이면 멈춘다. N이 주어졌을 때, 마지막 과정이 끝난 후 결과를 출력하는 
프로그램을 작성하시오.
'''
# 입력
'''
입력을 여러 줄로 이루어져 있다. 각 줄에 N이 주어진다. 파일의 끝에서 입력을 멈춘다. 
N은 0보다 크거나 같고, 12보다 작거나 같은 정수이다.
'''
# 출력
'''
입력으로 주어진 N에 대해서, 해당하는 칸토어 집합의 근사를 출력한다.
'''
# 해법
'''
1. N을 입력받음
2. 3**N개의 -로 이루어진 문자열을 토큰화하여 리스트 L로 저장
3. 칸토어 집합의 근사를 구하는 함수 cantor(l)을 구현
l의 길이가 1이면 그대로 l을 반환
l을 같은 길이로 3등분하여 각각을 left, mid, right로 저장
mid의 모든 원소를 공백으로 대체
left와 right에 대하여 cantor 함수를 실행
l을 left+mid+right로 대체하고, l을 반환
4. cantor(l)을 출력
'''
import sys
def cantor(l: list):
    n=len(l)
    if n==1:
        return l
    p=n//3
    q=n//3*2
    left=l[:p]
    mid=l[p:q]
    right=l[q:]
    mid=[' ']*len(mid)
    left=cantor(left)
    right=cantor(right)
    l=left+mid+right
    return l
while True:
    try:
        N=int(sys.stdin.readline())
        L=list('-'*3**N)
        print(''.join(cantor(L)))
    except EOFError:
        break
# ValueError 발생
# 주의사항
'''
sys.stdin.readline은 입력받은 내용이 없을 경우 빈 문자열을 반환
따라서 ''을 정수형으로 반환하지 못해 ValueError가 발생한 것
'''
for line in sys.stdin:
    N=int(line)
    S='-'*3**N
    L=list(S)
    print(''.join(cantor(L)))
# Gemini의 조언: 굳이 문자열을 리스트로 분할할 필요 없이 곧바로 문자열을 바꿔 보자
'''
칸토르 집합의 규칙을 파악
N=0이면 -
N=1이면 - -
N=2이면 - -   - -
N=3이면 - -   - -         - -   - -
-> N=1의 결과는 공백 1개가 가운데, 그 양 옆에 N=0의 결과
-> N=2의 결과는 공백 3개가 가운데, 그 양 옆에 N=1의 결과
-> N=3의 결과는 공백 9개가 가운데, 그 양 옆에 N=2의 결과
-> N=n의 결과는 공백 3**(n-1)개가 가운데, 그 양 옆에 N=n-1의 결과
cantor(n)을 새로 정의해 보자
n이 0이면 -의 개수가 1이므로 -을 반환
이전 단계의 결과를 prev로 저장
prev+' '*3**(n-1)+prev를 반환
'''
import sys
from collections import deque
def cantor(n: int):
    if n==0:
        return '-'
    prev=cantor(n-1)
    return prev+' '*3**(n-1)+prev
result=deque()
for line in sys.stdin:
    N=int(line)
    result.append(cantor(N))
print('\n'.join(result))
