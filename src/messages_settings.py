MESSAGES = {
    "hello": "How can I help you?",
    "good bye": "Good bye!",
    "close": "Good bye!",
    "exit": "Good bye!",
    "add": "Your contact has been added",
    "add_more": "One more phone has been added",
    "added_address": "Address has been sucessfully added to your contact",
    "add_email": "Email succesfully added to your contact ",
    "change": "Your contact has been changed",
    "change_birth": "Birthday has been changed",
    "phone": "It's your phone number: ",
    "show_all": "These are all contacts:",
    "show_found": "These are found contacts:",
    "delete": "Item has been deleted",
    "iter": "These are part of contacts",
    "list_days_to_birthday": "List of nearest birthday"
}

EXIT_COMMANDS = ["good bye", "close", "exit"]

WARNING_MESSAGES = {
    "correct_command": "Enter correct command",
    "name": "Enter user name",
    "name_email": " Give me email, please",
    #"not_correct_phone": "Not correct phone",
    "name_phone": "Give me name and phone please. Syntax: >>> add nameUser phoneNumber",
    "name_address": "Give me address please. Syntax: >>> add_address nameUser",
    "name_birth": "Give me name and new birthday. Syntax: >>> change_birth 'name' 'new_birth'",
    "not_correct_phone_is_not_a_number": "Pleace, put a number",
    "not_correct_phone_short_long": "Pleace, put more than 9 numebres, but no more than 13",
    "missing_name": "This name is missing in contact book",
    "contacts_book_empty": "Contacts book is empty yet.",
    "iter_no_result": "There are no records in this range",
    "show_found_empty": "Search did not return any results.",
    "not_correct_data": "Not correct data. Expected syntax: add nameUser 21-12-2021 phoneNumber",
    "no_list_days_to_birthday": "No birthdays in the near future"
}

COMMAND_HANDLER_DESCRIPTION = {
    "hello": "Greeting",
    "add": "Add new contact to address book",
    "change": "Change existing contact",
    "change_birth": "Change date of birth",
    "phone": "Find phone (item) by Name",
    "show all": "Show_all contacts of address book",
    "iter": "Show parn of items from .. to ... Sintax of command: >>>iter (show count items by default); item 1 5",
    "search": "Search contacts by name or phone",
    "delete": "Delete contact",
    "daysbir": "Count days to birthday",
    "add_email": "Add email to existing contact record",
    "birthdays": "List of users whose birthday is close",
    "add note": "Add new note to dictionary notes",
    "search note": "Search notes",
    "search notes by tag": "Search notes by tag",
    "add_address": "Add address to existing contact",
    "help": "List of supported commands",
    "exit, close, good bye": "Close the program"
}
