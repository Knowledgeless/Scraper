'''

	Author: Knowledgeless
	Github: https://github.com/knowledgeless/

'''

try:
	class Colors:
			    Green = '\033[92m'
			    Red = '\033[91m'
			    White = '\033[99m'
	def MassPdfDownload():
		try:
			import requests
			import bs4 as bs
			import urllib.request
			from tqdm import tqdm

			print(Colors.Green+'''

				This Script Will Work For "https://bdebooks.com/" only
				
				''')

			print('''
				--------------------------------
				1. Download first page all books
				2. Download a writer's book only
				--------------------------------
				''')
			usrin = int(input("Choose an option: "))
			try:
				user = input("Enter your ebook link: ")
				response = requests.get(user).text
				search = bs.BeautifulSoup(response, "html.parser")
				source = search.find_all("a")
				links = []
				count = 0

						#parsing first page book links to get download link
				
				if usrin == 1:
					for i in source:
						link = i.get("href")	#checking urls
						if link is not None and link.startswith(user+"books/"):	#taking books links and appending next line
							links.append(link)
					for j in links:
						response1 = requests.get(j).text
						search1 = bs.BeautifulSoup(response1, "html.parser") #parsing second page link
						source1 = search1.find_all("a")
						links1 = []
						for k in source1:
							link1 = k.get("href")
							if link1 is not None and link1.startswith("http://dl.bdebooks.com/"): #taking only pdf links
								links1.append(link1)
								for t in links1:
									if t != "":
										dl = t
										if(dl[-4::]==".pdf"):
											r = requests.get(dl, stream = True)
											total = int(r.headers['content-length'])
												#downloading code
											with open(dl[-36::], "wb") as f:
												for data in tqdm(iterable = r.iter_content(chunk_size=1024), total=total/1024, unit="KB"):	#for progress bar
													f.write(data) #downloading books
											print(Colors.Green+"Complete! {}".format(dl))
										
				elif usrin ==2:
					for i in source:
						link = i.get("href")
						if link is not None and link.startswith("https://bdebooks.com/books/"):
							links.append(link)
					for j in links:
						response1 = requests.get(j).text
						search1 = bs.BeautifulSoup(response1, "html.parser")
						source1 = search1.find_all("a")
						links1 = []
						for k in source1:
							link1 = k.get("href")
							if link1 is not None and link1.startswith("http://dl.bdebooks.com/"):
								links1.append(link1)
								for t in links1:
									if t != "":
										dl = t
										count = count+1
										if(dl[-4::]==".pdf"):
											r = requests.get(dl, stream = True)
											total = int(r.headers['content-length'])
												#downloading code
											with open(t[-50::], "wb") as f:
												for data in tqdm(iterable = r.iter_content(chunk_size=1024), total=total/1024, unit="KB"):
													f.write(data)
											print(Colors.Green+"Complete!")
										

				else:
					print(Colors.Red+Colors.Red+"Sorry, Check Your Input!")
			except KeyboardInterrupt:
				print(Colors.Red+"\nYou Exited Manually")
			# except:
			# 	print("Check Your URL")
		except ValueError:
			print(Colors.Red+"Value Error!") 
		except ModuleNotFoundError:
			print(Colors.Red+'''

				[+] You Have To Install These First
				- pip & pip3 
				- tqdm
				- requests
				- bs4
					
				''')
		except requests.exceptions.ConnectionError:
			print(Colors.Red+"ConnectionError: Check Your Connection.")
		except KeyboardInterrupt:
				print(Colors.Red+"\nYou Exited Manually")
		
except:
	print(Colors.Red+'''
		Let Me Know Your Error!
		Github: https://github.com/Knowledgeless/
	''')
