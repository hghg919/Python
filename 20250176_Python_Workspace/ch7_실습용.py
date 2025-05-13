## 함수

##################################################
# 7.1. 함수 정의하기

# 함수(function) : 입력값에 따라 출력값이 달라지는 어떤 동작을 수행하는 것
# - 내장함수(built-in function) : 파이썬에서 특정 기능을 하도록 미리 만들어 둔 함수
#   . print(), len(), input(), ...
# - 사용자 정의 함수(user-defined function) : 개발자가 직접 만든 함수
# (함수 정의 기본형식)
# def 함수명() :
#     실행할 문장1
#     실행할 문장2
#     ...

# 7.1.1. 실습 : 은행 계좌 개설하기

# 함수 정의(definition)
#def open_account():
#    print("새로운 계좌를 개설합니다.")
#
# 앞에 정의한 open_account() 함수 호출(call)
#open_account()

# 함수명 짓기 (p.193 Note 내용 참고)

##################################################
# 7.2. 전달값과 반환값

# 함수의 3요소 : 전달값, 동작, 반환값
# - 전달값 : 함수를 호출할 때 전달하는 값
#   . 함수명 뒤에 소괄호 안에 정의
#   . 함수 본문에서는 전달값들을 활용해 동작을 수행
# - 반환값 : 함수의 동작이 끝난 뒤 호출한 곳으로 넘겨주는 값
#   . return과 함께 정의
# (형식)
# def 함수명(전달값1, 전달값2, ...) :
#     실행할 문장1
#     실행할 문장2
#     ...
#     return 반환값

# 7.2.1. 실습 : 입금하기
#def open_account():
#    print("새로운 계좌를 개설합니다.")
#
#open_account()
#
#def deposit(balance, money):
#    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
#    return balance + money
#
#balance = 0 # 초기 잔액
#balance = deposit(balance, 1000) # 1,000원 입금 
#deposit(blance, 10000) # 함수의 반환값을 사용하려면 저장할 변수에 대입해야 함

# balance 변수의 구분
# - 함수 호출 시 : 함수에 값을 전달하는 역할
# - deposit() 함수 정의
#   . 함수 호출 시 전달값을 저장하는 새로운 변수
#   . 함수 안에서만 사용할 수 있음
#   . 매개변수 (parameter)


# 7.2.2. 실습 : 출금하기
#def open_account():
#   print("새로운 계좌를 개설합니다.")
#
#open_account()
#
#def deposit(balance, money):
#   print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
#   return balance + money
#
#def withdraw(balance, money):
#   if balance >= money:
#      print("{}원을 출금했습니다. 잔액은 {}원입니다.".format(money, balance - money))
#      return balance - money
#   else:
#      print("잔액이 부족합니다. 잔액은 {}원입니다.".format(balance))
#      return balance
#   
#balance = 0
#balance = deposit(balance, 1000)
#
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
#
## 7.2.3. 실습 : 수수료 부과하기
#def withdraw_night(balacne, money):
#   commission = 100
#   print("업무 시간 외에 {}원을 출금했습니다.".format(money))
#   return commission, balacne - money - commission
#
#balance = 0
#balance = deposit(balance, 1000)
#
#commission, balance = withdraw_night(balance, 500)
#print("수수료 {}원이며, 잔액은 {}원입니다.".format(commission, balance))

(name, age, hobby) = ("피글렛", 20, "코딩")
print(name, age, hobby)

name, age, hobby = ("피글렛", 20, "코딩")
print(name, age, hobby)

name, age, hobby = "피글렛", 20, "코딩"
print(name, age, hobby)

##################################################
# 7.3. 함수 호출하기

# 7.3.1. 기본값 사용하기
# 기본값 : 함수에서 매개변수에 미리 지정해 둔 값


# 찰리와 루시가 나이도 같고 주 사용 언어도 같다면?
# - 기본값이 있으면 전달값을 일일이 적지 않아도 됨


# 기본값과 전달값 중 전달값을 우선적으로 사용    

# 전달값 작성 순서
# - 일반 전달값과 기본값이 있는 전달값을 함께 사용하는 경우
# - 반드시 일반 전달값을 먼저 적어야 함



# 7.3.2. 키워드 인자 사용하기기
# 키워드 인자(keyword argument)
# - 함수를 호출할 때 어떤 매개변수에 값을 전달할지 명시적으로 지정하는 것


# 전달하려는 값의 순서에 구매받지 않음


# 키워드 인자는 어떤 함수가 다양한 매개변수를 제공하는데 모두 기본값을 가지는 경우
# 대부분 기본값을 쓰고 일부 매개변수만 값을 지정하고자 할 때 유용


# 일반 전달값과 키워드 인자를 함께 사용해 함수를 호출할 경우
# - 반드시 일반 전달값을 순서대로 먼저 적은 후 키워드 인자를 적어야 함


# 위치 인자(positional argument)
# - 함수에서 정의된 순서대로 입력하는 전달값


# 7.3.3. 가변 인자 사용하기

# 사용할 수 있는 언어의 종류를 5개까지 입력 받도록 수정


# 사용할 수 있는 프로그래밍 언어sadfsdafasdf
# - 찰리 : 파이썬, 자바, C, C++, C#
# - 루시 : 코틀린, 스위프트



# (형식) print(출력할 내용, sep=" ", end="\n", file=None, flush=False)


# 출력해야 하는 사람이 많아지거나 사용하는 언어의 수가 더 많아지면 어떻게 해야 할까?

# 가변인자 (variable argument)
# - 개수가 변할 수 있는 인자
# - 함수에서 전달값을 받을 때 개수가 달라지는 경우에 가변 인자를 사용
# - 전달값 앞에 *를 추가
# - 전달값이 몇 개가 들어오든 묶어서 튜플로 인식
# (형식)
# def 함수명(전달값1, 전달값2, ..., *가변 인자):
#     실행할 문장1
#     실행할 문장2
#     ...
#     return 반환값



# for 반복문을 이용하여 프로그래밍 언어를 튜플 형태가 아닌 기존처럼 하나씩 출력하도록 수정

# 함수 안에서 함수 호출하기


##################################################
# 7.4. 변수의 범위 : 지역변수와 전역변수

# 영화관의 3D 안경 보관함에 3D 안경이 10개 있고 관객 2명에게 대여했을 때
# 남은 안경이 몇 개인지 구하는 프로그램

# 에러 발생 (UnboundedLocalError: local variable 'glasses' referenced before assignment)
# - glasses 변수가 아직 할당되지 않았는데 사용됐다는 에러 메시지
'''
glasses = 10 # 전체 3D 안경 개수: 10개

def rent(people): # 3D 안경을 대여한 관객 수
    glasses = glasses - people # 잔여 3D 안경 개수 = 전체 개수 - 대여한 개수 
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))

print("전체 3D 안경 개수: {0}".format(glasses))
rent(2) # 3D 안경을 대여한 관객이 2명일 때
print("남은 3D 안경 개수: {0}".format(glasses))
'''

# 지역변수 (local variable) : 함수 안에서만 사용할 수 있는 변수
# 전역변수 (global variable) : 모든 곳에서 사용할 수 있는 변수
# - global 키워드
#   : 변수 앞에 global을 붙이면 전역변수를 함수 안에서 사용하겠다는 의미

