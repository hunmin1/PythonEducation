# -*- coding: utf-8 -*-

prompt = """
0. exit
"""
number=1
while(number != 0):
	print(prompt)
	try:
		print("숫자입력 :",end=" ")
		number=int(input())
	except ValueError:
		print("숫자만 입력하세요!")
		