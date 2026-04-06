# Functions
def create_user(users:dict, doc: str, name_surname: str, age: str, sex: str):
    """This fucntion creates a user, based on a document of identity, 
    and that document leads to its corrresponding name, age, and sex. 
    It returns the dictionary fill with the information."""
    if doc.strip() == "":                                                      # -> Makes sure doc it is not empty.  
        return "Document cannot be empty."                                     
    
    elif doc in users:                                                         # -> If repeated doc, shows error.
        return "Document already exists."
    
    elif len(doc) < 10 or len(doc) > 10:                                       # -> Makes sure doc is a 10 digit number.
        return f"Document must be a 10 digit number."
    elif doc.isdigit() == False:                                               # -> Makes sure doc is a number.
        return f"Document can only be numbers, you wrote {doc}"
    
    elif name_surname.strip() == "":                                           # -> Makes sure name_surname is not empty.
        return "Name and surname can't be empty."
    
    elif not name_surname.replace(" ","").isalpha():                           # -> Makes sure name_surname is filled up with only letters.
        return f"Don't use any characters rather than letters, you wrote {name_surname}"
    
    elif age.strip == "" or not age.strip():                                   # -> Makes sure age is not empty and is a number
        return f"In age use just numbers, you wrote {age}"
    
    elif not sex.replace(" ","").isalpha():                                    # -> Makes sure sex is filled up with only letters.
        return f"Don't use any character rather than letter, you wrote {sex}"

    else:                                                                      # -> Creates the new user with a single code wich is the document.
        users[doc] = {
        "name surname":name_surname,
        "age":age,
        "sex":sex
        }

        return (f"User {name_surname} created.")

def search_user(users, doc:int)->str:
    """This function seraches the user using the document of 
    identity 'doc' and returns the dictionary, else, it will 
    display a text 'Document not found.'."""

    return users.get(doc,"Document not found.")

def update_user(users, doc:int, name_surname=None, age=None, sex=None)->str:
    """This function updates 1 or more data of a single user at a time."""
    if doc not in users:
        return "User not found."
    
    if name_surname is not None:
        users[doc]["name surname"] = name_surname

    if age is not None:
        users[doc]["age"] = age

    if sex is not None:
        users[doc]["sex"] = sex

    return "User updated succcesfully!"

def delete_user(users, doc:int)->str:
    """This function deletes the user usigh the unique key (document)."""
    if doc in users:
        del users[doc]
        return f"Deleted user with document {doc}"
    
    else:
        return "Not found"