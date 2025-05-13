## 제어문

################################################## clear -> 터미널 청소 # 나는 말하는 오이입니다. 저는 말하는 감자입니다.
# 6.1. 조건에 따라 분기하기: 조건문

# 6.1.1. 조건이 하나일 때: if 문
# - 코드에서 조건에 따른 분기가 필요할 때 사용
# - if 조건이 참일 때 실행할 명령들은 들여쓰기를 해서 구분
# (형식) p.162
# weather = "비"

# 비교연산자
# -, ==, >, <, >=, <=, != : 비교 결과는 True, False
# if weather == "비": # 대입 연산자(=)가 아닌 비교 연산자(==) 사용
#     print("우산을 챙기세요.")

# 콜론과 들여쓰기의 중요성 (p.162 Note 읽어보기)

# 6.1.2. 조건이 여러 개일 때: elif 문
# - 코드에서 분기 조건이 여러 개일 때 사용
# - if 문에 이어서 elif 문은 여러 번 사용 가능
# (형식) p.164
# weather = "미세먼지"
# 
# if weather == "비": # 조건1
#     print("우산을 챙기세요.")  # 조건 1번의 실행코드
# elif weather == "미세먼지":   # 조건2
#     print("마스크를 챙기세요") # 조건 2번의 실행코드

# 6.1.3. 모든 조건이 맞지 않을 때: else 문
# - if 문과 elif 문의 조건에 모두 해당하지 않을 때 실행할 명령을 정의
# - else 문은 생략 가능
# (형식) p.165
# weather = "맑음"
# 
# if weather == "비":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요.\n")

# 6.1.4. input()으로 값 입력받아 비교하기
# - input() 함수 : 프로그램을 실행했을 때 사용자로부터 어떤 값을 입력받는 용도로 사용
#   . 숫자를 입력해도 문자열로 인식
#   . 값을 비교하고나 계산해야 한다면 숫자 자료형으로 형변환해야 함
# weather = input("오늘 날씨는 어때요? ")
# print(weather) 

# if weather == "비":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요.\n")

# 하나의 명령에 대해서 조건을 여러개 나열해야 하는 경우

# if (weather == "비") or (weather == "눈"): # 괄호가 연산자 중 가장 먼저 계산 // 비교 -> 논리
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요.")

# temp = int(input("오늘 기온은 어때요? ")) # 입력값을 정수형으로 형변환
# if 30 <= temp: # 30도 이상이면
#if temp >= 30:
#    print("너무 더워요. 외출을 자제하세요.")
# elif 10 <= temp and temp < 30: # 10도 이상 30도 미만이면
# elif 10 <= temp < 30:
#elif temp >= 10:
#    print("활동하기 좋은 날씨예요.")
# elif 0 <= temp and temp < 10: # 0도 이상 10도 미만이면
# elif 0 <= temp < 10:
#elif temp >= 0:
#    print("외투를 챙기세요.")
#else: # 그 외의 모든 경우(0도 미만이면)
#    print("너무 추워요. 나가지 마세요.")

# 숫자 중 소수점으로 변환하고 싶으면? --> float() 함수 사용
# pi_val = float(input("파이를 소수점 두자리로 표현하면?"))
# print(pi_val, type(pi_val))

# input() 함수에서 여러 개의 값을 입력 받을 수 있음
# year, month, day = input("오늘은 몇년 몇월 몇일인가요?").split()
# year = int(year)
# month = int(month)
# day = int(day)
# 
# print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))

##################################################
# 6.2. 같은 일 반복하기: 반복문

# 6.2.1. 범위 안에서 반복하기: for 문
# - 같은 동작을 여러 번 반복해서 수행할 때 사용
# - 보통 반복 대상에 정해진 만큼 반복
# (형식) p.172
# for waiting_no in[1,2,3,4,5]:
#     print("대기번호 : {0}".format(waiting_no)) # {0}의 위치에 waiting_no의 값이 들어감

# 지정한 범위 안에서 연속한 정수를 사용하고 싶으면? --> range() 함수
# (형식) p.173
# range(5) ==> [0,1,2,3,4]

# 1) range(숫자) : 0부터 n-1 까지의 연속한 정수
# [0,1,2,4, ......, n-1]
# for waiting_no in range(5):
#     print("대기번호 : {0}".format(waiting_no))
# 
# # 2) range(start, end) : start부터 end-1까지의 연속한 정수    
# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))
# 
# # 3) range(start, end, gap) : start부터 end-1까지의 gap씩 건너뛰며 연속한 정수 
# for waiting_no in range(1,6,2):
#     print("대기번호 : {0}".format(waiting_no))
# 
# orders = ["아이언맨", "토르", "스파이더맨"] # 손님 닉네임 리스트
# for customer in orders:
#     print("{0} 님, 커피가 준비됐습니다. 픽업대로 와 주세요.".format(customer))

# 6.2.2. 조건을 만족할 동안 반복하기: while 문
# - 같은 동작을 여러 번 반복해서 수행하기 위해 사용
# (형식) p.175
# - 보통 주어진 조건을 만족하는 동안 끝없이 반복
# customer = "토르" # 손님 닉네임
# index = 5 # 초깃값, 부르는 횟수 최대 5번
# 
# while index >= 1: # 부르는 횟수가 1 이상일 때만 실행
#     print("{} 님, 커피가 준비됐습니다.".format(customer))
#     index -= 1 # 횟수 1회 차감
#     print("{}번 남았어요".format(index))
#     if index == 0: # 5번 모두 불렀다면
#         print("커피를 폐기 처분합니다.")

# 무한 루프(infinite loop)
#  - while 문을 끝없이 반복 수행 하는 것
#  - 이럴 때에는 프로그램을 강제 종료해야 함 (실행 중 Ctrl + C)
# customer = "아이언맨"
# index = 1
# 
# while True:
    # print("{0} 님, 커피가 준비됐습니다. 호출{1}회".format(customer,index))
    # index += 1

# input() 함수와의 연동 (사용자의 입력에 따른 조건 처리)
# customer = "토르"
# person = None # None : 아무것도 없다는 의미
# 
# while person != customer :
    # print("{}님, 커피가 준비됐습니다.".format(customer))
    # person = input("이름이 어떻게 되세요?")

# 6.2.3. 흐름 제어하기 : continue와 break

# continue
# - 반복문에서 해당 반복을 건너뛰고 다음 반복으로 넘어가기 위해 사용
# - continue를 만나면 이후 문장들은 실행하지 않고 다음 반복으로 넘어감
# absent = [2, 5] # 결석한 학생 출석번호
# 
# for student in range(1,11): # 출석번호 1 ~ 10번
#     if student in absent: # 결석한 학생이면
#         continue # 다음 학생으로 넘어가기
#     print("{0}번 학생, 책을 읽어보세요.".format(student))

# break
# - 반복문을 탈출할 때 사용
# - break를 만나면 이후 문장들은 실행하지 않고 즉시 반복문을 빠져나옴
# absent = [2, 5] # 결석한 학생 출석번호
# no_book = [7] # 책을 가져오지 않은 학생 출석번호호
# 
# for student in range(1,11): # 출석번호 1 ~ 10번
#     if student in absent: # 결석한 학생이면
#         continue # 다음 학생으로 넘어가기
#     elif student in no_book: # 책을 가져오지 않으면 바로 수업 종료
#         print("오늘 수업은 여기까지. {}번 학생은 교무실로 따라와요.".format(student))
#         break # 반복문 탈출
#     print("{0}번 학생, 책을 읽어보세요.".format(student))

# 6.2.4. for 문 한 줄로 작성하기
# - 한 줄 for 문(리스트 컴프리헨션, list comprehension)
#  . 반복 대상의 값들에 각각 어떤 동작을 수행하고, 수행한 결과들을 모아 새로운 리스트를 만드는 것
#  (형식) p.180
students = [1,2,3,4,5]
print(students)

# 한 줄 for 문으로 각 항목에 100 더하기
students = [i + 100 for i in students]
print(students)

# 한 줄 for 문 작성 시 주의할 점
# p.182 Note 참고
students = ["Iron man", "Thor", "Sipder Man"]
print(students)

# 한 줄 for 문으로 각 이름을 이름의 길이 정보로 변환
students = [len(i) for i in students]
print(students)

# 한 줄 for 문으로 각 이름을 모두 대문자로 변경
students = ["Iron man", "Thor", "Sipder Man"]
students = [i.upper() for i in students]
print(students)