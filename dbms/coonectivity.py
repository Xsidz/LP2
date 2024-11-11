import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

# CRUD Functions
def create():
    try:
        record = {
            "ID": entry_id.get(),
            "Name": entry_name.get()
        }
        if collection.find_one({"ID": record["ID"]}):
            messagebox.showerror("Error", "ID already exists!")
        else:
            collection.insert_one(record)
            messagebox.showinfo("Success", "Record added successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def read():
    try:
        result = collection.find_one({"ID": entry_id.get()})
        if result:
            entry_name.delete(0, tk.END)
            entry_name.insert(0, result["Name"])
            messagebox.showinfo("Success", "Record found!")
        else:
            messagebox.showerror("Error", "Record not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update():
    try:
        query = {"ID": entry_id.get()}
        new_values = {"$set": {"Name": entry_name.get()}}
        result = collection.update_one(query, new_values)
        if result.matched_count > 0:
            messagebox.showinfo("Success", "Record updated successfully!")
        else:
            messagebox.showerror("Error", "Record not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete():
    try:
        query = {"ID": entry_id.get()}
        result = collection.delete_one(query)
        if result.deleted_count > 0:
            entry_id.delete(0, tk.END)
            entry_name.delete(0, tk.END)
            messagebox.showinfo("Success", "Record deleted successfully!")
        else:
            messagebox.showerror("Error", "Record not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create GUI window
root = tk.Tk()
root.title("CRUD with MongoDB")
root.geometry("300x200")

# ID input
tk.Label(root, text="ID:").grid(row=0, column=0, padx=10, pady=10)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

# Name input
tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

# CRUD buttons
tk.Button(root, text="Create", command=create).grid(row=2, column=0, pady=10)
tk.Button(root, text="Read", command=read).grid(row=2, column=1, pady=10)
tk.Button(root, text="Update", command=update).grid(row=3, column=0, pady=10)
tk.Button(root, text="Delete", command=delete).grid(row=3, column=1, pady=10)

root.mainloop()