# Start with an empty grocery list
groceries = []

# Prompt for a new item until the just hit Enter
# (meaning the didn't type anything in at the prompt)
while True:
    item = input('What do you need from the store? ')

    if item == '':  # Alternatively: check if len(item) == 0
        break
    groceries.append(item)

# After we break, python will move to the next unindented line of code after the loop

# Print the grocery list with indexes
indexes = range(len(groceries))
for i in indexes:
    item = groceries[i]
    print(f'{i}: {item}')

# Give them the chance to replace 
start_index_to_replace = int(input('What start index to replace? '))
end_index_to_replace = int(input('What end index to replace? '))

if start_index_to_replace == end_index_to_replace:
    # Prompt the user for the new item
    new_item = input('What is the new item? ')

    # - replace the item at that index with the new item
    groceries[start_index_to_replace] = new_item
else:
    # gather replacements
    replacements = []
    while True:
        new_item = input('What is the new item? ')
        if new_item == '':
            break
        replacements.append(new_item)
        print(replacements)
    print('-------about to do weird thing--------')
    print(groceries)
    groceries[start_index_to_replace:end_index_to_replace] = replacements
    print('-------just did weird thing--------')
    print(groceries)


# - print the updated combined list
for i in indexes:
    item = groceries[i]
    print(f'{i}: {item}')


# to_delete = [3, 5, 6, 9]
# for index_of_item_to_delete in to_delete:
#     del groceries[index_of_item_to_delete]
