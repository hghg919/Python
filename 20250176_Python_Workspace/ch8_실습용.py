## 입출력

################################################################
# 8.1. 표준 입력받기: input()

# 표준 입력 : 표준 입력 장치인 키보드로 값을 입력받는 것
# - input() : 사용자로부터 어떤 값을 입력받는 용도로 사용하는 표준 입력 함수

#answer = input("아무 값이나 입력하세요 : ")
#print("입력한 값은 " + answer + "입니다.")
#
## 입력값은 항상 문자열을 인식!!!
#print(type(answer))
#
## 숫자를 입력받아 연산하려는 경우에는 형변환해야 함
#print(type(int(answer)))
#answer = 10
#print(type(answer))

# 여러개의 값을 동시에 입력받을 때
#num1, num2 = input("두 개의 숫자를 입력하세요 : ").split(" ")
#
#num1 = int(num1)
#num2 = int(num2)
#print("두 숫자의 합은 : ", num1 + num2)


###################################################################################
# 8.2. 표준 출력 시 유용한 기능

# 표준 출력 : 기본 출력 장치를 통해 프로그램을 수행한 결과를 사용자에게 보여주는 것 (예: VSCode 터미널)
# - print() : 어떤 값을 출력하는 용도로 사용하는 표준 출력 함수

# 8.2.1. 구분자 넣기: sep
# - 여러 데이터를 지정한 값으로 구분

#print("파이썬", "자바") # 한 칸 띄우고 문자열을 합침
#print("파이썬" + "자바") # 띄어쓰기 없이 문자열을 합침

# 값을 쉼표로 구분
#print("파이썬", "자바", sep=",")

# 값을 ' vs '로 구분
#print("파이썬", "자바", "자바스크립트", sep=" vs ")

# 8.2.2. 문장 끝 지정하기: end
# - 문장 끝을 줄바꿈 대신 지정한 값으로 출력

# 줄바꿈 없이 "? "를 출력하고 다음 출력내용을 기다림
#print("파이썬", "자바", sep=", ", end="? ")
#print("무엇이 더 재미있을까요?")

# 기본값은 줄바꿈을 하고 다음 출력내용을 기다림
#print("파이썬", "자바", sep=", ")
#print("무엇이 더 재미있을까요?")


# 8.2.3. 출력 위치 지정하기: file
# - 출력 대상을 지정 (print() 문의 실행결과를 어디에 출력할지 지정)
#import sys # sys 모듈을 가져와서 사용하겠다는 의미

# 표준 출력에 결과를 출력
#print("파이썬", "자바", file=sys.stdout)
# 표준 오류에 결과를 출력 (오류가 발생했을 때 터미널에 오류 메시지를 출력하라는 의미)
#print("파이썬", "자바", file=sys.stderr)

# 8.2.4. 공간 확보해 정렬하기: ljust()와 rjust()
# - ljust() : 미리 공간을 확보하고 왼쪽 정렬로 출력
# - rjust() : 미리 공간을 확보하고 오른쪽 정렬로 출력

# 3과목에 대한 성적 정보를 출력하는 예제 (동작원리는 p.230 그림 참고)
#scores = {"수학": 0, "영어": 50, "파이썬 코딩": 100} # 딕셔너리 자료구조
#
#for subject, score in scores.items(): # (key, value)
#    print(subject, score)

# ljust(), rjust() 함수로 정렬해서 깔끔하게 출력 (동작원리는 p.231 그림 참고)
#scores = {"수학": 0, "영어": 50, "코딩": 100}
#
#for subject, score in scores.items(): # (key, value)
#    print(subject.ljust(8), str(score).rjust(4), sep=":")


# 8.2.5. 빈칸 0으로 채우기: zfill()
# - zfill() : 미리 공간을 확보하고 빈칸을 0으로 채움 (동작원리는 p.232 그림 참고)

#for num in range(1, 21): # 1~20의 숫자
#    print("대기번호 : " + str(num))

# 은행의 대기번호처럼 3자리로 표시하고 자릿값이 비어 있을 때는 0으로 채워 넣음
#for num in range(1, 21): # 1~20의 숫자
#    print("대기번호 : " + str(num).zfill(3))


##################################################
# 8.3. 다양한 형식으로 출력하기: format()
# - 원하는 형태의 출력 포맷을 지정하는 용도로 사용용

# {0} 위치에 값 500 출력
#print("{0}".format(500))

# 빈칸으로 두기, 오른쪽 정렬, 공간 10칸 확보 (동작원리는 p.234 그림 참고)
#print("{0: >10}".format(500))

# 빈칸으로 두기, 오른쪽 정렬, + 기호 붙이기, 공간 10칸 확보 (동작원리는 p.235 그림 참고)
#print("{0: >+10}".format(500))
#print("{0: >+10}".format(-500))

# 빈칸을 _로 채우기, 왼쪽 정렬, 공간 10칸 확보 (동작원리는 p.235 그림 참고)
#print("{0:_<10}".format(500))

# 큰 수를 확인하기 쉽도록 3자리마다 쉽표 표시
#print("{0:,}".format(100000000000)) # 3자리마다 쉼표 찍기
#print("{0:+,}".format(100000000000))
#print("{0:+,}".format(-100000000000))

# 빈칸을 ^로 채우기, 왼쪽 정렬, + 기호 붙이기, 공간 30칸 확보, 3자리마다 쉼표 찍기
#print("{0:^<+30,}".format(100000000000))

# 소수점을 포함하는 실수 출력
#print("{0}".format(5 / 3))
#print("{0:f}".format(5 / 3))
#print("{0:.2f}".format(5 / 3))

# 출력 형식 정리 (p.237 형식 참고)


##################################################
# 8.4. 파일 입출력

# 8.4.1. 파일 열고 닫기: open(), close()
# (형식) open("파일명", "모드", encoding="인코딩 형식")
# - 파일 열기 모드 (p.238 표 8-1 참고)
# - 모든 파일은 열고 나면 반드시 닫아줘야 함 (close() 함수)
#score_file = open("score.txt", "w", encoding="utf8")
#print("수학 : 0", file=score_file)
#print("영어 : 50", file=score_file)
## 주의! : 파일을 열고 나면 항상 마지막에 파일을 닫아줘야 함
# score_file.close() # score.txt 파일 닫기

# 8.4.2. 파일 쓰기: write()
#score_file = open("score.txt", "a", encoding="utf8")
# write() 함수는 줄바꿈을 해주지 않으므로 \n을 마지막에 추가
#score_file.write("과학 : 80\n")
#score_file.write("코딩 : 100\n")
#score_file.close()

# 8.4.3. 파일 읽기: read(), readline(), readlines()

# (1) read() : 파일 내용을 한꺼번에 읽어 오기
#score_file = open("score.txt", "r", encoding="utf8")
#print(score_file.read())
#score_file.close()

# (2) readline() : 파일 내용을 한 줄씩 읽어 오기

# readline()을 4번 반복해서 내용 출력
# - 대부분은 파일을 열어 보기 전까지 총 몇 줄인지 알 수가 없음
#   ==> while 문 사용
# score_file = open("score.txt", "r", encoding="utf8") # score.txt 파일을 읽기 모드로 열기
# print(score_file.readline(), end="") # 한 줄씩 읽어 오고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # end 값을 설정해 줄 바꿈 중복 수행 방지
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# while 반복문을 사용한 파일 내용 한 줄씩 읽어 오기
#score_file = open("score.txt", "r", encoding="utf8")
#
#while True:
#    line = score_file.readline()
#    if not line:
#        break
#    print(line, end="")
#
#score_file.close()

# (3) readlines() : 파일 내용을 줄 단위로 나뉜 리스트 형태로 한꺼번에 읽어 오기
# score_file = open("score.txt", "r", encoding="utf8")
# 
# lines = score_file.readlines()
# for line in lines:
#    print(line, end="")
# 
# score_file.close()

##################################################
# 8.5. 데이터를 파일로 저장하기: pickle 모듈
# - pickle : 프로그램에서 작업하던 데이터를 파일에 저장하거나, 저장된 데이터를 불러올 때 사용하는 모듈
#  . dump() 함수 : 데이터를 파일로 저장할 때 사용하는 함수
#    (형식) dump(저장할 데이터, 저장할 파일명)
#  . load() 함수 : 파일에서 데이터를 불러올 때 사용하는 함수
#    (형식) load(불러올 파일명)

# pickle 모듈로 저장하는 파일은 바이너리(binary) 형태 (p.245 표 8-3 파일형태에 따른 파일 열기 모드 참고)
# - 텍스트 파일: 사람이 읽을 수 있는 글자(한글, 영어, 숫자 등)로 이루어진 파일로, 보통 txt 형식으로 저장
# - 바이너리 파일: 컴퓨터가 인식할 수 있는 이진수(0과 1)로 이루어진 파일로, JPG, PNG 같은 이미지 파일, MP3와 같은 음악 파일, EXE와 같은 실행 파일 등이 해당

# pickle 모듈 가져다 쓰기
#import pickle

# 바이너리 형태로 쓰고 저정하는 코드
#profile_file = open("profile.pickle", "wb")
#profile = {"이름" : "스누피", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
#print(profile)
#
#pickle.dump(profile, profile_file) # profile 데이터를 파일에 저장
#profile_file.close()
#
## 바이너리 형태로 저장된 파일에서 내용 읽어오기
#profile_file = open("profile.pickle", "rb")
#profile = pickle.load(profile_file)
#
#print(profile)
#profile_file.close()

##################################################
# 8.6. 파일 한 번에 열고 닫기: with 문
# : with문을 사용하면 파일을 열고 나서 close() 함수를 호출하지 않아도 자동으로 파일을 닫아줌
# : with문을 사용하면 파일을 읽고 쓰는 코드가 간결해짐
# : 매번 close() 함수를 호출해야 하는 부담도 줄어들어서 좀 더 간단하게 파일 관련 작업 할 수 있음

# (형식) with 작업 as 변수명:
#            실행할 명령1
#            실행할 명령2
#            ...

# pickle 모듈로 "profile.pickle" 파일에 썼던 내용 읽기를 with문으로 작성
#import pickle
#
#with open("profile.pickle", "rb") as profile_file:
#    print(pickle.load(profile_file))

# "study.txt" 파일에 내용을 읽고 쓰기를 with문으로 작성
#import pickle
#
#with open("study.txt", "w", encoding="utf8") as study_file:
#    study_file.write("파이썬을 열심히 공부하고 있어요.")
#
#with open("study.txt", "r", encoding="utf8") as study_file:
#    print(study_file.read())    