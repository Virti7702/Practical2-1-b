'''
Name - Virti Shah
ID - 20CE135
Aim - A python script to merge two dictionaries.


'''
dict = {1:'110', 2:'69', 3:'9'}
e = {4:'z', 5:'y', 6:'x'}
def merge(dict,e):
    return (dict.update(e))

print(merge(dict,e))
print (dict)   