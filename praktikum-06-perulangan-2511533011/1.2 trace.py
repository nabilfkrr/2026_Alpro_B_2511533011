stock = 7
sold = 0
  
while stock >= 2: 
    print("Sold:", sold, "left:", stock)
    stock -= 2 
    sold += 2 
  
print("Sold:", sold, "left:", stock)