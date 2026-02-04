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

# 1620번: 나는야 포켓몬 마스터 이다솜
# 문제
'''
오박사 : 그럼 다솜아 이제 진정한 포켓몬 마스터가 되기 위해 도감을 완성시키도록 하여라. 
일단 네가 현재 가지고 있는 포켓몬 도감에서 포켓몬의 이름을 보면 포켓몬의 번호를 말하거나, 
포켓몬의 번호를 보면 포켓몬의 이름을 말하는 연습을 하도록 하여라. 나의 시험을 통과하면, 
내가 새로 만든 도감을 주도록 하겠네.
'''
# 입력
'''
첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 
주어져. N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수인데, 자연수가 
뭔지는 알지? 모르면 물어봐도 괜찮아. 나는 언제든지 질문에 답해줄 준비가 되어있어.
둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 
줄에 하나씩 입력으로 들어와. 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 
글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어. 아참! 일부 포켓몬은 마지막 
문자만 대문자일 수도 있어. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야. 그 다음 
줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와. 문제가 알파벳으로만 
들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 
출력해야해. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 
입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅!!!
'''
# 출력
'''
첫째 줄부터 차례대로 M개의 줄에 각각의 문제에 대한 답을 말해줬으면 좋겠어!!!. 
입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 
포켓몬의 이름에 해당하는 번호를 출력하면 돼. 그럼 땡큐~
'''
# 해법
'''
1. N, M을 입력받음. 두 개의 딕셔너리 num_pokemon과 pokemon_num을 생성
num_pokemon은 포켓몬 번호를 key, 포켓몬 이름을 value로 하는 딕셔너리
pokemon_num은 포켓몬 이름을 key, 포켓몬 번호를 value로 하는 딕셔너리
2. N개의 줄에 걸쳐 도감에 수록된 포켓몬의 이름 pokemon을 입력받음
3. 두 개의 딕셔너리에 알맞게 삽입
num_pokemon[i+1]=pokemon
pokemon_num[pokemon]=i+1
4. M개의 줄에 걸쳐 문제(포켓몬 번호 또는 포켓묜 이름) problem을 입력받음
5. problem을 정수형으로 변환할 때, 오류가 발생하지 않는다면 포켓몬 번호가 주어진 것,
오류가 발생한다면 포켓몬 이름이 주어진 것이므로 try-except를 이용하여 주어진 문제의
유형에 따라 서로 다른 딕셔너리를 참조하도록 구현
6. try 이하에는 오류가 없는 상황, 즉 문제가 포켓몬 번호로 주어진 상황에 대한 처리를
구현해야 하므로 num_pokemon[problem]을 출력
7. except 이하에는 오류가 발생하는 상황, 즉 문제가 포켓몬 이름으로 주어진 상황에 대한
처리를 구현해야 하므로 pokemon_num[problem]을 출력
'''
import sys
N, M=map(int, sys.stdin.readline().split())
num_pokemon={}
pokemon_num={}
for i in range(N):
    pokemon=sys.stdin.readline().strip()
    num_pokemon[i+1]=pokemon
    pokemon_num[pokemon]=i+1
for _ in range(M):
    problem=sys.stdin.readline().strip()
    try:
        problem=int(problem)
        print(num_pokemon[problem])
    except:
        print(pokemon_num[problem])

# 10816번: 숫자 카드 2
# 문제
'''
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 
구하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 
-10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 
숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
'''
# 출력
'''
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 
가지고 있는지를 공백으로 구분해 출력한다.
'''
# 해법
'''
1. N을 입력받음
2. N개의 숫자를 입력받아 리스트 cards로 저장
3. M을 입력받음
4. M개의 숫자를 입력받아 리스트 numbers로 저장
5. 빈 리스트 result를 생성
6. numbers의 각 원소별로, cards에서 그 원소의 개수를 구하여 result에 추가
7. result의 원소들을 공백 간격으로 출력
'''
import sys
N=int(sys.stdin.readline())
cards=sys.stdin.readline().split()
M=int(sys.stdin.readline())
numbers=sys.stdin.readline().split()
result=[]
for n in numbers:
    result.append(cards.count(n))
print(' '.join(map(str, result)))
# 시간 초과 발생. 효율을 더 높여야 함
'''
딕셔너리를 이용하여 연산 시간을 줄여 본다면?
'''
import sys
N=int(sys.stdin.readline())
cards=list(map(int, sys.stdin.readline().split()))
M=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split()))
result={}
for n in numbers:
    result[n]=cards.count(n)
for n in numbers:
    print(result[n], end=' ')
# 이번에도 시간 초과. 좀 더 빠른 방법은?
'''
1. result를 numbers의 각 원소를 key, 모든 value가 0인 딕셔너리로 초기화
2. cards의 각 원소 c에 대하여, 아래 try-except문을 실행
result[c]+=1을 실행
만약 위 연산이 정상적으로 실행된다면, c는 numbers에 있는 숫자
만약 위 연산에서 오류(KeyError)가 발생한다면, c는 numbers에 없는 숫자이므로 이 
숫자는 결과에 영향을 주지 않음. 따라서 아무런 작업을 할 필요가 없음
3. numbers의 각 원소 n에 대하여 result[n]의 값을 공백 간격으로 출력
'''
import sys
N=int(sys.stdin.readline())
cards=list(map(int, sys.stdin.readline().split()))
M=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split()))
result={}
for n in numbers:
    result[n]=0
for c in cards:
    try:
        result[c]+=1
    except KeyError:
        pass
for n in numbers:
    print(result[n], end=' ')

# 1764번: 듣보잡
# 문제
'''
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 
사람의 명단을 구하는 프로그램을 작성하시오.
'''
# 입력
'''
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 
N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 
주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. 
N, M은 500,000 이하의 자연수이다.
듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
'''
# 출력
'''
듣보잡의 수와 그 명단을 사전순으로 출력한다.
'''
# 해법
'''
1. N과 M을 입력받음. 듣도 못한 사람과 보도 못한 사람의 목록을 저장할 빈 집합 hear,
see를 생성
2. N개의 줄에 걸쳐 듣도 못한 사람의 이름을 입력받아 hear에 저장
3. M개의 줄에 걸쳐 보도 못한 사람의 이름을 입력받아 see에 저장
4. hear과 see의 교집합을 리스트 형태로 변환하여 result로 저장
5. result를 정렬
6. result의 길이를 출력하고, 그 다움 줄부터 result의 원소들을 한 줄에 하나씩 출력
'''
N, M=map(int, input().split())
hear=set()
see=set()
for _ in range(N):
    hear.add(input())
for _ in range(M):
    see.add(input())
result=list(hear.intersection(see))
result.sort()
print(len(result))
for r in result:
    print(r)
# 알고리즘의 효율을 높여 보자
import sys
N, M=map(int, sys.stdin.readline().split())
hear=set()
see=set()
for _ in range(N):
    hear.add(sys.stdin.readline().rstrip())
for _ in range(M):
    see.add(sys.stdin.readline().rstrip())
result=list(hear.intersection(see))
result.sort()
print(len(result))
print('\n'.join(result))

# 1269번: 대칭 차집합
# 문제
'''
자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 이때, 두 집합의 대칭 차집합의 
원소의 개수를 출력하는 프로그램을 작성하시오. 두 집합 A와 B가 있을 때, (A-B)와 (B-A)
의 합집합을 A와 B의 대칭 차집합이라고 한다.
예를 들어, A = { 1, 2, 4 } 이고, B = { 2, 3, 4, 5, 6 } 라고 할 때,  A-B = 
{ 1 } 이고, B-A = { 3, 5, 6 } 이므로, 대칭 차집합의 원소의 개수는 1 + 3 = 4개이다.
'''
# 입력
'''
첫째 줄에 집합 A의 원소의 개수와 집합 B의 원소의 개수가 빈 칸을 사이에 두고 주어진다. 
둘째 줄에는 집합 A의 모든 원소가, 셋째 줄에는 집합 B의 모든 원소가 빈 칸을 사이에 두고 
각각 주어진다. 각 집합의 원소의 개수는 200,000을 넘지 않으며, 모든 원소의 값은 
100,000,000을 넘지 않는다.
'''
# 출력
'''
첫째 줄에 대칭 차집합의 원소의 개수를 출력한다.
'''
# 해법
'''
1. N, M을 입력받음
2. N개의 원소를 갖는 집합 A를 생성
3. M개의 원소를 갖는 집합 B를 생성
4. A와 B의 대칭 차집합의 길이를 출력(symmetric_difference 함수를 사용)
'''
import sys
N, M=map(int, sys.stdin.readline().split())
A=set(sys.stdin.readline().split())
B=set(sys.stdin.readline().split())
print(len(A.symmetric_difference(B)))

# 11478번: 서로 다른 부분 문자열의 개수
# 문제
'''
문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.
부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.
예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, 
abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.
'''
# 입력
'''
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.
'''
# 출력
'''
첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.
'''
# 해법
'''
1. S를 입력받음. 부분 문자열을 저장할 빈 집합 sub을 생성
2. S의 길이를 l로 저장
3. 가능한 부분 문자열의 길이는 1부터 l까지
4. 각 부분 문자열을 sub에 삽입
5. sub의 길이를 출력
'''
S=input()
sub=set()
l=len(S)
for length in range(1, l+1):
    for i in range(l-length+1):
        sub.add(S[i:i+length])
print(len(sub))