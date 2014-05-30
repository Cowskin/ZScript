from random import randrange


a = range(1,10)
for i in a:
  if i== 10:
	print i;
	break;
else:
    print "not found 10"
	
	

n = 5
foo = [randrange(10) for v in range(n)] #list comprehension

for t in foo:
    if t == 0:
        print('found 1');
        break;
else:
    print('did not find 1')