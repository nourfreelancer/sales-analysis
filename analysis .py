f=open("sales.csv","r")
cont=f.readlines()

total_quantity=0
total_amount=0
max_product_sales=0
top_product=None
products={}


for line in range(len(cont)):
       if line == 0 :
              continue

       part=cont[line]
       name=part.strip().split(",")[1]
       quantity=int(part.strip().split(",")[2])
     
       price=float(part.strip().split(",")[3])
       total_quantity += quantity
       total_amount += price*quantity
       totalamount=price*quantity
       if name not in products:
         products[name] = totalamount
       else : 
              products[name] += totalamount

for i,k in products.items():
       if k > max_product_sales :
              max_product_sales = k
              top_product = i


print("------ Summary report ------ ")
with open("sales_summary.csv","w") as file:
   
    file.write("Metric,Value\n")
    file.write(f"Total Quantity sold , {total_quantity}\n")
    file.write(f"Total Sales Amount, {total_amount}\n")
    file.write(f"Top Product ,{top_product}")
f.close()

