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