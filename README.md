# Inventory System with CSV Persistence (Python)

## Description
This project is a console-based inventory management system developed in Python. It allows users to manage products through CRUD operations and persist data using CSV files.

The system supports adding, displaying, searching, updating, and deleting products, as well as calculating statistics and saving/loading data between sessions.

---

## Objective
The main goal of this project is to:
- Manage an inventory using lists and dictionaries  
- Apply CRUD operations (Create, Read, Update, Delete)  
- Calculate business statistics  
- Implement file persistence using CSV  
- Handle errors and validate user input  
- Structure code using functions and modules  

---

## Features

### CRUD Operations
- Add new products (name, price, amount)  
- Show all stored products  
- Search for a product by name  
- Update product information  
- Delete products from inventory  

---

### Statistics
The system calculates:
- Total units in stock  
- Total inventory value  
- Most expensive product  
- Least expensive product  

It also shows subtotals per product using a `lambda` function.

---

### CSV Persistence

#### Save Data
- Exports inventory to a CSV file (`products.csv`)  
- Includes headers: name, price, amount  
- Writes all product data in a structured format  

#### Load Data
- Reads data from a CSV file  
- Converts values to correct data types  
- Clears current inventory before loading  
- Handles errors like missing files  

---

## Data Structure
The inventory is stored as a list of dictionaries.  
Each product contains:
- name  
- price  
- amount  

This structure allows easy manipulation and access to product data.

---

##  Program Flow

The system follows these steps:

1. **Input**  
   The user enters product data or selects an option from the menu  

2. **Processing**  
   The program validates data, performs calculations, or modifies the inventory  

3. **Output**  
   Results are displayed in the console or saved to a file  

---

##  Validation & Error Handling
- Price and amount are validated as numeric values  
- Invalid inputs are handled without crashing the program  
- File operations use `try/except` to prevent errors  
- Missing file detection (`FileNotFoundError`)  

---

##  Modular Design
The code is organized into functions for:
- Product management  
- Statistics calculation  
- File handling (CSV)  

Each function has a specific responsibility, making the code cleaner and easier to maintain.

---

##  Menu Options
The system is designed to support a menu with options such as:
1. Add product  
2. Show inventory  
3. Search product  
4. Update product  
5. Delete product  
6. Show statistics  
7. Save to CSV  
8. Load from CSV  
9. Exit  

---

## Flow Chart
![Week 3 Flow Chart](https://github.com/user-attachments/assets/c81eb0a2-24ca-4138-a26b-e376b9b31ac0)

---

## 📝 Conclusion
This project demonstrates how to build a complete and functional inventory system using Python. It integrates fundamental programming concepts with file persistence, allowing data to be stored, reused, and managed efficiently.
