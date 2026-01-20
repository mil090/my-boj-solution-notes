# 약수, 배수와 소수 1
# 5086번: 배수와 약수
# 문제
'''
4 * 3 = 12이다.

이 식을 통해 다음과 같은 사실을 알 수 있다.

3은 12의 약수이고, 12는 3의 배수이다.

4도 12의 약수이고, 12는 4의 배수이다.

두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

첫 번째 숫자가 두 번째 숫자의 약수이다.
첫 번째 숫자가 두 번째 숫자의 배수이다.
첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
'''
# 입력
'''
입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 10,000이 넘지않는 두 
자연수로 이루어져 있다. 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.
'''
# 출력
'''
각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 
multiple을, 둘 다 아니라면 neither를 출력한다.
'''
# 해법
'''
1. A, B를 입력받음
2-1. A>B이면 A%B를 계산. 이 값이 0이면 multiple, 0이 아니면 neither를 출력
2-2. A<B이면 B%A를 계산. 이 값이 0이면 factor, 0이 아니면 neither를 출력
3. 1~2의 과정을 반복문으로 구현. while True로 무한루프를 만든 후, A와 B가 모두
0이면 break로 반복문을 탈출
'''
while True:
    A, B=map(int, input().split())
    if A==0 and B==0:
        break
    if A>B:
        if A%B==0:
            print('multiple')
        else:
            print('neither')
    else:
        if B%A==0:
            print('factor')
        else:
            print('neither')

# 2501번: 약수 구하기
# 문제
'''
어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다. 
6을 예로 들면
6 ÷ 1 = 6 … 0
6 ÷ 2 = 3 … 0
6 ÷ 3 = 2 … 0
6 ÷ 4 = 1 … 2
6 ÷ 5 = 1 … 1
6 ÷ 6 = 1 … 0
그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 
작성하시오.
'''
# 입력
'''
첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 
이상 N 이하이다.
'''
# 출력
'''
첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 
적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.
'''
# 해법
'''
1. N, K를 입력받음
2. N의 약수들을 저장할 빈 리스트 factors를 생성
3. 1부터 N까지 N개의 자연수 i에 대하여 i가 N의 약수이면, 즉 N을 i로 나눈 나머지가
0이면 i를 factors에 삽입
4. try-except를 이용하여 예외 처리. try 내에서 factors[K-1]을 출력. 만약 try
내에서 오류가 발생할 경우, except를 이용하여 0을 출력하도록 예외 처리
'''
N, K=map(int, input().split())
factors=[]
for i in range(1, N+1):
    if N%i==0:
        factors.append(i)
try:
    print(factors[K-1])
except:
    print(0)

# 9506번: 약수들의 합
# 문제
'''
어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.
예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.
n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.
'''
# 입력
'''
입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)
입력의 마지막엔 -1이 주어진다.
'''
# 출력
'''
테스트케이스 마다 한줄에 하나씩 출력해야 한다.
n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).
이때, 약수들은 오름차순으로 나열해야 한다.
n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.
'''
# 해법
'''
1. while True로 무한 루프 틀을 생성
2. n을 입력받음. 만약 입력받은 n이 -1이면 break로 반복문을 탈출
3. n 자신을 제외한 n의 약수들을 저장할 빈 리스트 factors를 생성
4. 1부터 n-1까지의 자연수 i에 대하여 i가 n의 약수이면, 즉 n을 i로 나눈 나머지가
0이면 i를 factors에 삽입
5. factors의 모든 원소의 합과 n을 비교
6-1. 두 값이 같으면 결과로 출력할 빈 문자열 result를 생성. result에 'n =' 를 추가
factors의 각 원소 f에 대하여 result에 f를 추가. 만약 f가 factors의 최댓값이
아니라면 result에 ' + '를 추가. 반복문이 종료되면 result를 출력
6-2. 두 값이 다르면 'n is NOT perfect'를 출력
'''
while True:
    n=int(input())
    if n==-1:
        break
    factors=[]
    for i in range(1, n):
        if n%i==0:
            factors.append(i)
    if n==sum(factors):
        result=''
        result+=f'{n} = '
        for f in factors:
            result+=f'{f}'
            if f!=max(factors):
                result+=' + '
        print(result)
    else:
        print(f'{n} is NOT perfect.')

# 1978번: 소수 찾기
# 문제
'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
'''
# 입력
'''
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 
1,000 이하의 자연수이다.
'''
# 출력
'''
주어진 수들 중 소수의 개수를 출력한다.
'''
# 해법
'''
어떤 자연수가 소수일 필요충분조건: 그 자연수의 약수의 개수가 2
1. N을 입력받음. 결과로 반환할 변수 result를 생성하여 0으로 초기화
2. N번 동안 반복문을 진행
3. 소수인지 판별할 자연수 n을 입력받음. n의 약수를 저장할 리스트 factors를 생성
4. 1부터 n까지의 자연수 i에 대하여 i가 n의 약수이면, 즉 n을 i로 나눈 나머지가 0이면
i를 factors에 추가
5. factors의 길이가 2이면 result에 1을 더함
6. 반복문이 종료되면 result를 출력
'''
N=int(input())
result=0
numbers=list(map(int, input().split()))
for idx in range(N):
    n=numbers[idx]
    factors=[]
    for i in range(1, n+1):
        if n%i==0:
            factors.append(i)
    if len(factors)==2:
        result+=1
print(result)
