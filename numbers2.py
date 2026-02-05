# 약수, 배수와 소수 2
# 1934번: 최소공배수
# 문제
'''
두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 
이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 
30, 60, 90등이 있으며, 최소 공배수는 30이다.
두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 
걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)
'''
# 출력
'''
첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.
'''
# 해법
'''
1. math 모듈의 메소드 gcd를 호출, T를 입력받음
2. 입력받은 두 개의 수를 A, B로 저장하고, 두 수의 최대공약수를 G로 저장
3. 구하는 최소공배수를 L이라고 하면, A*B=G*L이 성립하므로, A*B//G를 출력
'''
from math import gcd
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    A, B=map(int, sys.stdin.readline().split())
    G=gcd(A, B)
    print(A*B//G)

# 13241번: 최소공배수
# 문제
'''
정수 B에 0보다 큰 정수인 N을 곱해 정수 A를 만들 수 있다면, A는 B의 배수이다.
예:
10은 5의 배수이다 (5*2 = 10)
10은 10의 배수이다(10*1 = 10)
6은 1의 배수이다(1*6 = 6)
20은 1, 2, 4,5,10,20의 배수이다.
다른 예:
2와 5의 최소공배수는 10이고, 그 이유는 2와 5보다 작은 공배수가 없기 때문이다.
10과 20의 최소공배수는 20이다.
5와 3의 최소공배수는 15이다.
당신은 두 수에 대하여 최소공배수를 구하는 프로그램을 작성 하는 것이 목표이다.
'''
# 입력
'''
한 줄에 두 정수 A와 B가 공백으로 분리되어 주어진다.
50%의 입력 중 A와 B는 1000(103)보다 작다. 다른 50%의 입력은 1000보다 크고 
100000000(108)보다 작다.
추가: 큰 수 입력에 대하여 변수를 64비트 정수로 선언하시오. C/C++에서는 long long 
int를 사용하고, Java에서는 long을 사용하시오.
'''
# 출력
'''
A와 B의 최소공배수를 한 줄에 출력한다.
'''
# 해법
'''
유클리드 호제법을 구현해 보자
A와 B의 최대공약수를 gcd(A, B)라고 할 때, gcd(A, B)=gcd(B, A%B)
1. A와 B를 입력받음
2. 유클리드 호제법을 이용한 최대공약수를 구하는 함수 euc_gcd(a, b)를 구현
a는 b보다 작지 않음. 만약 a를 b로 나눈 나머지가 0이면 그때의 b 값을 반환
만약 a를 b로 나눈 나머지가 0이 아니면 euc_gcd(b, a%b)를 반환. b로 나눈 나머지는
b보다 항상 작으므로 위 입력 조건을 만족함
3. euc_gcd(max(A, B), min(A, B))가 A, B의 최대공약수가 됨
4. A*B=G*L임을 이용하여 A*B//G의 값을 출력
'''
A, B=map(int, input().split())
def euc_gcd(a: int, b: int):
    if a%b==0:
        return b
    else:
        return euc_gcd(b, a%b)
print(A*B//euc_gcd(max(A, B), min(A, B)))

# 1735번: 분수 합
# 문제
'''
분수 A/B는 분자가 A, 분모가 B인 분수를 의미한다. A와 B는 모두 자연수라고 하자.
두 분수의 합 또한 분수로 표현할 수 있다. 두 분수가 주어졌을 때, 그 합을 기약분수의 
형태로 구하는 프로그램을 작성하시오. 기약분수란 더 이상 약분되지 않는 분수를 의미한다.
'''
# 입력
'''
첫째 줄과 둘째 줄에, 각 분수의 분자와 분모를 뜻하는 두 개의 자연수가 순서대로 주어진다. 
입력되는 네 자연수는 모두 30,000 이하이다.
'''
# 출력
'''
첫째 줄에 구하고자 하는 기약분수의 분자와 분모를 뜻하는 두 개의 자연수를 빈 칸을 사이에 
두고 순서대로 출력한다.
'''
# 해법
'''
1. math 모듈에서 최대공약수와 최소공배수를 구하는 함수 gcd, lcm을 호출
2. 두 분수를 입력받음. 각 분자는 numer1, numer2로, 분모는 denom1, denom2로 입력받음
3. 두 분수의 분모를 통분하기 위해 두 분모의 최소공배수 L을 구함
4. L을 각 분모로 나눈 몫을 q1, q2라고 하고, 이를 각 분자에 곱하여 합함
5. 두 분수를 더한 값을 분수로 나타내면 (numer1*q1+numer2*q2)/L
6. 위 결과에서 분모와 분자의 최대공약수 G를 구하여 각각을 G로 나누고, 그 값을 공백
간격으로 출력
'''
from math import gcd, lcm
numer1, denom1=map(int, input().split())
numer2, denom2=map(int, input().split())
L=lcm(denom1, denom2)
q1=L//denom1
q2=L//denom2
numer=numer1*q1+numer2*q2
G=gcd(numer, L)
print(numer//G, L//G)
# fractions 모듈의 Fraction을 이용하면 보다 간단히 구현할 수 있다
'''
Fraction 함수는 분자와 분모를 입력받아 이를 분수 형태로 나타내는 함수
numerator 변수는 분자를, denominator 변수는 분모를 출력
Fraction 객체끼리 사칙연산을 수행할 경우, 자동으로 기약분수 형태로 바꾸어 줌
'''
from fractions import  Fraction
numer1, denom1=map(int, input().split())
numer2, denom2=map(int, input().split())
frac1=Fraction(numer1, denom1)
frac2=Fraction(numer2, denom2)
result=frac1+frac2
print(result.numerator, result.denominator)
