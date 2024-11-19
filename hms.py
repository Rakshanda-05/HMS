import tkinter as tk
from tkinter import messagebox

# Simulated database
users = {"admin": "admin"}  # Default user credentials (username: admin, password: admin)
rooms = {
    101: {"type": "Single", "status": "Available", "price": 100},
    102: {"type": "Double", "status": "Available", "price": 150},
    103: {"type": "Suite", "status": "Available", "price": 250},
}

current_user = None


# Functions for the application
def register_user():
    username = reg_username.get()
    password = reg_password.get()

    if username in users:
        messagebox.showerror("Error", "User already exists.")
    elif not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty.")
    else:
        users[username] = password
        messagebox.showinfo("Success", "Registration successful! Please log in.")
        registration_window.destroy()


def login_user():
    global current_user
    username = login_username.get()
    password = login_password.get()

    if username in users and users[username] == password:
        current_user = username
        messagebox.showinfo("Success", f"Welcome {username}!")
        login_window.destroy()
        main_menu()
    else:
        messagebox.showerror("Error", "Invalid credentials.")


def check_availability():
    available_rooms = [f"Room {room}: {details['type']} - ${details['price']}"
                       for room, details in rooms.items() if details["status"] == "Available"]
    if available_rooms:
        messagebox.showinfo("Available Rooms", "\n".join(available_rooms))
    else:
        messagebox.showinfo("Available Rooms", "No rooms available.")


def book_room():
    room_number = room_input.get()
    if not room_number.isdigit():
        messagebox.showerror("Error", "Please enter a valid room number.")
        return

    room_number = int(room_number)
    if room_number in rooms and rooms[room_number]["status"] == "Available":
        rooms[room_number]["status"] = "Booked"
        messagebox.showinfo("Success", f"Room {room_number} has been booked!")
    else:
        messagebox.showerror("Error", "Room not available or invalid room number.")


def checkout_room():
    room_number = room_input.get()
    if not room_number.isdigit():
        messagebox.showerror("Error", "Please enter a valid room number.")
        return

    room_number = int(room_number)
    if room_number in rooms and rooms[room_number]["status"] == "Booked":
        rooms[room_number]["status"] = "Available"
        messagebox.showinfo("Success", f"Room {room_number} has been checked out!")
    else:
        messagebox.showerror("Error", "Room not booked or invalid room number.")


# GUI for Registration
def registration_screen():
    global registration_window, reg_username, reg_password
    registration_window = tk.Tk()
    registration_window.title("Register")

    tk.Label(registration_window, text="Register", font=("Arial", 16)).pack(pady=10)
    tk.Label(registration_window, text="Username:").pack(pady=5)
    reg_username = tk.Entry(registration_window)
    reg_username.pack(pady=5)

    tk.Label(registration_window, text="Password:").pack(pady=5)
    reg_password = tk.Entry(registration_window, show="*")
    reg_password.pack(pady=5)

    tk.Button(registration_window, text="Register", command=register_user).pack(pady=10)
    registration_window.mainloop()


# GUI for Login
def login_screen():
    global login_window, login_username, login_password
    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Login", font=("Arial", 16)).pack(pady=10)
    tk.Label(login_window, text="Username:").pack(pady=5)
    login_username = tk.Entry(login_window)
    login_username.pack(pady=5)

    tk.Label(login_window, text="Password:").pack(pady=5)
    login_password = tk.Entry(login_window, show="*")
    login_password.pack(pady=5)

    tk.Button(login_window, text="Login", command=login_user).pack(pady=10)
    tk.Button(login_window, text="Register", command=lambda: [login_window.destroy(), registration_screen()]).pack(
        pady=5)
    login_window.mainloop()


# Main Menu after Login
def main_menu():
    main_window = tk.Tk()
    main_window.title("Hotel Management System")

    tk.Label(main_window, text="Hotel Management System", font=("Arial", 18), fg="blue").pack(pady=10)

    tk.Button(main_window, text="Check Room Availability", command=check_availability).pack(pady=5)

    global room_input
    tk.Label(main_window, text="Enter Room Number:").pack(pady=5)
    room_input = tk.Entry(main_window)
    room_input.pack(pady=5)

    tk.Button(main_window, text="Book Room", command=book_room).pack(pady=5)
    tk.Button(main_window, text="Checkout Room", command=checkout_room).pack(pady=5)
    tk.Button(main_window, text="Exit", command=main_window.quit).pack(pady=10)

    main_window.mainloop()


# Start the application with login screen
login_screen()
