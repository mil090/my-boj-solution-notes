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
