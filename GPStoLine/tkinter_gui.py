import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from video_to_line import VideoToLine
import os

def browse_input_path():
    """Open a file dialog to select the input file and update the entry field."""
    input_path = filedialog.askopenfilename(title="Select Input File")
    if input_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_path)

def browse_output_path():
    """Open a file dialog to select the output folder and update the entry field."""
    output_path = filedialog.asksaveasfilename(title="Output KML", filetypes=[("KML files", "*.kml")])
    if output_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_path)

def run_process():
    """Perform an action using the input and output paths."""
    input_path = input_entry.get()
    output_path = output_entry.get()

    if not input_path:
        messagebox.showerror("Error", "Please specify an input path.")
        return
    if not output_path:
        messagebox.showerror("Error", "Please specify an output path.")
        return

    # Example action: print the paths (replace this with your logic)
    print(f"Input path: {input_path}")
    print(f"Output path: {output_path}")
    vtl = VideoToLine(input_video = input_path, save_path = output_path)
    vtl.get_coordinates()
    vtl.create_kml()
    messagebox.showinfo("Success", "Process completed successfully!")

# Create the main application window
root = tk.Tk()
root.title("GoPro Video to Line")

# Create and place the input path components
input_label = tk.Label(root, text="Input Path:")
input_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=5)

input_button = tk.Button(root, text="Browse...", command=browse_input_path)
input_button.grid(row=0, column=2, padx=10, pady=5)

# Create and place the output path components
output_label = tk.Label(root, text="Output KML:")
output_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=5)

output_button = tk.Button(root, text="Browse...", command=browse_output_path)
output_button.grid(row=1, column=2, padx=10, pady=5)

# Add the Run button
run_button = tk.Button(root, text="Run", command=run_process, bg="green", fg="white")
run_button.grid(row=2, column=1, pady=20)
# Add a contact label
contact_label = tk.Label(root, text="Contact Sam Smith at smiths@aks-eng.com for support.")
contact_label.grid(row=3, column=1, pady=5)
# Run the application
root.mainloop()
