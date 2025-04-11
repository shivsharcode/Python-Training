import tkinter as tk
import random
import math
import time


class SpinningWheel:
    def __init__(self, root):
        self.root = root
        self.root.title("Spinning Wheel Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.choices = []  # Stores user choices
        self.angle = 0  # Initial angle of rotation
        self.spinning = False  # Flag to track spin state

        # User input field
        self.entry = tk.Entry(root, width=30)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Choice", command=self.add_choice)
        self.add_button.pack()

        # Spin button
        self.spin_button = tk.Button(root, text="Spin", command=self.start_spin)
        self.spin_button.pack()

    def add_choice(self):
        choice = self.entry.get()
        if choice:
            self.choices.append(choice)
            self.entry.delete(0, tk.END)
            self.draw_wheel()

    def draw_wheel(self):
        self.canvas.delete("all")  # Clear canvas
        if not self.choices:
            return

        num_choices = len(self.choices)
        center_x, center_y = 200, 200
        radius = 150
        angle_step = 360 / num_choices

        for i, choice in enumerate(self.choices):
            start_angle = (self.angle + i * angle_step) % 360
            end_angle = (self.angle + (i + 1) * angle_step) % 360

            x1 = center_x + radius * math.cos(math.radians(start_angle))
            y1 = center_y + radius * math.sin(math.radians(start_angle))
            x2 = center_x + radius * math.cos(math.radians(end_angle))
            y2 = center_y + radius * math.sin(math.radians(end_angle))

            # Draw segment
            self.canvas.create_polygon(center_x, center_y, x1, y1, x2, y2,
                                       fill=random.choice(["red", "blue", "green", "yellow"]))

            # Draw text
            text_x = center_x + (radius - 40) * math.cos(math.radians(start_angle + angle_step / 2))
            text_y = center_y + (radius - 40) * math.sin(math.radians(start_angle + angle_step / 2))
            self.canvas.create_text(text_x, text_y, text=choice, font=("Arial", 12, "bold"), fill="black")

        # Draw a pointer
        self.canvas.create_polygon(190, 50, 210, 50, 200, 30, fill="black")

    def start_spin(self):
        if not self.choices or self.spinning:
            return

        self.spinning = True
        self.angle = random.randint(0, 360)  # Start from a random position
        spin_time = 3  # Duration of spin in seconds
        deceleration = 0.95  # Slow down factor
        speed = 20  # Initial speed of rotation

        start_time = time.time()
        while time.time() - start_time < spin_time:
            self.angle += speed
            speed *= deceleration  # Gradually slow down
            self.draw_wheel()
            self.root.update()
            time.sleep(0.05)

        self.spinning = False
        self.display_result()

    def display_result(self):
        num_choices = len(self.choices)
        angle_step = 360 / num_choices
        index = int((self.angle % 360) / angle_step)
        winner = self.choices[index]
        self.canvas.create_text(200, 370, text=f"Winner: {winner}", font=("Arial", 14, "bold"), fill="black")


# Run the application
root = tk.Tk()
app = SpinningWheel(root)
root.mainloop()
