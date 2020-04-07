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

sub_menu = '''

1. Print items
2. Delete an item
3. Delete multiple items
4. Return to main menu
'''


main_menu = '''

1. Print List
2. Add Items
3. Edit Items
4. Remove Items
5. Quit

'''
groceries = []

# Defines second menu function to use in main menu loop.
def second_menu():
        while True:
                
                menu_choice2 = int(input(sub_menu))
                grocery_range = range(len(groceries))

                if menu_choice2 == 1:
                    for i in grocery_range:
                        item = groceries[i]
                        print(f'{i}: {item}')
                elif menu_choice2 == 2:
                    while True:
                        item_to_remove = input('Please input the index number of the item you would like to remove: ')
                        if item_to_remove == '':
                            break
                        else:
                            item_to_remove = int(item_to_remove)
                            del groceries[item_to_remove]
                elif menu_choice2 == 3:
                    first_menu_choice = int(input('Please enter starting index point: '))
                    second_menu_choice = int(input('Please enter endind index point: '))
                    del groceries[first_menu_choice:second_menu_choice]# = removals
                elif menu_choice2 == 4:
                    break


# Creates while loop that handles the main menu selection using if statements.
while True:

    menu_choice = int(input(main_menu))
   

    # Add if/else statements for each menu item
    # For each of these, add in code to handle adding/editing/removing items

    # If users entry is 1 it should print the grocery list and prompt the submenu after list entry is done.
    if menu_choice == 1:
        grocery_range = range(len(groceries))
        for i in grocery_range:
            item = groceries[i]
            print(f'{i}: {item}')

        # Should call second menu and let the user select menu items reliably.
        second_menu()
           

    # Menu selection 2 should allow the user to add items to their list as needed. It should also then print the submenu.
    elif menu_choice == 2:
            while True:
                item_add = input('Please add items to your grocery list: ')
                if item_add == '':
                    break
                groceries.append(item_add)
        
            second_menu()

    # Menu selection 3 should allow users to edit their list based on index points. It should also print the submenu.
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
            
            second_menu()

    # Menu selection 4 should allow users to remove whatever item they want. It should also prompt users with the submenu
    elif menu_choice == 4:
            print(groceries)
            while True:
                item_to_remove = input('Please input the index number of the item you would like to remove: ')
                if item_to_remove == '':
                    break
                else:
                    item_to_remove = int(item_to_remove)
                    del groceries[item_to_remove]
            
            second_menu()

    # Menu selection 5 will exit out of the entire program
    elif menu_choice == 5:
         break

    #print(f'Your current list: {groceries}')  
    #elif menu_choice == 4:


print('Thank you for using the grocery list app!')