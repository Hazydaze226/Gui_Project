import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk
import store_module

def main():
    master = tk.Tk()
    master.title("Store data")
    master.geometry("600x500")
    master.configure(bg='darkslategray')
    tab_control = ttk.Notebook(master)
    tab_control.grid(row=0, column=2, rowspan=10, columnspan=10)

    store_module.create_data_entry_page(tab_control)
    store_module.create_data_display_page(tab_control)

    # Load and resize the images using PIL
    package_box_image = Image.open("package-box.png")
    package_box_image = package_box_image.resize((50, 50))  # Resize to your preferred dimensions
    package_box_photo = ImageTk.PhotoImage(package_box_image)

    delivery_truck_image = Image.open("delivery-truck.png")
    delivery_truck_image = delivery_truck_image.resize((50, 50))  # Resize to your preferred dimensions
    delivery_truck_photo = ImageTk.PhotoImage(delivery_truck_image)

    # Create Labels to display the resized images
    package_box_label = tk.Label(master, image=package_box_photo)
    package_box_label.image = package_box_photo  # To prevent image from being garbage collected
    package_box_label.grid(row=10, column=4, padx=10, pady=10)

    delivery_truck_label = tk.Label(master, image=delivery_truck_photo)
    delivery_truck_label.image = delivery_truck_photo  # To prevent image from being garbage collected
    delivery_truck_label.grid(row=10, column=6, padx=10, pady=10)

    # Create an Exit button
    exit_button = tk.Button(master, text="Exit", command=master.quit, font=("Cambria", 14), background="red", foreground="white")
    exit_button.grid(row=10, column=5, padx=10, pady=10)

    master.mainloop()

if __name__ == "__main__":
    main()