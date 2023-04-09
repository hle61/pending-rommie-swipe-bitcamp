#1. User registration and login
#2. Search for roommates based on gender, race, and hobbies
#3. Search for off-campus housing based on location, price range, and other criteria
#4. Gamified questions to help match users with compatible roommates
#5. Messaging system for communication between potential roommates
#6. Reviews and ratings system for housing and roommates

#-> build 3d button that says find my roomnie 
#-> user find their location 
#-> user fill out questions ( their info)

# from flask import Flask, render_template
# from kivy.app import App 
# from kivy.uix.lable import Label
import requests
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
import tkinter as tk

class SwipeScreen(BoxLayout):
    def init(self, **kwargs):
        super().init(**kwargs)
        self.orientation = 'vertical'
        self.images = ['2023-04-09 (1).png', '2023-04-09 (2).png', '2023-04-09.png']
        self.current_image_index = 0
        self.add_widget(Image(source=self.images[self.current_image_index]))
        self.swipe_button = Button(text='Swipe Right', size_hint=(0.2, 0.1), pos_hint={'x': 0.8, 'y': 0.9})
        self.swipe_button.bind(on_press=self.swipe_right)
        self.add_widget(self.swipe_button)

    def swipe_right(self, instance):
        self.current_image_index += 1
        if self.current_image_index >= len(self.images):
            self.current_image_index = 0
        self.clear_widgets()
        self.add_widget(Image(source=self.images[self.current_image_index]))
        self.add_widget(self.swipe_button)

# Retrieve public real estate data
response = requests.get('https://sdat.dat.maryland.gov/RealProperty/Pages/default.aspx')

database = response.json()

# Display the data to the user
for property in database:
    print(f"Property ID: {property['id']}")
    print(f"Address: {property['address']}")
    print(f"Price: {property['price']}")
    print(f"Description: {property['description']}")
    print("--------------")
    
# Ask the user to select a property
selected_property = input("Please enter the ID of the property you want to rent out: ")

# Retrieve the details of the selected property
response = requests.get(f'https://sdat.dat.maryland.gov/RealProperty/Pages/default.aspx{selected_property}')
property_details = response.json()

# Display the details to the user
print(f"Property ID: {property_details['id']}")
print(f"Address: {property_details['address']}")
print(f"Price: {property_details['price']}")
print(f"Description: {property_details['description']}")
print(f"Features: {property_details['features']}")


root = tk.Tk()

timeline_canvas = tk.Canvas(root, bg="white", bd=0, highlightthickness=0)
def show_timeline():
    timeline_canvas.pack(side="left", fill="both", expand=True)
    house_icon.config(relief=tk.SUNKEN)

house_icon = tk.Button(root, text="🏠", font=("Arial", 150), command=show_timeline)
house_icon.pack(side="top", pady=10)

#needs change because circles  needs to be in a zig zag section so we cannot put them in i in range
circle_coords = [(100, 100), (100, 180), (100, 260), (100, 340), (100, 420)]
line_coords = [(120, 120), (120, 160), (120, 200), (120, 240), (120, 280), (120, 320), (120, 360), (120, 400)]
numbers = ["1", "2", "3", "4", "5"]
#change later to customized each 
for i in range(5):
    x, y = circle_coords[i]
    timeline_canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue", outline="black")
    timeline_canvas.create_text(x, y, text=numbers[i], font=("Arial", 16))
    timeline_canvas.create_line(line_coords, width=2)

def login_form():

    login_window = tk.Toplevel(root)
    # Set the title of the window
    login_window.title("Log In")

    # Create a label for the username field
    username_label = tk.Label(login_window, text="Username")
    username_label.pack()

    # Create an entry field for the username
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    # Create a label for the password field
    password_label = tk.Label(login_window, text="Password")
    password_label.pack()

    # Create an entry field for the password
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    # Create a button to submit the form
    submit_button = tk.Button(login_window, text="Log In")
    submit_button.pack()

login_button = tk.Button(root, text="Log In", command=login_form)
login_button.pack()


def signup_form():
    signup_window = tk.Toplevel(root)
    # Set the title of the window
    signup_window.title("Sign Up")

    # Create a label for the name field
    name_label = tk.Label(signup_window, text="Name")
    name_label.pack()

    # Create an entry field for the name
    name_entry = tk.Entry(signup_window)
    name_entry.pack()

    # Create a label for the email field
    email_label = tk.Label(signup_window, text="Email")
    email_label.pack()

    # Create an entry field for the email
    email_entry = tk.Entry(signup_window)
    email_entry.pack()

    # Create a label for the password field
    password_label = tk.Label(signup_window, text="Password")
    password_label.pack()

    # Create an entry field for the password
    password_entry = tk.Entry(signup_window, show="*")
    password_entry.pack()

    # Create a button to submit the form
    submit_button = tk.Button(signup_window, text="Sign Up")
    submit_button.pack()

signup_button = tk.Button(root, text="Sign Up", command=signup_form)
signup_button.pack()

def get_location():
    res = requests.get("Https://ipinfo.io/")
    data = res.json
    city = data["city"]
    state = data["region"]
    return f"{city}, {state}"

def search_house(location, price_range):
    pass

def main():
    print("Welcome to the ideal house and roommie searching app!")
    location = input("Please enter your location(city, states): ")
    school = input("Are you in school? What school do you go to:")
    major = input("What is your major:")
    print("We would like to find the ideal rommate for you? Please answer a few questions that would help us understadn you more as well as your future roommie!")
    a = input("What are your sleeping habits?")
    b = input("How often do you clean your room? Organize, sweep, etc?")
    c = input("Do you enjoy cooking?")
    d = input("Do you enjoy studying in the apt or outside of the apt?")
    e = input("What are your favorite movies/tv shows?")
    f = input("How do you spend your alone time?")


    if not location:
        location = get_location()
        print(f"Your location is {location}")
    
    price_range= input("Please enter your price range (min-max): ")

    search_house(location, price_range)

if __name__ =="__main__":
    main()

root.mainloop()


# login_page = tk.Tk()
# login_page.title("Log In")
# login_page.geometry("300x200")
# login_page.configure(bg= "violet")



# def get_location():
#     location = input("Where would you like to live? ")
#     return location

# login_button = tk.Button(login_page, text = "Log In", bg = "white", command = get_location)
# login_button.pack(pady = 20)

# def search_housing(location):
#     response = requests.get(f"https://api.realestate.com/search?location={location}")
#     results = json.loads(response.text)
# print("Here are some available properties:")

# for property in results["properties"]:
#     print(f"- {property['address']} ({property['price']})")

# def main():
#     location = get_location()
#     search_housing(location)

# if __name__ == "main":
#     main()





