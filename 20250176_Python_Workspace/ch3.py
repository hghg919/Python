print("Hello World!")

## 연산자(operator) : 프로그래밍에서 연산을 할 때 사용하는 기호

##############################################################
## 3.1 : 연산자의 종류
# - 산술, 대입, 비교, 논리, 비트 연산자 등... 

# 3.1.1. 산술 연산자
# - 덧셈, 뺄셈, 곱셈, 나눗셈 등 수를 연산하는데 사용
print(2 + 3) # 덧셈
print(4 - 1) # 빼기
print(5 * 2) # 곱하기
print(6 / 3) # 나누기 (결과의 자료형 : 실수)

print(2 ** 3) # 거듭제곱
print(10 % 3) # 나눈 나머지 (modular operator)
print(10 // 3) # 나눈 몫

# 3.1.2. 비교 연산자
# - 값의 크기를 비교할 때 사용 (등호, 부동호를 기호로 사용)
# - 비교 연산자의 결과는 항상 True, False 중 하나

print(10 > 3) # 크다
print(4 >= 7) # 크거나 같다
# print(4 >= 7) # 크거나 같다 (허용 X)
# print(4 > = 7) # 기호 사이에 공백이 들어가면 안됨

print(10 < 3) # 작다
print(5 <= 5) # 작거나 같다

print(3 == 3) # 같다
# print(3 = 3)  # 대입 연산자이기 때문에 좌측에 값을 넣을 수 없다.

print(4 == 2)
print(3 + 4 == 7)
print(1 != 3) # 다르다

# 3.1.3 논리 연산자
# - 수식, 조건 등에서 값이 참인지 거짓인지 판단할 때 사용
# - 논리 연산자의 결과는 항상 True, False 중 하나

print((3 > 0) and (3 > 5)) # True and False ==> False
print((3 > 0) or (3 > 5)) # True or False ==> True
print(not(1 != 3))

# 논리 연산자를 연달아 사용하는 것도 가능
print(5 > 4 > 3) # 5 > 4 and 4 > 3
print(4 > 5 > 3) # 4 > 5 and 5 > 3

###############################################################################
## 3.2 : 연산자의 우선순위
# - 연산자에는 우선순위가 있어서 수식을 어떻게 작성하느냐에 따라 연산 순서가 달라짐

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

################################################################################
## 3.3 : 변수로 연산하기
# - 연산을 쉽게 하기 위해 변수에 연산 결과를 저장한 뒤 새로운 연산에 활용

number = 2 + 3 + 4 # 더하기 연산을 모두 완료한 후 number 변수에 대입
print(number)
number = number + 2 # 2 + 3 + 4 + 2
print(number)

# - 복합 대입 연산자(augmented assignment operator) : 대입 연산자와 산술 연산자를 합친 것
# - 복합 대입 연산자를 사용하면 더욱 간소한 형태로 연산 가능

number = 2 + 3 + 4 # 더하기 연산을 모두 완료한 후 number 변수에 대입
print(number)
# number = number + 2 # 2 + 3 + 4 + 2
# print(number)
number += 2 # number = number + 2와 동일
print(number)
number -= 2 # number = number - 2와 동일
print(number)
number *= 2 # number = number * 2와 동일
print(number)
number /= 2 # number = number / 2와 동일
print(number)
number **= 2 # number = number ** 2와 동일
print(number)
number //= 2 # number = number // 2와 동일
print(number)
number %= 2 # number = number % 2와 동일
print(number)

###################################################################
## 3.4 : 함수로 연산하기

# 3.4.1. 숫자 처리 함수
# - 파이썬에서는 다양한 연산을 편리하게 할 수 있도록 여러가지 함수를 제공ㄴ

print(abs(-5))         # -5의 절대값을 출력
print(pow(4, 2))       # 4를 제곱한 값을 출력
print(max(5, 12))      # 5와 12 중 큰 값을 출력
print(min(5, 12))      # 5와 12 중 작은 값을 출력
print(round(3.14))     # 3.14를 소수점 이하 첫째 자리에서 반올림 한 정수룰 출력
print(round(4.678, 2)) # 4.678을 소수점 이하 셋째 자리에서 반올림한 정수를 출력

# 3.4.2. math 모듈 : 숫자 연산을 수행하는 함수들이 들어 있는 곳
# - 모듈(module) : 어떤 기능을 하는 코드를 모아 놓은 파이썬 파일

# (형식) from 모듈명 import 기능
from math import * # math 모듈의 모든 기능을 가져다 쓰겠다는 의미

# floor, round, ceil : 내림, 반올림, 올림
result = floor(4.99)
print(result) # 4.99의 내림한 값
result = round(4.99)
print(result) # 4.99의 반올림한 값
result = ceil(3.14)
print(result) # 3.14의 올림한 값

# sqrt (square root) : 제곱근
result = sqrt(16) # 16의 제곱근
print(result)

# (형식) import 모듈명
# - 이 방법은 기능(함수) 앞에 기능이 속한 모듈 명을 점(.)으로 연결해서 적어야 함
import math # math 모듈의 기능을 가져다 쓰겠다
result = math.floor(4.99)
print(result)
result = math.ceil(3.14)
print(result)
result = math.sqrt(16)
print(result)

# 3.4.3. random 모듈 : 난수가 필요한 경우에 사용하는 함수 포함
from random import * # random 모듈의 모든 기능을 가져다 쓰겠다는 의미

# 실행 결과 : 0 이상 1 미만 사이의 수를 출력. 실행할 때마다 매번 다른 수 출력
print(random())
print(random())
print(random())

### 형변환
# - int() : 입력값을 정수로 변환
# - float() : 입력값을 실수로 변환
# - str() : 입력값을 문자로 변환
print(int("3"))
print(float("3.14"))
print(str(4))

print(random() * 10)
print(int(random() * 10)) # 0부터 9사이의 난수를 출력
print(int(random() * 10) + 1) # 1부터 10사이의 난수를 출력

# 로또 번호 생성(1부터 45사이의 난수 출력)
print(int(random() * 45) + 1)

# 원하는 범위 내에서 난수를 뽑을 수 있는 함수들
# - randrange(a, b) : a 이상 b 미만에서 난수 생성
# - randint(a, b) : a 이상 b 이하에서 난수 생성
print(randrange(1, 46))
print(randint(1, 45))

#이번주 로또 번호
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))