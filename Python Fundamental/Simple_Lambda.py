print("simple calculate lamda")
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
print('')



print("Filter dictionary dengan lamda")
items = [
    {'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'name': 'wine', 'price': 10.0, 'quantity': 5},
]
def read_item(name):
    global items
    #filter return true jika objek tersedia
    myitems = list(filter(lambda x : x['name'] == name, items))
    return myitems
    
for key,val in read_item('wine')[0].items():
    print(f"{key} : {val}")