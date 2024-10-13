from tkinter import Button, Entry
from canvas import root, frame
from helpers import clean_screen, get_password_hash
from json import dump, loads  # dump gets a dictionary and adds it .txt file as json format, loads gets string->dict
from buying_page import display_products


def get_users_data():
    info_data = []

    with open("db/users_information.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def render_entry():
    register_button = Button(
        root,
        text='Register',    # text of the button
        bg='green',     # background color
        fg='white',     # foreground color (font color)
        bd=0,           # border properties. Here we don't want to have a border
        width=9,        # button width
        height=1,       # button height
        command=register    # when register button is clicked it will run the register function(this is a reference)
    )

    frame.create_window(350, 260, window=register_button)   # creating a window for the current button

    login_button = Button(
        root,
        text='Log in',
        bg='blue',
        fg='white',
        bd=0,
        width=9,
        height=1,
        command=login
    )

    frame.create_window(350, 260, window=register_button)  # creating a window for the current button
    frame.create_window(350, 300, window=login_button)


def register():
    clean_screen()
    frame.create_text(100, 50, text="First Name:")     # creating a text for the first name
    frame.create_text(100, 100, text="Last Name:")     # creating a text for the last name
    frame.create_text(100, 150, text="Username:")     # creating a text for the username
    frame.create_text(100, 200, text="Password:")     # creating a text for the password

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        bd=0,
        width=7,
        height=1,
        command=registration
    )

    frame.create_window(200, 250, window=register_button)


def registration():
    info_dict = {
        "First name": first_name_box.get(),     # collects information for every credential
        "Last name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get(),
    }

    if check_registration(info_dict):
        with open("db/users_information.txt", "a") as users_file:
            info_dict["Password"] = get_password_hash(info_dict["Password"])
            dump(info_dict, users_file)   # get the info dictionary and paste it into the users_file as the right format
            users_file.write("\n")
            display_products()


def check_registration(info_dict):
    frame.delete("error")   # deletes everything that has errors

    for key, value in info_dict.items():
        if not value.strip():
            frame.create_text(
                200,
                300,
                text=f"{key} cannot be empty!",
                fill="red",
                tags="error",
            )

            return False

    users_data = get_users_data()

    for user in users_data:
        if user["Username"] == info_dict["Username"]:
            frame.create_text(
               200,
               300,
               text="Username is already taken!",
               fill="red",
               tags="error",
            )

            return False

    return True


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username:")
    frame.create_text(100, 80, text="Password:")

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 80, window=password_box)

    frame.create_window(200, 120, window=login_button)


def logging():
    if check_login():
        display_products()

    else:
        frame.create_text(
            200,
            150,
            text="Invalid username or password!",
            fill="red",
            tags="error",
        )


def check_login():
    users_data = get_users_data()

    user_username = username_box.get()
    user_password = get_password_hash(password_box.get())

    for user in users_data:
        current_user_username = user["Username"]
        current_user_password = user["Password"]

        if current_user_username == user_username and current_user_password == user_password:
            return True

    return False


def change_login_button_status(event):
    info = [
        username_box.get(),
        password_box.get(),
    ]

    for element in info:
        if not element.strip():
            login_button["state"] = "disabled"
            break

    else:
        login_button["state"] = "normal"


first_name_box = Entry(root, bd=0, bg="grey")      # defining a box for typing for all credentials
last_name_box = Entry(root, bd=0, bg="grey")
username_box = Entry(root, bd=0, bg="grey")
password_box = Entry(root, bd=0, bg="grey", show="*")   # show="*" means that the password will not be visible on screen

login_button = Button(
    root,
    text="Login",
    bg="blue",
    fg="white",
    bd=0,
    width=7,
    height=1,
    command=logging
)

login_button["state"] = "disabled"      # state is an option, which now is disabled because there is no credentials

root.bind("<KeyRelease>", change_login_button_status) # if user release keyboard button change_login_button_status will be called
