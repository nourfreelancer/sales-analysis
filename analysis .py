f=open("sales.csv","r")
cont=f.readlines()

total_quantity=0
total_amount=0

for line in range(len(cont)):
       if line == 0 :
              continue

       part=cont[line]
      
       quantity=int(part.strip().split(",")[2])
     
       price=float(part.strip().split(",")[3])
       total_quantity += quantity
       total_amount += price*quantity

print("----- Summary report ------ ")
print(f"Total Quantity sold: {total_quantity}")
print(f"Total Sales Amount: {total_amount}")


f.close()


