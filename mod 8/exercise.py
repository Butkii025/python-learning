data= True
line=1
word= "python"  #reading of PYTHON from starting
with open("mod 8/sample.txt","r") as f:
    while data:
        data= f.readline()
        if (word in data):
            print(f"{word} found in line {line}")
            break

    
        line+=1
