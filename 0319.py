# age= 18
# print(age)
#
# after_2 = 2
# print(age + after_2)
#
# result = age - after_2
# print(result)

# type(변수명) : 변수의 자료형을 알려줍니다.
# age = 18
# print(type(age))
#
# pi = 3.14
# print(type(pi))
#
# x = 10 + 3.14
# print(type(x))

# 진수 표현
# print(0b1100111000)
# print(type(0b1100111000))

# 지수 표현
# print(10e3)
# print(type(10e3))
# print(1.23456e-2)
# print(type(1.23456e-2))
# print(1.23456e22)

# 복소수
# print(8+24j)
# c = 1.2 + 3.4j
#
# print(type(1.2 + 3.4j))
# print(c.real)
# print(c.imag)
# print(c.conjugate())        # 켤레 복소수를 구하는 함수
#
# d = 1j
# print(d*d.conjugate())

# 변환 함수 (형변환)
# print(int('132'))
# print(int('132.0'))             # 실수인 문자형 -> 변환 과정을 2번 해야 함
# print(int('132.4'))             # 변환 과정을 2번 해야 함
# print(float('132.0'))
# print(float('132.4'))
# print(float('132'))

# 문자열 다루기
greeting = 'Hello'
to = "world!"
print(greeting)
print(type(greeting))

say_hello = greeting + ", " + to
print(say_hello)

print("Hello" * 5)
print("\"Hello\"\n" + to)
print('"Hello"\n' + to)

multiline = """Happy
Programming"""
print(multiline)