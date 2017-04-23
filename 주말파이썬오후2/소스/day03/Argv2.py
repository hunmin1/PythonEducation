import requests
from bs4 import BeautifulSoup


def stock(code):
	url = "http://finance.naver.com/item/main.nhn?code="+code
	s = requests.get(url)
	plain_text = s.text
	#print(plain_text)
	return plain_text


if __name__=='__main__':
	StockHtml = stock(sys.argv[1])
	soup = BeautifulSoup(StockHtml)
	ranks = soup.find("dl",{"class":"blind"})
		#dl 요소의 class : blind 속성
		#	<dl class="blind">를 찾음.
	print(ranks)
	print(ranks.get_text())
	exit(0)


#dddd
