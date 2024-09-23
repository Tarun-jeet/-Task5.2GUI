from tkinter import *
from gpiozero import PWMLED

# I'm initializing the PWM LEDs for Red, Green, and Blue on GPIO pins 16, 17, and 18.
red_led = PWMLED(16)
green_led = PWMLED(17)
blue_led = PWMLED(18)

# creating the main window for the GUI.
window = Tk()
window.title('LED Intensity Control')  # Giving the window a meaningful title
window.minsize(800, 500)  # Setting a minimum size for the window

# This function updates the intensity of the Red LED based on the slider value.
def update_red(value):
    red_intensity = float(value)
    red_led.value = red_intensity
    print(f"Red Intensity: {red_intensity}")  # Printing the current intensity for monitoring

# This function updates the intensity of the Green LED.
def update_green(value):
    green_intensity = float(value)
    green_led.value = green_intensity
    print(f"Green Intensity: {green_intensity}")

# This function updates the intensity of the Blue LED.
def update_blue(value):
    blue_intensity = float(value)
    blue_led.value = blue_intensity
    print(f"Blue Intensity: {blue_intensity}")

#a label to address functionality
label = Label(window, text="SLIDE TO WATCH INTENSITY VARIATION", font=("Arial", 16, "bold"), fg="black")
label.pack(pady=20)

#the exit buttom using lambda expression for adding multiple functions in the command
button=Button(window, text='EXIT',background="#808080",fg="#202020",command=lambda:[window.destroy(),red_led.close(),green_led.close(),blue_led.close()])
button.pack(side=BOTTOM)

# I'm creating a customized slider for the Red LED and similar for other ones
red_scale = Scale(window, from_=0.0, to=1.0, orient='horizontal', length=300, resolution=0.01, command=update_red, label="Red LED", fg='red', troughcolor='pink')
red_scale.pack(pady=20)  # Adding some vertical spacing (padding) for neatness

green_scale = Scale(window, from_=0.0, to=1.0, orient='horizontal', length=300, resolution=0.01, command=update_green, label="Green LED", fg='green', troughcolor='lightgreen')
green_scale.pack(pady=20)

blue_scale = Scale(window, from_=0.0, to=1.0, orient='horizontal', length=300, resolution=0.01, command=update_blue, label="Blue LED", fg='blue', troughcolor='lightblue')
blue_scale.pack(pady=20)

#starting the main event loop for the window to keep it open
window.mainloop()