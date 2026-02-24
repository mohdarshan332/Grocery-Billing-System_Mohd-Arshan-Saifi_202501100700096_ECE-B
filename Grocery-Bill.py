'''Name:- Mohd Arshan Saifi'''
'''Roll No:- 202501100700096'''
'''Branch & Sec:- ECE-B'''


p1 = float(input("Enter Price of Item 1: "))
q1 = int(input("Enter Quantity of Item1: "))

p2 = float(input("Enter Price of Item 2: "))
q2 = int(input("Enter Quantity of Item2: "))

p3 = float(input("Enter Price of Item 3: "))
q3 = int(input("Enter Quantity of Item3: "))

p4 = float(input("Enter Price of Item 4: "))
q4 = int(input("Enter Quantity of Item4: "))

p5 = float(input("Enter Price of Item 5: "))
q5 = int(input("Enter Quantity of Item5: "))

total = (p1*q1) +  (p2*q2) +  (p3*q3) +  (p4*q4) +  (p5*q5)
print("Original total: ", total)

if(total > 100):
    discount = total * 0.10
    total = total - discount
    print("Discount applied: ", discount)
    
    
print("Final Amount: ", total)