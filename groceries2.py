'''
Instrutions:


The starter code provides you with the main menu for a command-line
based grocery list application.

The user should be able to add, update, and remove items.

Small exercise ------------------------------------------------
Using this starter code, you're going to combine the pieces of code
you've written so far to create the functionality for each action (either 
adding, updating, or removing an item).

Each time the user adds, updates, or deletes an item, they should see the main menu again.

Medium exercise ------------------------------------------------
For each sub-menu, show the user another menu with choices for that section of the application.
For example, when Removing Items, show the user this menu:

1. Print items
2. Delete an item
3. Delete multiple items
4. Return to main menu

If they enter "2", prompt them for the index of the item to delete.
If they enter "3", prompt them for a start index and an end index for the slice to delete.

After deleting, show them the "delete" menu again.
To return to the main menu, the user needs to enter "4" at the prompt.

Large exercise ------------------------------------------------
Add a second array that stores whether or not each grocery list item has been obtained.
Every time you add or remove an item, you need to add to or remove from this second list.

Add an additional main menu option for changing the status of any grocery list item.

Update the "Print Items" output so that it shows whether or not an item has been obtained.
'''


groceries = []


main_menu = '''

1. Print List
2. Add Items
3. Edit Items
4. Remove Items
5. Quit

'''
sub_menu = '''

1. Print items
2. Delete an item
3. Delete multiple items
4. Return to main menu
'''

while True:
    menu_choice = int(input(main_menu))

    # Add if/else statements for each menu item
    # For each of these, add in code to handle adding/editing/removing items
    if menu_choice == 1:
        while True:
            menu_choice2 = int(input())
            grocery_range = range(len(groceries))
            for i in grocery_range:
                item = groceries[i]
                print(f'{i}: {item}')
    elif menu_choice == 2:
            while True:
                item_add = input('Please add items to your grocery list: ')
                if item_add == '':
                    break
                groceries.append(item_add)
    elif menu_choice == 3:
            first_menu_choice = int(input('Please enter starting index point: '))
            second_menu_choice = int(input('Please enter endind index point: '))

            if first_menu_choice == second_menu_choice:
                new_item = input('Please enter new item to add: ')

                groceries[second_menu_choice] = new_item
            else:
                replacements = []
                while True:
                    item_to_replace = input('Please input item to add: ')
                    if item_to_replace == '':
                        break
                    replacements.append(item_to_replace)
                    groceries[first_menu_choice:second_menu_choice] = replacements
    elif menu_choice == 4:
            print(groceries)
            while True:
                item_to_remove = input('Please input the index number of the item you would like to remove. If you would like to exit enter -1: ')
                if item_to_remove == '':
                    break
                else:
                    item_to_remove = int(item_to_remove)
                    del groceries[item_to_remove]

    elif menu_choice == 5:
         break

    #print(f'Your current list: {groceries}')  
    #elif menu_choice == 4:


print('Thank you for using the grocery list app!')