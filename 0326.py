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
print("'{:d}'".format(515))
print("'{:5d}'".format(515))
print("'{:+5d}'".format(515))
print("'{:=+d}'".format(515))
print("'{:05d}'".format(515))
print("'{:+0d}'".format(515))

