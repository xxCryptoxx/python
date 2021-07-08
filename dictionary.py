import requests
from bs4 import BeautifulSoup
import lxml

class Dictionary:

	def __init__(self, word):
		self.word = word
		self.headers = headers
		self.url = url


	def soupify(self):
		page = requests.get(url, headers)

		soup = BeautifulSoup(page.content, "lxml")
		try:
			search = soup.find('h1', class_='css-o8eka5').text
			content = soup.find('span', class_='one-click-content css-nnyc96 e1q3nk1v1').text
			example = soup.find('span', class_='luna-example italic').text
			howto = soup.find('p', class_='one-click-content css-b5q2lz e15kc6du2').text

			print(end='\n')
			print(f'\033[1mWORD:\033[0m {search}', end='\n\n')
			print(f'\033[1mDEFINED:\033[0m {content}', end='\n\n')
			print(f'\033[1mEXAMPLE:\033[0m {example}', end='\n\n')
			print(f'\033[1mHOW TO USE:\033[0m {howto}', end='\n\n')
		except:
			print('\033[1mTroubleshooter Says\033[0m')
			print('Nothing Here.')
			print('1. Does your word exist?')
			print('2. Is the spelling correct?')
			pass


while True:
	x = input('What Word? ')
	url = f'https://www.dictionary.com/browse/{x}'
	headers = {
		"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
		"Referer":"https://www.dictionary.com/",
	}
	start = Dictionary(x)
	print(start.soupify())

	if x == 'quit()':
		break
	else:
		continue
