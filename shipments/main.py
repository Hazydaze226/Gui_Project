import tkinter as tk
import pickle
from tkinter import ttk, scrolledtext

# Define sorting functions here
def sort_by_store_number():
    data_list = []
    with open("data.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                data_list.append(data)
            except EOFError:
                break

    sorted_data = sorted(data_list, key=lambda x: x.get("Store Number"))
    display_all_data(sorted_data)

def sort_by_shipment_number():
    data_list = []
    with open("data.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                data_list.append(data)
            except EOFError:
                break

    sorted_data = sorted(data_list, key=lambda x: x.get("Shipping Number"))
    display_all_data(sorted_data)


def save_data():
    store_number = storeEntryEntry.get()
    district = districtEntry.get()
    shipping_number = shipmentEntry.get()
    scac_code = scacEntry.get()
    seal_number = sealEntry.get()
    trailer_number = trailerNumEntry.get()
    pickup_time = pickupEntry.get()

    data = {
        "Store Number": store_number,
        "District": district,
        "Shipping Number": shipping_number,
        "SCAC Code": scac_code,
        "Seal Number": seal_number,
        "Trailer Number": trailer_number,
        "Pickup Time": pickup_time
    }

    with open("data.pkl", "ab") as file:
        pickle.dump(data, file)

    clear_input_boxes()
def delete_data():
    shipment_number = deleteEntry.get()
    data_list = []

    # Read existing data and filter out the data with the specified shipment number
    with open("data.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data["Shipping Number"] != shipment_number:
                    data_list.append(data)
            except EOFError:
                break

    # Save the filtered data back to the file
    with open("data.pkl", "wb") as file:
        for data in data_list:
            pickle.dump(data, file)

    # Clear the input box
    deleteEntry.delete(0, tk.END)


def search_data():
    search_store_number = searchEntry.get()
    found_data = None

    with open("data.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data["Store Number"] == search_store_number:
                    found_data = data
                    break
            except EOFError:
                break

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

def clear_input_boxes():
    storeEntryEntry.delete(0, tk.END)
    districtEntry.delete(0, tk.END)
    shipmentEntry.delete(0, tk.END)
    scacEntry.delete(0, tk.END)
    sealEntry.delete(0, tk.END)
    trailerNumEntry.delete(0, tk.END)
    pickupEntry.delete(0, tk.END)

def display_result(result):
    result_text.delete(1.0, tk.END)
    for key, value in result.items():
        result_text.insert(tk.END, f"{key}: {value}\n")

def create_data_entry_page(tab_control):
    data_entry_frame = ttk.Frame(tab_control)
    tab_control.add(data_entry_frame, text="Data Entry")

    storeLabel = tk.Label(data_entry_frame, text="Enter store number", font=("Cambria", 14), bg='lemonchiffon', fg='black')
    districtLabel = tk.Label(data_entry_frame, text="Enter the district", font=("Cambria", 14), bg='lemonchiffon', fg='black')
    shipmentLabel = tk.Label(data_entry_frame, text="Enter the shipping number", font=("Cambria", 14), bg='lemonchiffon', fg='black')
    scacLabel = tk.Label(data_entry_frame, text="Enter the SCAC code", font=("Cambria", 14), bg='lemonchiffon', fg='black')
    sealLabel = tk.Label(data_entry_frame, text="Enter the Seal Number", font=("Cambria", 14), bg='lemonchiffon', fg='black')
    trailerNumLabel = tk.Label(data_entry_frame, text="Enter the Trailer Number", font=("Cambria", 14), bg='lemonchiffon', fg='black')
    pickupLabel = tk.Label(data_entry_frame, text="Enter the Pick Up time", font=("Cambria", 14), bg='lemonchiffon', fg='black')

    global storeEntryEntry, districtEntry, shipmentEntry, scacEntry, sealEntry, trailerNumEntry, pickupEntry

    storeEntryEntry = tk.Entry(data_entry_frame, foreground="black", background="bisque", font=("Cambria", 14))
    districtEntry = tk.Entry(data_entry_frame, foreground="black", background="bisque", font=("Cambria", 14))
    shipmentEntry = tk.Entry(data_entry_frame, foreground="black", background="bisque", font=("Cambria", 14))
    scacEntry = tk.Entry(data_entry_frame, foreground="black", background="bisque", font=("Cambria", 14))
    sealEntry = tk.Entry(data_entry_frame, foreground="black", background="bisque", font=("Cambria", 14))
    trailerNumEntry = tk.Entry(data_entry_frame, foreground="black", background="bisque", font=("Cambria", 14))
    pickupEntry = tk.Entry(data_entry_frame, foreground="black", background="bisque", font=("Cambria", 14))

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
        font=("Cambria", 14)
    )

    save_button.grid(row=7, column=1, padx=10, pady=5)

def create_data_display_page(tab_control):
    data_display_frame = ttk.Frame(tab_control)
    tab_control.add(data_display_frame, text="Data Display")

    global all_data_text

    all_data_text = scrolledtext.ScrolledText(data_display_frame, wrap=tk.WORD, width=60, height=10, font=("Cambria", 12), bg='black', fg='limegreen')
    all_data_text.grid(row=0, columnspan=3,)

    refresh_button = tk.Button(data_display_frame, text="Refresh Data", command=display_all_data, font=("Cambria", 14))
    refresh_button.grid(row=1, column=0,)

    sort_store_button = tk.Button(data_display_frame, text="Sort by Store Number", command=sort_by_store_number, font=("Cambria", 14))
    sort_store_button.grid(row=2, column=0,)

    sort_shipment_button = tk.Button(data_display_frame, text="Sort by Shipment Number", command=sort_by_shipment_number, font=("Cambria", 14))
    sort_shipment_button.grid(row=3, column=0,)

    # Create a label and entry for entering the shipment number to delete
    deleteLabel = tk.Label(data_display_frame, text="Enter Shipment Number to Delete", font=("Cambria", 14), bg='dark gray', fg='white')
    global deleteEntry
    deleteEntry = tk.Entry(data_display_frame, foreground="black", background="light gray", font=("Cambria", 14))
    deleteLabel.grid(row=1, column=1, )
    deleteEntry.grid(row=2, column=1,)

    # Create a button to initiate the deletion
    delete_button = tk.Button(data_display_frame, text="Delete by Shipment Number", command=delete_data, font=("Cambria", 14))
    delete_button.grid(row=3, column=1, padx=1, pady=1)

def main():
    master = tk.Tk()
    master.title("Store data")
    master.geometry("600x400")
    master.configure(bg='darkslategray')

    tab_control = ttk.Notebook(master)
    tab_control.grid(row=0, column=0, rowspan=10, columnspan=10,)




    create_data_entry_page(tab_control)
    create_data_display_page(tab_control)

    master.mainloop()

if __name__ == "__main__":
    main()
