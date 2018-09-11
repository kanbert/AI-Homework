fruits =['apple', 'pear', 'orange', 'pinapple', 'mandarin']
for i in range(4):
    if(fruits[i] == "apple"):
      print ("I found it!")
fruits.append('bannana')
fruits.append('kiwi')
print (fruits)
letters =[]
for i in range(len(fruits)):
    letters.append(len(fruits[i]))
    print (str(fruits[i]) + " has " + str(letters[i]) + " letters.")