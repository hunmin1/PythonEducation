import sys
MyMoney = int()
Pass = 123123
Input = 0;
count = 0;
if __name__=="__main__":
	MyMoney = 100000000
	while True:
		try:
			print("패스워드를 입력하세요 : ", end="")
			Input = int(input())
			if Input==123123:
				while True:
					print("인출할 금액을 입력 \n최대100만원 입니다.  : ", end="")
					OutMoney = int(input())
					if OutMoney < 1000000:
						if OutMoney < MyMoney:
							MyMoney -= OutMoney
							print("%d원을 인출\n 잔고 : %d" % (OutMoney, MyMoney))
							exit(0)
						else:
							print("인출하고자 하는 금액이 잔고보다 많습니다.")
							continue
					else:
						print("한번에 최대 100만원까지 인출할 수 있습니다.")
						continue
			else:
				count+=1
				print("패스워드를 제대로 입려하세요. (%d회 틀림)"%count)
				if(count==5):
					print("")
					print("%%%%%%%%%%%%%%%%%%% 종 료 %%%%%%%%%%%%%%%%%%%%%%%%")
					print("\t5회이상 틀려서 프로그램 종료")
					exit(0)

				continue

		except ValueError:
			print("숫자만 입력해야합니다")
			continue
		
			

		
		