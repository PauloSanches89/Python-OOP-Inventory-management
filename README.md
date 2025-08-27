# 🥿 Shoe Inventory Manager

This is a command line interface, Python-based, inventory management system for a shoe retail store. It reads from and writes to a `.txt` file, allowing the user to manage product stock, restock low inventory, view item values, and identify sale items.

---

## 📁 Files

* `inventory.txt` – The main database file containing stock records.
* `shoe_manager.py` – Python script containing the Shoe class and logic.
* `README.md` – This file, describing the program, how it works, and how to use it.

---

## 🧠 What This Program Does

| Feature                       | Description                                                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------- |
| 🔄 **Capture New Shoes**      | Add a new product to the inventory and update the database.                                   |
| 📄 **View All Shoes**         | Display all current shoe data in a tabular format.                                            |
| 🧮 **Re-Stock**               | Check for the product with the lowest stock, prompt for restocking, and update the inventory. |
| 🔍 **Search by Product Code** | Search and display a specific shoe's data by entering the stock code (e.g., `SKU12345`).      |
| 💰 **Value Per Item**         | Calculate and show the total value of each shoe (cost × quantity).                            |
| 📢 **Highest Quantity**       | Identify the item with the highest quantity and mark it as ON SALE.                       |
| 📦 **Auto File Update**       | Every change made through the app is saved back to `inventory.txt`.                           |

---

## 🧱 How It Works

* All data is stored in `inventory.txt` in this format:
  `Country,Code,Product,Cost,Quantity`

* On program start, it reads from `inventory.txt` into `Shoe` objects using the `read_shoes_data()` function.

* The main menu repeats in a loop until the user chooses to quit. Each option triggers a different function.

---

## 🧾 Example Inventory File Format

```
Country,Code,Product,Cost,Quantity
South Africa,SKU10001,Nike Air Zoom,1200,20
USA,SKU10002,Adidas Ultraboost,1500,15
Germany,SKU10003,Puma RS-X,1000,25
```

---

## 🔧 Functions Overview

| Function                | Description                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------- |
| `Shoe` class            | Encapsulates all shoe attributes and methods like `get_cost()` and `get_quantity()` |
| `capture_shoes()`       | Adds new shoe object and updates inventory file                                     |
| `view_all()`            | Displays all shoe records in a formatted table using `tabulate`                     |
| `re_stock()`            | Finds lowest quantity item and updates it if user agrees                            |
| `seach_shoe()`          | Search for a shoe by product code                                                   |
| `value_per_item()`      | Displays total value of each shoe type                                              |
| `highest_qty()`         | Displays the product with the highest quantity as ON SALE                       |
| `verify_product_code()` | Validates user-entered product codes follow the `SKU#####` format                   |
| `get_int()`             | Validates and retrieves positive integers from user input                           |

---

## ✅ Requirements

* Python 3.x
* `tabulate` library (install using `pip install tabulate` if not already available)

---

## 🚀 How to Run

1. Ensure `inventory.txt` is in the same folder as your Python script.
2. Run the script:

   ```bash
   python shoe_manager.py
   ```
3. Use the interactive menu to manage your shoe inventory.

---

## 📌 Notes

* The product code must follow the format `SKU#####` (e.g., `SKU10001`).
* The program prevents negative values and handles incorrect input gracefully.
* It uses a class-based design for better data management and extensibility.

---
