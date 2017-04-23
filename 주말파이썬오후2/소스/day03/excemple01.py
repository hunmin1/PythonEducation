
print("문제1")
for i in range(1,6):
	for j in range(0,i):
		print("*",end="")
	print("")
#구구단
print("문제2")
print("숫자를 입력하시오 : ",end="")

c = int(input())
for i in range(c,c+1):
	for j in range(1,10):
		print("%d * %d = %d" % (i,j,i*j))

#패스워드
print("문제3")
PASS=0
count = 0
Logined = False

while True:
	if count == 3:
		print("3회 초과!! 로그인 실패!")
		break
	print("패스워드 입력 : ",end="")
	try:
		PASS=int(input())
	except ValueError:
		print("잘못된 입력(숫자만입력)")
		continue
	if PASS==123123:
		print("login success!")
		Logined = True
		break
	else:
		count+=1
		print("pass가 다릅니다. %d회 누적" % count)

if(Logined):
	select = 0
	print("당신은 로그인상태입니다.")
	prom = """	1.aa
	2.bb
	3.cc
	4.dd
	5.exit"""
	while True:
		print(prom)
		print("입력 : ",end="")
		try:
			select=int(input())
		except ValueError:
			print("잘못된입력(숫자만입력)")
			continue
		if select==5:
			print("프로그램종료")
			exit(0)
		else:
			print("당신은 %d를 선택했습니다" % select)
			break;
		
else:
	print("당신은 로그인상태가 아닙니다.")


