# 슬라이싱 (원하는 부분을 가져옴 : 문자열[인덱스 n:인덱스 m] n부터 m까지(m바로 전까지))
# s = "Life is too short, You need Python."
# print(s[3:7])
# print(s[-10:-7])
# print(s[3:-10])
# print(s[-10:30])
# print(s[3:2])
# print(s[30:])

# 문자열 함수
h = "  Happy Programming  "
print(len(h))
print(h.count("p"))
print(h.upper())
print(h.lower())
print(h.strip())
print(h.replace("Happy", "Funny"))
print(h.find("ap"))
print(h.rfind("a"))
print("zoo")

h = "  Happy Programming  "
print("a" in h)
print("amp" in h)
x = "01::23::ab::&&"
y = x.split("::")
print(y)
print(", " .join(y))

