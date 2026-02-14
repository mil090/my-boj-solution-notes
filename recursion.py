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
