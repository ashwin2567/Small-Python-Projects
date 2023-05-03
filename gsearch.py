from googlesearch import search as s
Keyword = input("Enter your query: ")
results = s(Keyword, 20);
for i in results:
    print(i);

