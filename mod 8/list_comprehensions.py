# it`s a short trick methode for printing a sequence

# it`s a pattern ~ [ output for item in range if condition]

sq= [i for i in range (10) if i%3==0]
print(sq)


# another method 

sq=[]
for i in range(6): 
    sq.append(i*i)  # prints all digits within the range 6*6=36.
print(sq)
 

# practice

num=[-2, -1, 3, 5, -3]
num=[ 0 if val<0 else val for val in num]
print(num)