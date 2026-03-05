##Task 1
import sys

try:
    order_amount=int(input("Enter the order amount: "))
    print("You entered:", order_amount)
    
except ValueError:
    print("Invalid input. Please enter a valid number.")
    sys.exit(1)

if order_amount>=2000:
    discount=0.15*order_amount
elif order_amount>=1500 and order_amount<2000:
    discount=0.1*order_amount
elif order_amount>=1000 and order_amount<1500:
    discount=0.07*order_amount
else:
    discount=0
print("Discount amount is: ", discount)

##Task 2
orders=[1200,2500,800,1750,3000]
for order_amount in orders:
    if order_amount>=2000:
        discount_percentage=15
    elif order_amount>=1500 and order_amount<2000:
        discount_percentage=10
    elif order_amount>=1000 and order_amount<1500:
        discount_percentage=70
    else:
        discount_percentage=0
    
    discount= (discount_percentage/100)*order_amount
    final_amount=order_amount-discount

    print(order_amount, "->", discount_percentage, "%", "->", final_amount)

total_revenue=0
for order_amount in orders:
    if order_amount>=2000:
        discount_percentage=15
    elif order_amount>=1500 and order_amount<2000:
        discount_percentage=10
    elif order_amount>=1000 and order_amount<1500:
        discount_percentage=70
    else:
        discount_percentage=0
    
    discount= (discount_percentage/100)*order_amount
    final_amount=order_amount-discount

    total_revenue+=final_amount

print("Total revenue is: ", total_revenue)



##Task 3

orders = []

while True:
    print("\n----- MENU -----")
    print("1 - Add Order Amount")
    print("2 - Show Orders with Discounts")
    print("q - Quit")

    choice = input("Enter your choice: ")

    if choice == 'q':
        print("Program terminated.")
        break   

    elif choice == '1':
        try:
            amount = int(input("Enter order amount: "))
            orders.append(amount)
            print("Order added successfully!")
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue 

    elif choice == '2':
        if not orders:
            print("No orders available.")
            continue  

        total = 0
        print("\nOrder  ->  Discount%  ->  Final Amount")
        print("----------------------------------------")

        for order_amount in orders:

            if order_amount >= 2000:
                discount_percent = 15
            elif order_amount >= 1500:
                discount_percent = 10
            elif order_amount >= 1000:
                discount_percent = 7
            else:
                discount_percent = 0

            discount = (discount_percent / 100) * order_amount
            final_amount = order_amount - discount
            total += final_amount

            print(order_amount, "->", str(discount_percent) + "%", "->", final_amount)

        print("Total Revenue:", total)

    else:
        print("Invalid choice! Please select 1, 2, or q.")
        continue 



##Task 4

daily=[200, 150, 0, 400, 50, -1, 300]
total_sales=[]
for value in daily:
    if value==-1:
        print("Corrupted data found.")
        break
    elif value==0:
        print("No sales on this day.")
        continue
    else:
        total_sales.append(value)
print("Total sales: ", sum(total_sales))


