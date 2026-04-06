👤 User Management System

A simple Python CLI application for managing user records in memory. It allows you to create, search, update, and delete users through an interactive menu.

Each user is identified by a unique 10-digit document number.

📁 Project Structure
user-management-system/
│
├── main.py          # Entry point — runs the interactive menu
└── functions.py     # Core logic — CRUD functions for user management
🚀 Features
Create new users
Search users by document number
Update existing user information
Delete users
Data stored temporarily in memory (no database required)
🧠 How It Works
User data is stored in a Python dictionary
The document number is used as the unique key
Each user contains:
Name
Age
Sex

Example structure:

users = {
    "1234567890": {
        "name": "Juan",
        "age": 20,
        "sex": "M"
    }
}
▶️ Getting Started
Clone the repository or download the files
Open a terminal in the project folder
Run the program:
python main.py
📋 Menu Options

When you run the program, you will see:

1) Create User
2) Search User
3) Update User
4) Delete User
5) Exit Program

Select an option by typing the corresponding number.

⚠️ Notes
The document number must be exactly 10 digits
Data is not persistent (it resets when the program stops)
No external libraries are required
🛠️ Technologies Used
Python 3
Standard Library only
