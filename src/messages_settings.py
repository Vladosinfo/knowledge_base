MESSAGES = {
    "hello": "How can I help you?",
    "good bye": "Good bye!",
    "close": "Good bye!",
    "exit": "Good bye!",
    "add_contact": "Your contact has been added",
    "add_more": "One more phone has been added",
    "added_address": "Address has been sucessfully added to your contact",
    "add_email": "Email succesfully added to your contact ",
    "change_phone": "Your contact has been changed",
    "change_birth": "Birthday has been changed",
    "clean_dir": "",
    "find_contact": "It's your phone number: ",
    "show_all": "These are all contacts:",
    "show_found": "These are found contacts:",
    "delete_contact": "Item has been deleted",
    "iter_contacts": "These are part of contacts",
    "list_days_to_birthday": "List of nearest birthday",
    "text_before_start": "Hello! Welcome to your Pocket Helper. For a quick start, enter space and see full list of commands that I can do.",
    "list_notes": "List of notes:",
    "list_notes_by_tag": "List notes searched by tag",
    "list_notes_by_string": "List notes searched by string",
    "change_notes_note_add_tag1": "Mark a word with the # symbol to make it a tag. (Example: 'Some #good news...')",
    "change_notes_note_add_tag2": "Mark a word with the # symbol to make it a tag. (Example: 'Some #special information...')",
    "change_notes_note_add_tag3": "You can enter more tags as desired 'words separated by spaces'. Or send empty string.",
    "changed_note": "Notes that you changed.",
    "change_note_input_tags": "Еnter more tags as desired 'words separated by spaces'. Or send empty string.:",
    "change_note_current_title": "Current title:",
    "change_note_current_description": "Current description:",
    "change_note_current_tags": "Current list of tegs:"
}

EXIT_COMMANDS = ["good bye", "close", "exit"]

WARNING_MESSAGES = {
    "correct_command": "Enter correct command",
    "change_phone": "Give me name, old_phone and new_phone. Syntax: >>> change_phone nameUser phoneNumber phoneNumber",
    "name": "Enter user name",
    "name_email": " Give me email, please. Syntax: >>> add_email nameUser email",
    "name_phone": "Give me name and phone please. Syntax: >>> add nameUser phoneNumber",
    "name_address": "Give me address please. Syntax: >>> add_address nameUser",
    "name_birth": "Give me name and new birthday. Syntax: >>> change_birth 'name' 'new_birth'",
    "not_correct_phone_is_not_a_number": "Pleace, put a number",
    "not_correct_phone_short_long": "Pleace, put more than 9 numebres, but no more than 13",
    "missing_name": "This name is missing in contact book",
    "contacts_book_empty": "Contacts book is empty yet.",
    "iter_no_result": "There are no records in this range",
    "show_found_empty": "Search did not return any results.",
    "search_cont": "Give me some text or digit",
    "not_correct_data": "Not correct data. Expected syntax: add nameUser 21-12-2021 phoneNumber",
    "no_list_days_to_birthday": "No birthdays in the near future",
    "search_note_by_tag_id_empty": "Input tag for search note"
}

COMMAND_HANDLER_DESCRIPTION = {
    "hello": "Greeting",
    "add_contact": "Add new contact to address book",
    "change_phone": "Change existing contact",
    "change_email": "Change existing email",
    "change_address": "Change existing address",
    "change_birth": "Change date of birth",
    "clean_dir": "Directory cleanup utility",
    "find_contact": "Find phone (item) by Name",
    "show all": "Show_all contacts of address book",
    "iter_contacts": "Show parn of items from .. to ... Sintax of command: >>>iter (show count items by default); item 1 5",
    "delete_contact": "Delete contact",
    "daysbir": "Count days to birthday",
    "add_email": "Add email to existing contact record",
    "birthdays": "List of users whose birthday is close",
    "add_note": "Add new note to dictionary notes",
    "show_all_notes": "Show all notes",
    "search_contact": "Search contacts by name or phone",
    "search_note": "Search notes",
    "search_notes_by_tag": "Search notes by tag",
    "change_note": "Change note",
    "delete_note": "Delete note by title. Write title of note.",
    "add_address": "Add address to existing contact",
    "help": "List of supported commands",
    "exit": "Close the program",
    "close": "Close the program",
    "good bye": "Close the program"
}
