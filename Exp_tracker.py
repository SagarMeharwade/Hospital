# print("------ Welcome to Daily Expense Tracker ------")

# expenses = []  # List to store expense dictionaries

# while True:
#     print("\nMenu:")
#     print("1. Add Expense")
#     print("2. View All Expenses")
#     print("3. Delete an Expense")
#     print("4. View Total Expenses")
#     print("5. Exit")
    
#     try:
#         choice = int(input("Enter your choice (1-5): "))
        
#         if choice == 1:
#             # Add expense
#             name = input("Enter expense name: ")
#             amount = float(input("Enter amount: "))
#             category = input("Enter category (Food/Travel/Bills/etc.): ")
#             expenses.append({"name": name, "amount": amount, "category": category})
#             print(f"Expense '{name}' added successfully!")
        
#         elif choice == 2:
#             # View all expenses
#             if not expenses:
#                 print("No expenses added yet.")
#             else:
#                 print("\nAll Expenses:")
#                 for i, exp in enumerate(expenses, start=1):
#                     print(f"{i}. {exp['name']} - ${exp['amount']} - Category: {exp['category']}")
        
#         elif choice == 3:
#             # Delete an expense
#             if not expenses:
#                 print("No expenses to delete.")
#             else:
#                 for i, exp in enumerate(expenses, start=1):
#                     print(f"{i}. {exp['name']} - ${exp['amount']} - Category: {exp['category']}")
#                 try:
#                     idx = int(input("Enter the number of the expense to delete: "))
#                     if 1 <= idx <= len(expenses):
#                         removed = expenses.pop(idx - 1)
#                         print(f"Expense '{removed['name']}' deleted successfully!")
#                     else:
#                         print("Invalid number!")
#                 except ValueError:
#                     print("Please enter a valid number!")
        
#         elif choice == 4:
#             # View total expenses
#             total = sum(exp['amount'] for exp in expenses)
#             print(f"Total Expenses: ${total}")
        
#         elif choice == 5:
#             print("Thank you for using the Expense Tracker. Goodbye!")
#             break
        
#         else:
#             print("Invalid choice! Please enter a number between 1 and 5.")
    
#     except ValueError:
#         print("Error: Please enter a valid number!")


# def Menu(): 
#     print('-------------------------')
#     print("\n------ Welcome to Daily Expense Tracker ------")
#     print('1. Add Expense')
#     print('2. View Expense')
#     print('3. Delete an Expense')
#     print('4. View all Expense')
#     print('5. Exit')


# Expense_Tracker = []

# while True:
#     Menu()
#     try:
#         choice = int(input('Enter your Choice(1-5): '))
#     except ValueError as N:
#         print('Error Code:',N)
#     try:
#         if choice not in [1,2,3,4,5]:
#             raise Exception('Invaild Choice! Try Again..')
        
#     except Exception as e:
#         print('Error Code:',e)
    
    
#     if choice == 1:
#         name = input('Enter your Name: ')
#         try:
#             if name in Expense_Tracker:
#                     raise Exception('Person Name is already Existed...')
#             else:
#                 amount = int(input('Enter your amount: '))
#                 category = input("Enter category (Food/Travel/Bills/etc.): ").capitalize()
#                 Expense_Tracker.append({'Name':name,'Amount':amount,'Category':category})
#                 print('Expense is added to DB suessfully....')
#         except Exception as A:
#             print('Error Code:',A)
        
#     elif choice == 2:
#         try:
#             if not Expense_Tracker:
#                 raise Exception('There is no Expense is addded')
#             else:
#                 for i,Details in enumerate(Expense_Tracker,start = 1):
#                     print(f"{i}, Name: {Details['Name']}, Amount: {Details['Amount']}, Category: {Details['Category']}")
#         except Exception as F:
#             print('Error Code:',F)
                
        
#     elif choice == 3:
#         try:
#             for i,Details in enumerate(Expense_Tracker,start = 1):

#             print(f"{i}, Name: {Details['Name']}, Amount: {Details['Amount']}, Category: {Details['category']}")
#             idx = int(input('Enter the index number which you want delete your Expense: '))
#                 if 1 <= idx < len(Expense_Tracker):
#                     res = Expense_Tracker.pop(idx-1)
#                 else:
#                     raise ValueError('Invaild String sir please enter the vaild number Sir')
#         except ValueError as V:
#             print('Error Code',V)
    
#     elif choice == 4:
#         print('\nTotal Expense')
#         print('------------------------')
#         total = sum(exp['Amount'] for exp in Expense_Tracker)
#         print(f"Total Expenses: ₹{total}")

#     elif choice == 5:
#         print('Thank you sir Visit Again...')
#         break





# arr1 = [5 ,4 ,13 ,1]
# arr2 = [3 ,2 ,6 ,1]

# arr1.sort()
# arr2.sort()
# m1 = min(arr1)
# m2 = min(arr2)
# if m1 == m2:
#     arr2.pop(m2 - 1)
#     m2 = min(arr2)
# else:
#     res = m1+m2
# print(m1+m2)



# arr = [4, 5, 1, 2, 3]
# arr.sort()
# n = len(arr) // 2
# res = []
# for i in range(n):
#     mi = min(arr)
#     ma = max(arr)
#     res.append(mi)
#     res.append(ma)
#     arr.pop(-1)
#     arr.pop(0)
# if arr:
#     res.append(arr[0]) 
# print(res)

#0. 1. 2. 3. 4  5. 6  7
# arr = [9, 2, 8, 4, 5, 7, 6, 0]
# arr.sort()

# res = 0

# left = 0
# right = len(arr)-1
# while left < right:
#     res += arr[left] * arr[right]
#     left += 1
#     right -= 1
# print(res)

# arr = [7, 9, 10, 8, 11]

# for i in range(1,len(arr)-1):
#     mid = arr[i]
#     left = arr[i-1]
#     right = arr[i+1]
#     if left <= mid >= right: 
#         print(i+1)
#         break

# def fuc(S):
#     if S % 11 == 0:
#         return 1
#     return -1
# S = 94
# print(fuc(S))
