import os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as pt



def inputDeets():
    header = ["Category","Expense","Date"]
    deets = []
    cat = input("Enter the Category: ")
    amount = int(input("Enter The Expense: "))
    dat = input("Enter the Date(YYYY/MM/DD)")
    deets = np.array([cat,amount,dat])
    if os.path.exists("data.csv"):
        with open("data.csv",mode="a",newline="") as file:
            csv_reader = csv.writer(file)
            csv_reader.writerow(deets)
    else:
        with open("data.csv",mode="w",newline="") as file:
            csv_reader = csv.writer(file)
            csv_reader.writerow(header)

def analyzeDeets():
    df = pd.read_csv("data.csv")
    groupby_cat = df.groupby("Category")["Expense"].sum()
    groupby_date = df.groupby("Date")["Expense"].sum()
    print("Cateogry Based Spending")
    print(groupby_cat)
    print("Date wise spending")
    print(groupby_date)
    

def visualizeDeets():
    df = pd.read_csv("data.csv")
    grouped = df.groupby("Category")["Expense"].sum()
    x = grouped.index
    y = grouped.values
    pt.subplot(2,1,1)
    pt.barh(x,y)

    grouped2 = df.groupby("Date")["Expense"].sum()
    pt.subplot(2,1,2)
    x = grouped2.index
    y = grouped2.values
    pt.barh(x,y)
    pt.show()

def main():
    while True:
        print("\nExpense Tracker Menu")
        print("-------------------")
        print("1. Add New Expense")
        print("2. Analyze Expenses")
        print("3. Visualize Expenses")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            inputDeets()
        elif choice == '2':
            analyzeDeets()
        elif choice == '3':
            visualizeDeets()
        elif choice == '4':
            print("\nThank you for using Expense Tracker!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()


