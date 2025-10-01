# python-basics
A structured learning journey into Python fundamentals, starting from Week 1 basics and progressing step by step.  This repository will be updated weekly with practice programs, notes, and mini-projects.

# Week 1: Python Basics & Control Structures  

### 📝 Goal  
Understand the core building blocks of Python.  

### 📌 Topics Covered  
- Variables & Data Types (`int`, `float`, `string`, `boolean`)  
- Operators (`+`, `-`, `*`, `/`, `%`, `//`, `**`)  
- Conditional Statements (`if`, `else`, `elif`)  
- Loops (`for`, `while`)  

### 💻 Practice Programs  
1. **calculator.py** - Simple calculator performing +, -, *, /  
2. **even_odd_checker.py** - Checks if a number is even or odd  
3. **multiplication_table.py** - Generates multiplication table of a number     

# Week 2: Functions, Lists & Dictionaries

### 📝 Goal  
Learn how to organize code and store data efficiently.

### 📌 Topics Covered  
- Defining and calling **functions** (`def`, `return`, parameters)  
- **Lists** → storing items in order (e.g., `[10, 20, 30]`)  
- **Dictionaries** → storing data in key-value pairs (e.g., `{"name": "Alice", "score": 95}`)  

### 💻 Practice Programs  
1. **functions_example.py** – Write a simple function that greets a user  
2. **list_example.py** – Store and display a list of student names  
3. **dictionary_example.py** – Store and display student scores using a dictionary  
4. **student_scores.py** – Store student scores and add a function to calculate the average score

# Week 3: File Handling & Error Handling

###  📝 Goal
Learn how to read and write data to files, and handle errors smoothly.

### 📌 Topics Covered
- Opening, reading, and writing .txt and .csv files in Python (open, read, write, with)
- File modes → "r" (read), "w" (write), "a" (append)
- Error handling with try, except, finally

### 💻 Practice Programs
1. **write_file.py** – Write some text into a file
2. **read_file.py** – Read and display the contents of a file
3. **append_file.py** – Append new text into an existing file
4. **error_handling.py** – Demonstrate error handling using try and except
5. **contact_book.py** – Build a simple contact book that stores names & numbers in a file

# Week 4: Mini Project: Python Application  

### 📝 Goal  
Apply everything you’ve learned so far in a real-world mini project: plan, build, test, and improve a small Python application.  

### 📌 Topics Covered  
- Breaking a problem into input → logic → output → data storage  
- Organizing code with **functions**  
- File handling for saving project data (`.json`, `.txt`, `.csv`)  
- User input handling in CLI apps  
- Testing and improving the program
- (Optional) Using APIs (for projects like Weather Info)  

### 💻 Practice Programs / Files to Create  
1. **todo_cli.py** – Build a To-Do List CLI app (starter code provided below).

# Week 5: Python Modules & Libraries  

### 📝 Goal  
Learn to use external Python tools (libraries) and practice importing modules.  

### 📌 Topics Covered  
- Importing built-in modules (`math`, `random`, `datetime`)  
- Using `random` for generating passwords and random numbers  
- Using `datetime` for working with current date & time  
- Introduction to the idea of external libraries  

### 🛠 Steps to Follow  
1. Learn how to import modules using `import module_name`.  
2. Practice with:  
   - **random** → generate random numbers & passwords  
   - **datetime** → display current date, time, and formatting  
   - **math** → use mathematical functions like `sqrt()`, `factorial()`  
3. Task: Build a **Password Generator** that allows choosing length & symbols.  

### 💻 Practice Programs / Files to Create  
1. **math_demo.py** – Use math module functions like factorial, square root, power.  
2. **datetime_demo.py** – Print current date & time in different formats.  
3. **random_demo.py** – Show random number, random choice, dice simulator.  
4. **password_generator.py** – Generate secure passwords with custom length & symbols.

# Week 6: APIs and JSON

### 🎯 Goal
Work with real-world data from the internet using APIs and JSON.

### 📌 Topics Covered
- What APIs (Application Programming Interfaces) are
- Using the requests library to fetch API data
- Parsing data with the json module
- Building small applications (Weather App, News App)

### 🛠 Steps to Follow
1. Learn the basics of APIs and JSON.
2. Install & use requests to fetch data from a URL.
3. Parse the response with json() and extract useful information.
4. Build a simple Weather App or News App that uses real data.

### 💻 Practice Programs / Files to Create
1. fetch_api.py – Basic fetch from an API and display JSON response.
2. weather_app.py – Get city weather details from OpenWeatherMap API.
3. news_app.py – Fetch and display top headlines using News API.

# Week 8: Final Mini Project

### 🎯 Goal
Learn how to analyze and manipulate data using Pandas.

### 📚 Topics Covered
- Installing and importing Pandas
- Loading CSV data with pd.read_csv()
- Exploring data with .head(), .info(), .describe()
- Grouping and summarizing data using .groupby()
- Basic data cleaning and filtering

### 🛠 Steps to Follow
1. Install Pandas if not already installed:
   pip install pandas
2. Import Pandas in Python:
   import pandas as pd
3. Load a dataset (CSV file) using pd.read_csv("filename.csv").
4. Explore the data using:
.head() → first 5 rows
.describe() → statistics summary
.info() → dataset overview
5. Perform simple analysis with .groupby() and filtering.

### 💻 Practice Programs 
1. load_csv.py – Load and display a CSV file.
2. explore_data.py – Use .head(), .describe(), .info() to understand the data.
3. groupby_demo.py – Group data (e.g., average marks by subject, expenses by category).
4. analysis_task.py – Your own mini analysis project (marks, COVID, or expenses).

# Week 7: Data Analysis with Pandas

### 🎯 Goal
Apply everything learned so far by building a meaningful Python project.

### 📚 Topics Covered
- Breaking down a project into smaller steps (input → logic → output → save data)
- Using functions to organize code
- File handling & error handling
- Working with APIs / CSV files
- Building a complete mini project

### 🛠 Steps to Follow
1. Pick one project idea (File Organizer, Student Result System, Daily Expense Tracker, or Stock Tracker).
2. Plan the workflow: take inputs, process logic, display output, and save data.
3. Use Python concepts: functions, loops, file handling, exceptions, and libraries.
4. Test the program with different inputs and refine it.

### 💻 Practice Programs 
1. file_organizer.py – Organizes files into folders (Documents, Images, CSV, etc.).
2. student_result_system.py – Stores marks, calculates averages, and displays results.
3. daily_expense_tracker.py – Tracks expenses and saves them into a CSV file.
4. stock_tracker.py – Fetches stock prices using an API and displays updates.
  

