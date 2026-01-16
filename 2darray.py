# 2차원 배열

# 2738번: 행렬 덧셈
# 문제
'''
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 
차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. 
N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
'''
# 출력
'''
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 
구분한다.
'''
# 해법
'''
1. 행렬의 크기 N과 M을 입력받음(N은 행 수, M은 열 수)
2. 빈 리스트 A와 B를 생성
3. 각각 N번 반복되는 반복문을 이용하여 A, B의 행을 생성하고, 이들을 각각 A, B에 삽입
4. A, B의 각 행을 가져와서, 같은 열의 요소끼리 더한 값을 공백 간격으로 출력
'''
import numpy as np
N, M=map(int, input().split())
A=[]
B=[]
for _ in range(N):
    row=list(map(int, input().split()))
    A.append(row)
for _ in range(N):
    row=list(map(int, input().split()))
    B.append(row)
A, B=np.array(A), np.array(B)
for r in range(N):
    for c in range(M):
        print((A+B)[r][c], end=' ')
    print()
# 그러나 백준에서는 numpy와 같은 외부 모듈을 사용할 수 없으므로 다른 방법을 고안
N, M=map(int, input().split())
A=[]
B=[]
for _ in range(N):
    row=list(map(int, input().split()))
    A.append(row)
for _ in range(N):
    row=list(map(int, input().split()))
    B.append(row)
for r in range(N):
    Arow=A[r]
    Brow=B[r]
    for c in range(M):
        print(Arow[c]+Brow[c], end=' ')
    print()

# 2566번: 최댓값
# 문제
'''
<그림 1>과 같이 9*9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 
최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
예를 들어, 다음과 같이 81개의 수가 주어지면
(그림 생략)
이들 중 최댓값은 90이고, 이 값은 5행 7열에 위치한다.
'''
# 입력
'''
첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 
작은 자연수 또는 0이다.
'''
# 출력
'''
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 
사이에 두고 차례로 출력한다. 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.
'''
# 해법
'''
1. 입력받은 81개의 숫자를 저장할 빈 리스트 numbers를 생성하고, 최댓값의 위치를 나타낼
행 번호와 열 번호 변수를 각각 row, col로 생성하여 0으로 초기화
2. 한 줄에 9개씩 총 9줄의 숫자들을 리스트로 입력받아 numbers에 저장
3. 최댓값을 찾기 위한 반복문 시작. 우선 구하는 최댓값 maximum을 0으로 초기화
(numbers의 각 숫자는 음이 아닌 정수이므로, 최댓값 역시 음이 아닌 정수)
4. 0부터 9까지의 숫자로 반복문을 진행. 이때 행 번호는 반복 인자 i에 1을 더한 값
5. 각 행의 원소들을 maximum과 비교하는 반복문을 진행. 만약 현재 원소가 maximum보다
크다면, maximum을 그 원소 값으로 대체하고, row와 col을 각각 해당 원소의 행 번호 및
열 번호로 대체
6. 반복문이 종료되면 첫 번째 줄에 maximum을 출력하고, 두 번째 줄에 row와 col을
공백 간격으로 출력
'''
numbers=[]
maximum=0
row, col=1, 1
for _ in range(9):
    r=list(map(int, input().split()))
    numbers.append(r)
for i in range(9):
    for j in range(9):
        if maximum<numbers[i][j]:
            maximum=numbers[i][j]
            row=i+1
            col=j+1
print(maximum)
print(row, col, sep=' ')
