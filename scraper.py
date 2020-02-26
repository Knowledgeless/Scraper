import requests
import bs4 as bs
import urllib.request
from tqdm import tqdm
import option1 as PDF


class Colors:
    Green = '\033[92m'
    Red = '\033[91m'


def scraper():
	while True:
		try:
			print('''
				\t---Scrap Data Type---
				-------------------------------------
				1. PDF
				2. Images
				3. Links
				4. Exit
				''')

			user = int(input("\tChoose an option: "))

	# PDF Scraping Starts
			if user == 1:
				pdf = PDF.MassPdfDownload()
				return pdf
	# Image Scraping Starts
			elif user == 2:
				try:
					user = input("\tEnter Your URL: ")
					response = requests.get(user).text
					source = bs.BeautifulSoup(response, 'html.parser')
					# detecting img url
					imgs = source.find_all('img')
					links = []

					for img in imgs:
						# getting sources of img
						link =  img.get('src')
						if 'http://' not in link:
						 	link = user + link
						links.append(link)

					print("Images Detected: " + str(len(links)))
					# checking url
					for i in range(len(links)):
						filename = f'img_{i}{links[i][-4::1]}'
						with open(filename, 'wb') as image:
							image.write(requests.get(links[i]).content)
						print("Done!")

				except requests.exceptions.ConnectionError:
					print("\t\nCheck Data Connection!")
				except TypeError:
					print("\t\nURL Not Accessable!")

	# Link Scraping Starts
			elif user == 3:
				
				try:
					user = input("\tEnter Your URL: ")
					response = requests.get(user).text
					search = bs.BeautifulSoup(response, 'html.parser')
					# detecting urls
					source = search.find_all('a')
					links = []

					for i in source:
						# parsing url addresses
						link =  i.get('href')
						# checking href is a url or not
						if link.startswith("http"):
							links.append(link)
							# creating txt file
							with open("links.txt", "w") as files:
								content = files.write(str(links))
					print("\nDone! Check 'links.txt' file.\n")
				# handling error

				except TypeError:
					print("\t\nURL Not Accessable!")
				except requests.exceptions.ConnectionError:
					print("\t\nCheck Data Connection!")
				except:
					print("\t\nURL Doesn't Exist!\n")

			elif user == 4:
				print('''\n\t\t[+] If you have any query then let me know. Authors Github URL:
				https://www.github.com/knowledgeless
					''' )
				break
			else:
				print("Wrong Input!")
		except ValueError:
			print("ValueError: Enter Integer Number From Above Options")
		except KeyboardInterrupt: 
			print("\n\n\t[-] You Broke The Programme Manually\n")
			break
scraper()