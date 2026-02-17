print('Welcome to my Budget tracker')

expenses = [] #creates an empty list 
categories = [] 
while True:
    expense = input("Enter an expense (or type 'done' to finish): ")
    if expense == 'done':
        break
    else:
        category = input("What category? (rent,food/transport/shopping/other): ")
        expenses.append(float(expense))
        categories.append(category)
        print(f"Added ${expense} for {category}")

#Display of total 
#total = sum(expenses) #adds up all the numbers in your list
#print(f"\nTotal spending: ${total}") #/n creates a blank line to make it look nicer. f means format string

total = sum(expenses)
average = total / len(expenses)
highest = max(expenses)
lowest = min(expenses)

print("\n BUDGET SUMMARY ")
print("Total spending: $", total)
print("Average per expense: $", average)
print("Highest expense: $", highest)
print("Lowest expense: $", lowest)

print("\n SPENDING BY CATEGORY ")
for cat in set(categories):
    cat_total = sum(e for i, e in enumerate(expenses) if categories[i] == cat)
    print(cat, ": $", cat_total)

