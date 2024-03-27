# 슬라이싱 (원하는 부분을 가져옴 : 문자열[인덱스 n:인덱스 m] n부터 m까지(m바로 전까지))
# s = "Life is too short, You need Python."
# print(s[3:7])
# print(s[-10:-7])
# print(s[3:-10])
# print(s[-10:30])
# print(s[3:2])
# print(s[30:])

# 문자열 함수
# h = "  Happy Programming  "
# print(len(h))
# print(h.count("p"))
# print(h.upper())
# print(h.lower())
# print(h.strip())
# print(h.replace("Happy", "Funny"))
# print(h.find("ap"))
# print(h.rfind("a"))
# print("zoo")
#
# h = "  Happy Programming  "
# print("a" in h)
# print("amp" in h)
# x = "01::23::ab::&&"
# y = x.split("::")
# print(y)
# print(", " .join(y))

# format : 문자열 형식을 미리 정하고, 인자를 주어 문자열을 완성함
# s = "name: {}, mumber: {}, soccer: {}"
# print(s.format("Ronaldo", 7, True))
# print("name: {name}, number: {num},".format(name = "Jordan", num=23))

# 포맷 정수 표현
# print("'{:d}'".format(515))
# print("'{:5d}'".format(515))
# print("'{:+5d}'".format(515))
# print("'{:=+d}'".format(515))
# print("'{:05d}'".format(515))
# print("'{:+0d}'".format(515))

# 포맷 실수 표현
# print("'{:f}'".format(11.17))
# print("'{:12f}'".format(11.17))
# print("'{:12.1f}'".format(11.17))

# 혼자 해보기
# print("{:=+6.1f}".format(11.17))

# 리스트 : [], 튜플 : (), 딕셔너리 : {키:값, 키:값}, {값, 값}
# 리스트 생성
# l : []
# player = ["Messi", 10, True]
# print(list("happy"))
# print(list((1125, 2436)))
# print(list({"menu":"pizza","price":10000}))
# print(list({"사과", "배"}))
# nums = list(range(3))

# 리스트에 요소 추가
nums = list(range(3))
print(nums+[10, 11])
nums += [10, 11]
print(nums)
nums.append(20)
print(nums)
nums.append([30, 31])
print(nums)
nums.insert(2, 40)
print(nums)
nums.extend([50, 51])
print(nums)

