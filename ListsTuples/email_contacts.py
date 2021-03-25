# Given a list of tuples, each containing two strings: email address, and a contact name.
# This function creates a new list of contacts, in which it stores one string per person in the following familiar format for email purposes: ['Full Name <name@email.com>']

def full_emails(people):
    result = []
    for email, name in people: 
        result.append("{} <{}>".format(name, email))
    return result

contact_list = [
    (
        "johnsmith@company.com", "John Smith"
    ),
    (
        "joeblack@client.com", "Joe Black"
    )
]
print(full_emails(contact_list))

# Cautionary note about lists: 
# It is NOT advisable to use the range() function with lists the way we do with for...loops.  Instead, it is better to use the enumerate() function and then work with the indexes that way.

# Also, if there's a need to modify a list while iterating through it, a better approach is to work with a copy of the list instead.