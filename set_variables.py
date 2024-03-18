import tkinter as tk
from tkinter import simpledialog

# Create a function to get user input
def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Prompt user for input
    global apath, music_dir, email_id, email_pwd, sendemail_id, News_Api, api_key
    apath = simpledialog.askstring("Input", "Enter path for apath:")
    music_dir = simpledialog.askstring("Input", "Enter path for music_dir:")
    email_id = simpledialog.askstring("Input", "Enter your email ID:")
    email_pwd = simpledialog.askstring("Input", "Enter your email password:", show="*")
    sendemail_id = simpledialog.askstring("Input", "Enter email ID to send to:")
    News_Api = simpledialog.askstring("Input", "Enter your News API key:")
    api_key = simpledialog.askstring("Input", "Enter your OpenWeatherMap API key:")
    
    # Destroy the root window after input is provided
    root.destroy()

# Function to write variables to a file
def write_variables_to_file(filename):
    with open(filename, 'w') as f:
        f.write(f"apath={apath}\n")
        f.write(f"music_dir={music_dir}\n")
        f.write(f"email_id={email_id}\n")
        f.write(f"email_pwd={email_pwd}\n")
        f.write(f"sendemail_id={sendemail_id}\n")
        f.write(f"News_Api={News_Api}\n")
        f.write(f"api_key={api_key}\n")

# Get user input
get_user_input()

# Write variables to a file
write_variables_to_file("variables.txt")


# Now you can use the variables as needed
print(apath)
print(music_dir)
print(email_id)
print(email_pwd)
print(sendemail_id)
print(News_Api)
print(api_key)
