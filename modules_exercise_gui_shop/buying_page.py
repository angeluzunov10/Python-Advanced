from tkinter import Button, NW

from PIL import ImageTk, Image
from helpers import clean_screen
from json import load, dump  # load is loading from json
from canvas import frame, root


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    with open("db/products.json", "r") as stock:
        info = load(stock)

    x, y = 150, 50

    for item_name, item_info in info.items():
        pillow_image = Image.open(item_info["image"])
        resized_pillow_image = pillow_image.resize((130, 150))
        item_img = ImageTk.PhotoImage(resized_pillow_image)
        images.append(item_img)
        # keeping the reference to the image so that Tkinter doesn't delete it after the function ends

        frame.create_text(x, y, text=item_name, font=("Comic Sans MS", 12))
        frame.create_image(x, y + 100, image=item_img)

        if item_info["quantity"] > 0:
            color = "green"
            text = f"In stock: {item_info['quantity']}"

            item_button = Button(
                root,
                text="Buy",
                bg="green",
                fg="white",
                font=("Comic Sans MS", 12),
                width=10,
                command=lambda x=item_name, y=info: buy_product(x, y)
            )

            frame.create_window(x, y + 230, window=item_button)
        else:
            color = "red"
            text = "Out of stock"

        frame.create_text(x, y + 200, text=text, fill=color)

        x += 200

        if x >= 650:
            y += 270
            x = 150


def buy_product(product_name, info):
    info[product_name]["quantity"] -= 1

    with open("db/products.json", "w") as stock:
        dump(info, stock)

    display_products()


images = []
