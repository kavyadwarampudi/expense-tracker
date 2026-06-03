import csv
import os
import datetime

FILE="expenses.csv"

def main_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total")
    print("4. Delete Expense")
    print("5. Exit")
    choice=input("Enter choice: ")
    return choice

def add_expense():
    amount=input("Enter amount: ")
    category=input("Enter category (Food/Travel/Shopping etc): ")
    description=input("Enter description: ")
    date=datetime.date.today()
    
    with open(FILE,"a",newline="") as f:
        writer=csv.writer(f)
        writer.writerow([amount,category,description,date])

        print("Expense addded successfully!")



def view_expenses():
    if not os.path.exists(FILE):
        print("NO expenses found!")
        return
    with open(FILE,"r") as f:
        reader= csv.reader(f)
        print("\n--- All Expenses ---")
        for row in reader:
            print(f"Amount: {row[0]} | Category: {row[1]} | Description: {row[2]} | Date: {row[3]}")

def view_total():
    if not os.path.exists(FILE):
        print("No expenses found!")
        return
    total=0
    with open(FILE,"r") as f:
        reader=csv.reader(f)
        for row in reader:
            total=total+float(row[0])
    print(f"\nTotal Expenses: {total}")

def delete_expense():
    view_expenses()
    if not os.path.exists(FILE):
        return

    row_number=int(input("\nEnter row number to delete: "))

    with open(FILE,"r") as f:
        reader=csv.reader(f)
        rows=list(reader)
    if row_number<1 or row_number>len(rows):
        print("Invalid row number!")
        retuen

    rows.pop(row_number-1)

    with open(FILE,"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerows(rows)
    
    print("Expense deleted successfully!")
    


while True:
    choice=main_menu()
    if choice=="1":
        add_expense()
    elif choice=="2":
        view_expenses()
    elif choice=="3":
        view_total()
    elif choice=="4":
        delete_expense()
    elif choice=="5":
        print("Goodbye!!!")
        break
    else:
        print("Coming Soon.....")

