# 👤 User Management System

A simple command-line application written in Python for managing user records in memory. Users are stored in a dictionary using their 10-digit document number as a unique key.

---

## 📁 Project Structure
```
user-management-system/
│
├── main.py          # Entry point — runs the interactive menu
└── functions.py     # Core logic — CRUD functions for user management
```

---

## 🚀 Getting Started

### Requirements

- Python 3.x (no external libraries needed)

### Run the program
```bash
python main.py
```

---

## 🖥️ Features

The program presents an interactive menu with 5 options:
```
Welcome to User Management System.
1) Create User.
2) Search User.
3) Update User.
4) Delete User.
5) Exit Program.
```

---

## ⚙️ How It Works

### 1. Create User
Registers a new user in the system.

**Required fields:**
| Field | Validation |
|---|---|
| Document | Exactly 10 digits, numbers only, must be unique |
| Name & Surname | Letters only (spaces allowed), cannot be empty |
| Age | Cannot be empty |
| Sex | Letters only (e.g. `Male` or `Female`) |

**Example:**
```
Document: 1234567890
Name and surname: John Doe
Age: 25
Sex: Male
→ User John Doe created.
```

---

### 2. Search User
Looks up a user by their document number and displays their information.

**Example:**
```
Document: 1234567890
→ {'name surname': 'John Doe', 'age': '25', 'sex': 'Male'}
```

If the document is not found:
```
→ Document not found.
```

---

### 3. Update User
Updates one or more fields of an existing user. **Leave a field empty to skip it** and keep the current value.

**Example:**
```
Document: 1234567890
New name and surname (leave empty to skip): Jane Doe
New age (leave empty to skip): 
New sex (leave empty to skip): 
→ User updated successfully!
```

---

### 4. Delete User
Removes a user from the system using their document number.

**Example:**
```
Document: 1234567890
→ Deleted user with document 1234567890
```

---

### 5. Exit
Ends the program gracefully.
```
→ Goodbye!
```

---

## 🧠 Functions Reference (`functions.py`)

| Function | Parameters | Returns |
|---|---|---|
| `create_user` | `users, doc, name_surname, age, sex` | Success or error message |
| `search_user` | `users, doc` | User dict or `"Document not found."` |
| `update_user` | `users, doc, name_surname, age, sex` | Success or error message |
| `delete_user` | `users, doc` | Success or error message |

---

## ⚠️ Limitations

- Data is stored **in memory only** — all records are lost when the program exits.
- No file or database persistence.
- Document numbers must be **exactly 10 digits**.

---

## 🛠️ Potential Improvements

- Save and load users from a JSON or CSV file for persistence.
- Add input validation for age range (e.g. 0–120).
- Support listing all users.
- Add a graphical or web interface.

---

## 📄 License

This project is open source and free to use.
