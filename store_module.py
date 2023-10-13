import tkinter as tk
import pickle
from tkinter import ttk, scrolledtext, messagebox
from PIL import Image, ImageTk

# Define global variables
storeEntryEntry = None  # Entry widget for store number
districtEntry = None    # Entry widget for district
shipmentEntry = None    # Entry widget for shipping number
scacEntry = None        # Entry widget for SCAC code
sealEntry = None        # Entry widget for seal number
trailerNumEntry = None  # Entry widget for trailer number
pickupEntry = None      # Entry widget for pickup time
amPmCombobox = None     # Combobox for AM/PM selection
all_data_text = None    # ScrolledText widget to display all data
deleteEntry = None      # Entry widget to enter shipment number to delete

def sort_by_store_number():
    # Function to sort data by store number
    data_list = []
    with open("../data.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data.get("Store Number").isdigit():
                    data_list.append(data)
                else:
                    messagebox.showerror("Error", "Some records have invalid store numbers.")
            except EOFError:
                break

    if not data_list:
        messagebox.showerror("Error", "There are no valid records to sort.")
        return

    sorted_data = sorted(data_list, key=lambda x: int(x.get("Store Number")))
    display_all_data(sorted_data)

def sort_by_shipment_number():
    # Function to sort data by shipment number
    data_list = []
    with open("../data.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data.get("Shipping Number").isdigit():
                    data_list.append(data)
                else:
                    messagebox.showerror("Error", "Some records have invalid shipment numbers.")
            except EOFError:
                break

    if not data_list:
        messagebox.showerror("Error", "There are no valid records to sort.")
        return

    sorted_data = sorted(data_list, key=lambda x: int(x.get("Shipping Number")))
    display_all_data(sorted_data)

def is_valid_number(input_str):
    # Function to check if a string is a valid number
    return input_str.isdigit()

def save_data():
    # Function to save entered data
    store_number = storeEntryEntry.get()
    district = districtEntry.get()
    shipping_number = shipmentEntry.get()
    scac_code = scacEntry.get()
    seal_number = sealEntry.get()
    trailer_number = trailerNumEntry.get()
    pickup_time = pickupEntry.get()
    am_pm = amPmCombobox.get()

    # Validate input fields
    if not all([store_number, district, shipping_number, scac_code, seal_number, trailer_number, pickup_time, am_pm]):
        # Show an error message using messagebox
        messagebox.showerror("Error", "All fields must be filled.")
        return

    if not is_valid_number(store_number) or not is_valid_number(seal_number):
        # Show an error message if store number or seal number is not a valid number
        messagebox.showerror("Error", "Store Number and Seal Number must be valid numbers.")
        return

    pickup_time = f"{pickup_time} {am_pm}"

    data = {
        "Store Number": store_number,
        "District": district,
        "Shipping Number": shipping_number,
        "SCAC Code": scac_code,
        "Seal Number": seal_number,
        "Trailer Number": trailer_number,
        "Pickup Time": pickup_time
    }

    with open("../data.pkl", "ab") as file:
        pickle.dump(data, file)

    clear_input_boxes()

def delete_data():
    # Function to delete data by Shipment Number
    shipment_number = deleteEntry.get()

    # Validate the input field
    if not shipment_number:
        # Show an error message using messagebox
        messagebox.showerror("Error", "Shipment Number must be entered.")
        return

    data_list = []

    with open("../data.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data["Shipping Number"] != shipment_number:
                    data_list.append(data)
            except EOFError:
                break

    with open("../data.pkl", "wb") as file:
        for data in data_list:
            pickle.dump(data, file)

    deleteEntry.delete(0, tk.END)

def display_all_data(data_list=None):
    # Function to display all entered data
    all_data_text.config(state=tk.NORMAL)  # Enable text widget for editing

    if data_list is None:
        all_data_text.delete(1.0, tk.END)
        with open("../data.pkl", "rb") as file:
            while True:
                try:
                    data = pickle.load(file)
                    for key, value in data.items():
                        all_data_text.insert(tk.END, f"{key}: {value}\n")
                    all_data_text.insert(tk.END, "\n")
                except EOFError:
                    break
    else:
        all_data_text.delete(1.0, tk.END)
        for data in data_list:
            for key, value in data.items():
                all_data_text.insert(tk.END, f"{key}: {value}\n")
            all_data_text.insert(tk.END, "\n")

    all_data_text.config(state=tk.DISABLED)  # Disable text widget for editing

def clear_input_boxes():
    # Function to clear input fields
    storeEntryEntry.delete(0, tk.END)
    districtEntry.delete(0, tk.END)
    shipmentEntry.delete(0, tk.END)
    scacEntry.delete(0, tk.END)
    sealEntry.delete(0, tk.END)
    trailerNumEntry.delete(0, tk.END)
    pickupEntry.delete(0, tk.END)

def create_data_entry_page(tab_control):
    # Function to create the Data Entry page
    data_entry_frame = ttk.Frame(tab_control)
    tab_control.add(data_entry_frame, text="Data Entry")

    storeLabel = tk.Label(data_entry_frame, text="Enter store number", font=("Cambria", 14), bg='darkgoldenrod', fg='black')
    districtLabel = tk.Label(data_entry_frame, text="Enter the district", font=("Cambria", 14), bg='darkgoldenrod', fg='black')
    shipmentLabel = tk.Label(data_entry_frame, text="Enter the shipping number", font=("Cambria", 14), bg='darkgoldenrod', fg='black')
    scacLabel = tk.Label(data_entry_frame, text="Enter in the SCAC code", font=("Cambria", 14), bg='darkgoldenrod', fg='black')
    sealLabel = tk.Label(data_entry_frame, text="Enter the Seal Number", font=("Cambria", 14), bg='darkgoldenrod', fg='black')
    trailerNumLabel = tk.Label(data_entry_frame, text="Trailer Number", font=("Cambria", 14), bg='darkgoldenrod', fg='black')
    pickupLabel = tk.Label(data_entry_frame, text="Enter the Pick Up time", font=("Cambria", 14), bg='darkgoldenrod', fg='black')

    storeLabel.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    districtLabel.grid(row=1, column=0, sticky='w', padx=10, pady=5)
    shipmentLabel.grid(row=2, column=0, sticky='w', padx=10, pady=5)
    scacLabel.grid(row=3, column=0, sticky='w', padx=10, pady=5)
    sealLabel.grid(row=4, column=0, sticky='w', padx=10, pady=5)
    trailerNumLabel.grid(row=5, column=0, sticky='w', padx=10, pady=5)
    pickupLabel.grid(row=6, column=0, sticky='w', padx=10, pady=5)

    global storeEntryEntry, districtEntry, shipmentEntry, scacEntry, sealEntry, trailerNumEntry, pickupEntry, amPmEntry

    storeEntryEntry = tk.Entry(data_entry_frame, foreground="black", background="khaki", font=("Cambria", 14), width=10)
    districtEntry = tk.Entry(data_entry_frame, foreground="black", background="khaki", font=("Cambria", 14), width=10)
    shipmentEntry = tk.Entry(data_entry_frame, foreground="black", background="khaki", font=("Cambria", 14), width=10)
    scacEntry = tk.Entry(data_entry_frame, foreground="black", background="khaki", font=("Cambria", 14), width=10)
    sealEntry = tk.Entry(data_entry_frame, foreground="black", background="khaki", font=("Cambria", 14), width=10)
    trailerNumEntry = tk.Entry(data_entry_frame, foreground="black", background="khaki", font=("Cambria", 14), width=10)
    pickupEntry = tk.Entry(data_entry_frame, foreground="black", background="khaki", font=("Cambria", 14), width=5)
    amPmEntry = tk.Entry(data_entry_frame, foreground="black", background="khaki", font=("Cambria", 14), width=5)

    storeEntryEntry.grid(row=0, column=1, padx=10, pady=5)
    districtEntry.grid(row=1, column=1, padx=10, pady=5)
    shipmentEntry.grid(row=2, column=1, padx=10, pady=5)
    scacEntry.grid(row=3, column=1, padx=10, pady=5)
    sealEntry.grid(row=4, column=1, padx=10, pady=5)
    trailerNumEntry.grid(row=5, column=1, padx=10, pady=5)
    pickupEntry.grid(row=6, column=1, padx=10, pady=5)
    amPmEntry.grid(row=6, column=2, padx=0, pady=5)

    amPmLabel = tk.Label(data_entry_frame, text="AM/PM", font=("Cambria", 14), bg='darkgoldenrod', fg='black')
    amPmLabel.grid(row=6, column=3, sticky='w')

    am_pm_values = ("AM", "PM")
    global amPmCombobox
    amPmCombobox = ttk.Combobox(data_entry_frame, values=am_pm_values, font=("Cambria", 14), width=5)
    amPmCombobox.grid(row=6, column=4)

    save_button = tk.Button(
        data_entry_frame,
        text="Save",
        foreground="black",
        background="green",
        command=save_data,
        font=("Cambria", 14)
    )

    save_button.grid(row=7, column=1, padx=10, pady=5)

def create_data_display_page(tab_control):
    # Function to create the Data Display page
    data_display_frame = ttk.Frame(tab_control)
    tab_control.add(data_display_frame, text="Data Display")

    global all_data_text
    all_data_text = scrolledtext.ScrolledText(data_display_frame, wrap=tk.WORD, width=60, height=10, font=("Cambria", 12), bg='black', fg='limegreen')
    all_data_text.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    all_data_text.config(state=tk.DISABLED)  # Disable text widget for editing

    refresh_button = tk.Button(data_display_frame, text="Refresh Data", command=display_all_data, font=("Cambria", 14))
    refresh_button.grid(row=1, column=0)

    sort_store_button = tk.Button(data_display_frame, text="Sort by Store Number", command=sort_by_store_number, font=("Cambria", 14))
    sort_store_button.grid(row=2, column=0)

    sort_shipment_button = tk.Button(data_display_frame, text="Sort by Shipment Number", command=sort_by_shipment_number, font=("Cambria", 14))
    sort_shipment_button.grid(row=3, column=0)

    # Create a label and entry for entering the shipment number to delete
    deleteLabel = tk.Label(data_display_frame, text="Enter Shipment Number to Delete", font=("Cambria", 14), bg='dark gray', fg='white')
    global deleteEntry
    deleteEntry = tk.Entry(data_display_frame, foreground="black", background="light gray", font=("Cambria", 14))
    deleteLabel.grid(row=1, column=1)
    deleteEntry.grid(row=2, column=1)

    # Create a button to initiate the deletion
    delete_button = tk.Button(data_display_frame, text="Delete by Shipment Number", command=delete_data, font=("Cambria", 14))
    delete_button.grid(row=3, column=1, padx=10, pady=10)