import requests
import bs4
url = input("Enter your URL: ")
response = requests.get(url)
#print(type(response)) #object
#print(response.text) #unformatted, unreadable
filename = "temp.html"
bs = bs4.BeautifulSoup(response.text, "html.parser")
formatted_text = bs.prettify()
#print(formatted_text)
with open(filename, "w+") as f:
    f.write(formatted_text)
#count number of anchor tags and image tags
list_imgs = bs.find_all('img')
list_anchor = bs.find_all('a')
print("Number of image tage :",len(list_imgs), "Number of anchor tags:",len(list_anchor))