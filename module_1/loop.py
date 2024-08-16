
my_dict = {1:"sam", 2: "ram"}

news = {k:v for k,v in my_dict.items() if k not in [1]}

print(news[2])