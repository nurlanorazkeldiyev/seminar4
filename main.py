from mytree import myheap



f=open('words_37.txt', 'r')
lines=f.readlines()


mydata = myheap ()
for l in lines:
  #  print( l, end = ', ' )
    mydata.add( l, l )  
print()


print( 'sorted order ...' )
print( 'The result is : ', end   )
for x in mydata:
    print( x, end   )
print()
for l in range(0,561):
        max(lines)
        min(lines)
print('minimum',min(lines),'maximum',max(lines))
