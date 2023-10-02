#Code by Cameron Pace
#this is a GUI used to store shipment information.


import tkinter as tk
import pickle
from tkinter import ttk, scrolledtext

# Define sorting functions here
def sort_by_store_number():
    data_list = []  # Create an empty list to store data
    with open("data.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                data_list.append(data)

            except EOFError:
                break

    # Sort the data list by store number
    sorted_data = sorted(data_list, key=lambda x: x.get("Store Number"))

    # Display the sorted data
    display_all_data(sorted_data)

def sort_by_shipment_number():
    data_list = []  # Create an empty list to store data
    with open("data.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                data_list.append(data)

            except EOFError:
                break

    # Sort the data list by shipment number
    sorted_data = sorted(data_list, key=lambda x: x.get("Shipping Number"))

    # Display the sorted data
    display_all_data(sorted_data)

# Define other functions (save_data, search_data, display_all_data, etc.) here
def save_data():
    # Retrieve data from entry widgets
    store_number = storeEntryEntry.get()
    district = districtEntry.get()
    shipping_number = shipmentEntry.get()
    scac_code = scacEntry.get()
    seal_number = sealEntry.get()
    trailer_number = trailerNumEntry.get()
    pickup_time = pickupEntry.get()

    # Create a dictionary to store the data
    data = {
        "Store Number": store_number,
        "District": district,
        "Shipping Number": shipping_number,
        "Scac Code": scac_code,
        "Seal Number": seal_number,
        "Trailer Number": trailer_number,
        "Pickup Time": pickup_time
    }

    # Save the data to a pickle file
    with open("data.pkl", "ab") as file:
        pickle.dump(data, file)

    # Clear the input boxes
    clear_input_boxes()

def search_data():
    search_store_number = searchEntry.get()
    found_data = None

    # Search for the data in the pickle file
    with open("data.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data["Store Number"] == search_store_number:
                    found_data = data
                    break
            except EOFError:
                break

    # Display the found data or a message
    if found_data:
        display_result(found_data)
    else:
        display_result({"Data not found": ""})

def display_all_data(data_list=None):
    if data_list is None:
        all_data_text.delete(1.0, tk.END)
        with open("data.pkl", "rb") as file:
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

def create_data_entry_page(tab_control):
    data_entry_frame = ttk.Frame(tab_control)
    tab_control.add(data_entry_frame, text="Data Entry")

    storeLabel = tk.Label(data_entry_frame, text="Enter store number", font=("Helvetica", 14), bg='dark grey', fg='white')
    districtLabel = tk.Label(data_entry_frame, text="Enter the district", font=("Helvetica", 14), bg='dark grey', fg='white')
    shipmentLabel = tk.Label(data_entry_frame, text="Enter the shipping number", font=("Helvetica", 14), bg='dark grey', fg='white')
    scacLabel = tk.Label(data_entry_frame, text="Enter the Scac code", font=("Helvetica", 14), bg='dark grey', fg='white')
    sealLabel = tk.Label(data_entry_frame, text="Enter the Seal Number", font=("Helvetica", 14), bg='dark grey', fg='white')
    trailerNumLabel = tk.Label(data_entry_frame, text="Enter the Trailer Number", font=("Helvetica", 14), bg='dark grey', fg='white')
    pickupLabel = tk.Label(data_entry_frame, text="Enter the Pick Up time", font=("Helvetica", 14), bg='dark grey', fg='white')

    global storeEntryEntry, districtEntry, shipmentEntry, scacEntry, sealEntry, trailerNumEntry, pickupEntry

    storeEntryEntry = tk.Entry(data_entry_frame, foreground="black", background="white", font=("Helvetica", 14))
    districtEntry = tk.Entry(data_entry_frame, foreground="black", background="white", font=("Helvetica", 14))
    shipmentEntry = tk.Entry(data_entry_frame, foreground="black", background="white", font=("Helvetica", 14))
    scacEntry = tk.Entry(data_entry_frame, foreground="black", background="white", font=("Helvetica", 14))
    sealEntry = tk.Entry(data_entry_frame, foreground="black", background="white", font=("Helvetica", 14))
    trailerNumEntry = tk.Entry(data_entry_frame, foreground="black", background="white", font=("Helvetica", 14))
    pickupEntry = tk.Entry(data_entry_frame, foreground="black", background="white", font=("Helvetica", 14))

    storeLabel.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    storeEntryEntry.grid(row=0, column=1, padx=10, pady=5)
    districtLabel.grid(row=1, column=0, sticky='w', padx=10, pady=5)
    districtEntry.grid(row=1, column=1, padx=10, pady=5)
    shipmentLabel.grid(row=2, column=0, sticky='w', padx=10, pady=5)
    shipmentEntry.grid(row=2, column=1, padx=10, pady=5)
    scacLabel.grid(row=3, column=0, sticky='w', padx=10, pady=5)
    scacEntry.grid(row=3, column=1, padx=10, pady=5)
    sealLabel.grid(row=4, column=0, sticky='w', padx=10, pady=5)
    sealEntry.grid(row=4, column=1, padx=10, pady=5)
    trailerNumLabel.grid(row=5, column=0, sticky='w', padx=10, pady=5)
    trailerNumEntry.grid(row=5, column=1, padx=10, pady=5)
    pickupLabel.grid(row=6, column=0, sticky='w', padx=10, pady=5)
    pickupEntry.grid(row=6, column=1, padx=10, pady=5)

    save_button = tk.Button(
        data_entry_frame,
        text="Save",
        foreground="white",
        background="green",
        command=save_data,
        font=("Helvetica", 14)
    )

    save_button.grid(row=7, column=1, padx=10, pady=5)

def create_data_display_page(tab_control):
    data_display_frame = ttk.Frame(tab_control)
    tab_control.add(data_display_frame, text="Data Display")

    global all_data_text

    all_data_text = scrolledtext.ScrolledText(data_display_frame, wrap=tk.WORD, width=60, height=15, font=("Helvetica", 12))
    all_data_text.grid(row=0, column=0, padx=20, pady=20)

    refresh_button = tk.Button(data_display_frame, text="Refresh Data", command=display_all_data, font=("Helvetica", 14))
    refresh_button.grid(row=1, column=0, padx=20, pady=10)

    sort_store_button = tk.Button(data_display_frame, text="Sort by Store Number", command=sort_by_store_number, font=("Helvetica", 14))
    sort_store_button.grid(row=2, column=0, padx=20, pady=10)

    sort_shipment_button = tk.Button(data_display_frame, text="Sort by Shipment Number", command=sort_by_shipment_number, font=("Helvetica", 14))
    sort_shipment_button.grid(row=3, column=0, padx=20, pady=10)

def clear_input_boxes():
    # Clear input boxes
    storeEntryEntry.delete(0, tk.END)
    districtEntry.delete(0, tk.END)
    shipmentEntry.delete(0, tk.END)
    scacEntry.delete(0, tk.END)
    sealEntry.delete(0, tk.END)
    trailerNumEntry.delete(0, tk.END)
    pickupEntry.delete(0, tk.END)

def main():
    master = tk.Tk()
    master.title("Store data")
    master.geometry("1000x800")
    master.configure(bg='dark grey')

    tab_control = ttk.Notebook(master)
    tab_control.grid(row=0, column=0, padx=10, pady=10)

    create_data_entry_page(tab_control)
    create_data_display_page(tab_control)

    master.mainloop()

if __name__ == "__main__":
    main()
