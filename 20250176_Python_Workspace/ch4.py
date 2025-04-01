## 문자열 다루기

#########################################################
## 4.1 : 문자열이란? : 문자들의 집합

# 작은따음표 또는 큰따음표로 감싸서 표기
# - 같은 종류의 따음표를 사용
sententce1 = '나는 소년입니다.'
print(sententce1)

sententce2 = "나는 소녀입니다."
print(sententce2)

# 다른 종루의 따음표를 써서 문자열 표시하면 에러 발생
# sententce3 = "나는 어른입니다.'
# snetentce4 = '나는 어른입니다."

# type() 함수를 이용하여 자료형 확인 가능
# - sen1, sen2는 동일한 문자열 자료형
print(sententce1, type(sententce1))
print(sententce2, type(sententce2))

print("동해물과 백두산이 마르고 닳도록")
print("하느님이 보우하사 우리나라 만세")
print("무궁화 삼천리 화려강산")
print("대한사람 대한으로 길이 보전하세")

# 여러 줄에 걸쳐서 작성하는 경우
# - 같은 종류의 여는 따음표와 닫는 따음표르 각각 3개씩 넣어 앞뒤로 감싸준다.
sententce5 = """
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세
"""

print(sententce5)

# 여러 줄에 걸쳐서 한 문자열을 작성할 수 없음
# print("동해물과 백두산이 마르고 닳도록
# 만세")

print("파인" + "애플")
print("파인", "애플")

#############################################################
# 4.2 원하는 만큼 문자열 자르기 : 슬라이싱(Slicing)

# 인덱스(index) : 데이터의 순서 또는 위치
# - 0부터 시작 (주의 필요!!!)
# - 변수명 뒤에 대괄호 안에 숫자를 넣어 표시
# (형식) 변수명[인덱스]

jumin = "990229-1234567"
print("성별 식별번호 : " + jumin[7])

# 슬라이싱(slicing) : 인덱스로 자르려는 시작 위치와 끝 위치를 지정
# - 대괄호 안에 인덱스를 넣어 필요한 범위를 콜론(:)으로 구분해 표시
# (형식) 변수명[시작인덱스 : 종료인덱스] # 시작 인덱스부터 종료 인덱스 직전까지

jumin = "990229-1234567"
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4]) # 2 부터 4 직전까지 (2,3)
print("일 : " + jumin[4:6]) # 4 부터 6 직전까지 (4,5)
print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지 -> jumin[0:6]과 동일
print("주민등록번호 뒷자리 : " + jumin[7:]) # 7부터 끝까지 -> jumin[7:14]과 동일
print("주민등록번호 뒷자리(뒤에서부터) : " + jumin[-7:]) # 뒤에서 7번째 위치부터 끝까지

# 변수명[: 종료 인덱스] - 처음부터 종료 인덱스 직전까지 슬라이싱
# 변수명[시작 인덱스 :] - 시작 인덱스부터 끝까지 슬라이싱
# 변수명[:]            - 처음부터 끝까지 슬라이싱
# 뒤에서 부터 슬라이싱하려면 음수 인덱스 사용
# 음수 인덱스는 -1부터 시작

######################################################################
# 4.3. 함수로 문자열 처리하기 : 다수의 문자열 처리 함수 제공
# - (형식) 문자열(또는 변수).함수()
 
python = "Python is Amazing"

print(python.lower()) # 전체 소문자로 변환
print("Python is Amazing".lower())

print(python.upper()) # 전체 대문자로 변환

print(python[0].isupper())   # 인덱스 0에 있는 값이 대문자인지 확인 (대문자이면 True, 대문자 아니면 False)
print(python)
print(python[1:3].islower()) # 인덱스 1번부터 2번에 있는 값이 소문자인지 확인

print(python.replace("Python", "Java")) # Python을 Java로 바꾸기
print(python) # 함수를 수행한 결과값을 넘겨주고 변수에 저장되어 있는 값은 그대로 유지

find = python.find("n") # 처음 발견한 글자 "n"의 인덱스 검색
print(find) # "Python" 에서 n (인덱스 5)
find = python.find("n", find + 1) # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스 검색
print(find)
find = python.find("Java") # "Java"가 없으면 -1을 반환(출력) 한 후 프로그램 계속 수행
print(find)

idx = python.index("n") # 처음 발견한 n의 인덱스
print(idx) # "Python"에서 n (인덱스 5)
idx = python.index("n", idx + 1) # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(idx) # 'is Amazing'에서 n
idx = python.index("n", 2, 6) # 인덱스 2부터 6 직전까지 찾아 처음 발견한 n의 인덱스
print(idx) # 'thon'에서 n(인덱스 5)
# idx = python.index("Java") # Java가 없으면 오류가 발생하며 프로그램 종료
# print(idx)

print(python.count("n")) # "n"이 문자열 안에서 몇 번 나오는지 확인
print(python.count("v")) # "v"이 문자열 안에서 몇 번 나오는지 확인

print(len(python)) # python 변수에 저장된 문자열의 길이 변환

####################################################################
# 4.4. 문자열 포매팅(String Formatting)

# print() 함수에서 문자열 연결 방식
print("ab" + "ab") # 문자열 사이를 띄어쓰지 않고 연결
print("ab", "ab")  # 문자열 사이를 한 칸 띄어 연결

# 4.4.1. 서식 지정자(format specifier) 사용하기
# - 자료형을 표현하는 방법
# - % 뒤에 자료형을 나타내는 문자 표기
print("나는 %d살 입니다." % 20) # %d : 정수(decimal)
print("나는 %s을 좋아합니다" % "파이썬") # %s : 문자열(string) 
print("Apple은 %c로 시작해요." % "A") # %c : 문자(character)
print("나는 %s살입니다." % 20) # %s로도 정수값 표현 가증
print("나의 키는 %.1fcm 입니다." % 199.9) # %f : 실수(floating point)

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 값이 여러개 일때도 가능

# 4.4.2. format() 함수 사용하기
print("나는 {}살 입니다." .format(20))
print("나는 {}색과 {}색을 종아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {1}색을 좋아해요." .format("파란", "빨간"))

# {}안에 이름도 넣을 수 있음
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age=20))

# 4.4.3. f-문자열(f-string) 사용하기
# - 문자열 앞에 f를 추가하면 앞에 정의한 변수의 값을 사용할 수 있음
# - 파이썬 3.6 버전 이상에서 쓸 수 있음
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요")

#################################################################
# 4.5. 탈출 문자(Escape Character)
# - 문자열 안에서 직접 사용하기 어려운 문자를 삽입
# - 특정 동작을 수행하는 문자를 삽입

# 4.5.1. 줄바꿈 (\n)
print("백문이 불여일견 백견이 불여일타")
# SyntaxErrror 발생
# print("백문이 불여일견
# 백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타")

#4.5.2. 따음표 (\", \')
# print("저는 "정현준"입니다.")
print("저는 '정현준'입니다.")
# 또는
print('저는 "정현준"입니다.')

print("저는 \"정현준\"입니다.")
print('저는 \"정현준\"입니다.')
print("저는 \'정현준\'입니다.")
print('저는 \'정현준\'입니다.')

# 4.5.3. 역슬래시 (\\)
# print("C:\Users\User\Desktop\20250176\Python\20250176_Python_Workspace")
print("C:\\Users\\User\\Desktop\\20250176\\Python\\20250176_Python_Workspace")
print(r"C:\Users\User\Desktop\20250176\Python\20250176_Python_Workspace") # 문자열 내에 어떤 값이 있든지 무시하고 그대로 출력

# 4.5.4. 커서를 맨 앞으로 이동(\r)
print("Red Apple\rPine")

# 4.5.5. 백스페이스 : 앞 글자를 하나 삭제 (\b)
print("Redd\b Apple")

# 4.5.6. Tab키 (\t)
print("Red\tApple")
