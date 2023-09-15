test = []
_ = 0
max = 0
with open('datbase.txt', 'r') as data:
   test = data.readlines()
   
   for x in range(len(test)):
    if test[x] != '\n':
        _ += int(test[x])
    else:
       if max < _:
           max = _
       _ = 0
   print(max)