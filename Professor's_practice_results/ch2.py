## 자료형 : 데이터의 형태

########################################################
## 2.1. 숫자(number) 자료형 : 정수(integer) 또는 실수(float)로 이루어진 자료형
# 출력 방법 : 별도 표시 없이 소괄호(()) 안에 값을 그대로 넣기
print(5)
print(-10)
print(3.14)
print(1000)

# 수식도 출력 가능
# 주의할 점 : 연산 기호 사용 시 곱하기 연산은 *, 나누기 연산은 / 사용
# - 숫자와 연산 기호 사이에 공백은 출력에 영향을 미치지 않음
# - 나누기 연산의 결과는 실수

#print(5 + 3)
print(5+3)
print(2 * 8)
print(6 / 3)
print(3 * (3 + 1))

# 파이썬은 대소문자를 구분함
print(10)
#Print(10)

# 세미콜론(;)을 이용하여 한 줄에 여러 표현식을 작성할 수 있음
print(2); print(3)

# print() 명령은 내용 출력 후 줄바꿈해서 다음 명령의 내용은 다음 줄에 출력

# print() 명령과 콤마(,)
# 출력하는 내용을 콤마로 분리해서 전달하면 값들 사이에 공백 문자(' ')로 분리
print(2, 3)

########################################################
## 2.2. 문자열(string) 자료형 : 문자로 이루어진 자료형
# 출력 방법 : 작은 따옴표(')나 큰 따옴표(")로 감싸야 한다.
print('hello world')
print("hello world")

# 작은 따옴표와 큰 따옴표는 혼용해서 쓰면 안됨
# print('hello world")
# print("hello world')

# 문자열일까요? 숫자일까요? ==> 문자열입니다.
print("10")

# type() : 입력되는 값의 자료형을 출력해주는 명령
print(type("10"))


########################################################
## 2.3. 불(boolean) 자료형 : 참을 의미하는 True와 거짓을 의마하는 False만 값으로 가지는 자료형
# - 값 : True(1), False(0)

print(5 > 10) # False
print(5 < 10) # True

# not 연산자 : 값을 부정하는 연산자 (3장에서 다룸)
print(True)
print(False)

print(not True)
print(not False)

print(not (5 > 10)) # True

########################################################
## 2.4 변수(variable) : 어떤 값을 저장하는 공간

# 2.4.1 변수 정의하기
# - 변수를 만들고
# - 값을 대입해 저장
print("반려동물을 소개해 주세요.")
print("우리집 반려동물은 개인데, 이름이 연탄이에요")
print("연탄이는 4살이고, 산책을 아주 좋아해요.")
print("연탄이는 수컷인가요?")
print("네.")

# 다른 친구의 반려동물 소개
print("반려동물을 소개해 주세요.")
print("우리집 반려동물은 개인데, 이름이 해피에요")
print("해피는 4살이고, 산책을 아주 좋아해요.")
print("연탄이는 수컷인가요?")
print("네.")

# 위 코드의 문제는 무엇일까요?
# => 반려동물의 이름이 변경(연탄이 -> 해피)되면 해당 되는 부분의 글자를 변경해야 함

# 변수에 값을 저장할 때 변수명을 먼저 적고 등호(=)로 값을 대입
# - 대입 연산자 : 파이썬에서는 등호(=)를 "값을 대입(할당)한다"는 의미로 사용
# - 대입 연산자의 좌측에는 값이 올 수 없음

# (형식) 변수명 = 값
name = "연탄이"
animal = "개"
age = 4
hobby = "산책"
is_male = True

# 변수명 짓기 : 저장하는 값이 무엇인지 알기 쉽게 짓는 것이 좋다.
# - a, b, c, x, y, z, ... 지양

# 변수명 규칙(naming convention)
# - 변수명에는 소문자(a - z), 대문자(A - Z), 숫자(0 - 9), 언더바(_)를 사용한다.
# - 변수명은 대소문자를 구분한다.
# - 변수명은 숫자로 시작할 수 없고, 소문자, 대문자, 언더바로 시작할 수 있다.
# - 키워드는 변수명으로 사용할 수 없다.

# 2.4.2. 변수 사용하기
name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

print("반려동물을 소개해 주세요.")
print("우리집 반려동물은 " + animal + "인데, 이름이 " + name + "이에요")
#print("우리집 반려동물은 개인데, 이름이 연탄이에요")
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")
#print(name + "는 " + age + "살이고, " + hobby + "을 아주 좋아해요.") # 서로 다른 자료형은 + 로 연결할 수 없음
#print("연탄이는 4살이고, 산책을 아주 좋아해요.")

# 친구네 반려동물 소개
name = "해피"
animal = "고양이"
age = 2
hobby = "낮잠"

print("반려동물을 소개해 주세요.")
print("우리집 반려동물은 " + animal + "인데, 이름이 " + name + "이에요")
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")

## 쉼표 연결과 + 연산자 연결의 차이점
name = "해피"
animal = "고양이"
age = 2
hobby = "낮잠"

# + 연산자 이용
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")
# 쉼표 이용
# - 형변환하지 않아도 된다.
# - 값과 값 사이에 공백을 포함한다.
print(name, "는 ", age, "살이고, ", hobby, "을 아주 좋아해요.")

# 2.4.3. 형변환하기 (Type Casting)
# 의미 : 값의 자료형을 다른 형태로 바꾸는 것
# 명령어 : 소괄호 안에 바꾸길 원하는 값을 넣음
# - str() : 문자열로 형변환
# - int() : 정수형으로 형변환
# - float() : 실수형으로 형변환

print(3); print(type(3)) # 숫자
print("3"); print(type("3")) # 문자열

print(int("3")) # 문자열 "3"을 숫자로 형변환
# print(int("3") + "입니다.") # TypeError 발생
print(int(3.5)) # 실수를 정수로 변경
# print(int("삼")) # ValueError 발생

print(float("3.5"))
print(float(3))

# print(float("오")) # ValueError 발생

print(str(3) + "입니다.")
print(str(3.5) + "입니다.")

# 2.4.4. 변수를 사용할 때 유의할 점

# 1. 변수는 사용하기 전에 정의한다.
animal = "고양이"
age = 2
hobby = "낮잠"

print("반려동물을 소개해 주세요.")
print("우리집 반려동물은 " + animal + "인데, 이름이 " + name + "이에요") # name 변수가 앞에서 정의되지 않았기 때문에 에러 발생
name = "해피"
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")

# 2. 변수는 사용하기 전에 마지막으로 저장한 값을 사용한다.
name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

print("반려동물을 소개해 주세요.")
print("우리집 반려동물은 " + animal + "인데, 이름이 " + name + "이에요") # name 변수가 앞에서 정의되지 않았기 때문에 에러 발생
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")

# 2.5. 주석, 설명문 (comment)
# 주석(comment): 코드에서 실행하지 않도록, 즉 무시하도록 처리하는 것
# 코드에 설명을 추가해야 하거나 일시적으로 실행되지 않길 원하는 부분이 있을 때 사용한다.
# 한 줄을 주석 처리할 때: #(샤프, sharp)

# print("반려동물을 소개해 주세요.")
print("반려동물을 소개해 주세요.") # 설명문문


# 여러 줄을 주석 처리할 때: 따옴표(작은따옴표 또는 큰따옴표) 3개
'''
print("반려동물을 소개해 주세요.")
print("우리집 반려동물은 " + animal + "인데, 이름이 " + name + "이에요") # name 변수가 앞에서 정의되지 않았기 때문에 에러 발생
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")'
'''

"""
print("반려동물을 소개해 주세요.")
print("우리집 반려동물은 " + animal + "인데, 이름이 " + name + "이에요") # name 변수가 앞에서 정의되지 않았기 때문에 에러 발생
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")'
"""

# 변수의 자료형은 고정되어 있는 것이 아니라 값이 들어갈때 값의 자료형으로 설정된다.
name = "연탄이"
name = "해피"
name = 100
print(name)