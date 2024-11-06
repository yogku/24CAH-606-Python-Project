import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import threading
import time

# Generate random IP addresses
def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Network Traffic Simulation
class NetworkTrafficSimulator:
    def __init__(self, num_devices, attack_percentage):
        self.num_devices = num_devices
        self.attack_percentage = attack_percentage
        self.traffic_data = []
        self.is_running = False

    def generate_traffic(self):
        self.traffic_data.clear()
        for _ in range(self.num_devices):
            ip = generate_ip()
            port = random.randint(1, 65535)
            timestamp = time.time()
            # Simulate normal vs. malicious traffic
            if random.randint(1, 100) <= self.attack_percentage:
                attack_type = random.choice(["DoS", "Port Scan", "Brute Force"])
                self.traffic_data.append([ip, port, timestamp, attack_type])
            else:
                self.traffic_data.append([ip, port, timestamp, "Normal"])
        return self.traffic_data

    def start_simulation(self):
        self.is_running = True
        while self.is_running:
            self.generate_traffic()
            time.sleep(1)  # simulate traffic every second

    def stop_simulation(self):
        self.is_running = False

# GUI for the Network Security Visualizer
class NetworkSecurityVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Security Visualizer")
        self.simulator = None
        self.simulation_thread = None

        # GUI layout
        self.create_widgets()

    def create_widgets(self):
        # Device Input
        tk.Label(self.root, text="Number of Devices:").grid(row=0, column=0)
        self.device_entry = tk.Entry(self.root)
        self.device_entry.grid(row=0, column=1)

        # Attack Percentage Input
        tk.Label(self.root, text="Attack Percentage (0-100):").grid(row=1, column=0)
        self.attack_entry = tk.Entry(self.root)
        self.attack_entry.grid(row=1, column=1)

        # Buttons
        self.start_button = tk.Button(self.root, text="Start Simulation", command=self.start_simulation)
        self.start_button.grid(row=2, column=0)

        self.stop_button = tk.Button(self.root, text="Stop Simulation", command=self.stop_simulation)
        self.stop_button.grid(row=2, column=1)

        self.visualize_button = tk.Button(self.root, text="Visualize Traffic", command=self.visualize_traffic)
        self.visualize_button.grid(row=3, column=0, columnspan=2)

        # Frame for matplotlib figure
        self.figure_frame = tk.Frame(self.root)
        self.figure_frame.grid(row=4, column=0, columnspan=2, pady=20)

    def start_simulation(self):
        try:
            num_devices = int(self.device_entry.get())
            attack_percentage = int(self.attack_entry.get())
            if num_devices <= 0 or not (0 <= attack_percentage <= 100):
                raise ValueError

            # Create simulator instance
            self.simulator = NetworkTrafficSimulator(num_devices, attack_percentage)
            self.simulation_thread = threading.Thread(target=self.simulator.start_simulation)
            self.simulation_thread.start()
            messagebox.showinfo("Simulation", "Network traffic simulation started.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for devices and attack percentage.")

    def stop_simulation(self):
        if self.simulator:
            self.simulator.stop_simulation()
            if self.simulation_thread:
                self.simulation_thread.join()
            messagebox.showinfo("Simulation", "Network traffic simulation stopped.")

    def visualize_traffic(self):
        if self.simulator is None or len(self.simulator.traffic_data) == 0:
            messagebox.showwarning("No Data", "No traffic data to visualize. Start the simulation first.")
            return

        # Data preparation
        attack_count = {"Normal": 0, "DoS": 0, "Port Scan": 0, "Brute Force": 0}
        for traffic in self.simulator.traffic_data:
            attack_type = traffic[3]
            attack_count[attack_type] += 1

        labels = list(attack_count.keys())
        sizes = list(attack_count.values())
        colors = ['lightblue', 'orange', 'lightgreen', 'red']

        # Clear the figure frame before plotting
        for widget in self.figure_frame.winfo_children():
            widget.destroy()

        # Create Matplotlib pie chart
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  

        # Embed Matplotlib chart in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.figure_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSecurityVisualizer(root)
    root.mainloop()
