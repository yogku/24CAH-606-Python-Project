# Network Security Visualizer

## Overview
The **Network Security Visualizer** is a Python application that simulates network traffic and visualizes normal and malicious traffic patterns. Users can input the number of devices and the percentage of attack traffic, then visualize the results using pie charts.

## Prerequisites
Before installing the application, ensure you have the following installed on your machine:
- Python 3.x
- pip (Python package installer)

## Installation Instructions

### For Windows

1. **Install Python**: Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/windows/). Ensure you check the box to add Python to your PATH during installation.

2. **Clone the Repository**: Open Command Prompt (cmd) and clone the repository using Git:
   ```bash
   git clone https://github.com/MannuMourya/Network-Security-Visualizer-Project.git
   ```

3. **Navigate to the Project Directory**:
   ```bash
   cd Network-Security-Visualizer-Project
   ```

4. **Install Required Packages**: Install the necessary Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**: Start the application by running the following command:
   ```bash
   python network_security_visualizer.py
   ```

### For Linux

1. **Install Python**: Most Linux distributions come with Python pre-installed. You can check your Python version by running:
   ```bash
   python3 --version
   ```
   If Python is not installed, you can install it using your package manager. For example, on Ubuntu:
   ```bash
   sudo apt update
   sudo apt install python3
   ```

2. **Install Git**: If you don’t have Git installed, you can install it using your package manager. For example, on Ubuntu:
   ```bash
   sudo apt install git
   ```

3. **Clone the Repository**: Open a terminal and clone the repository using Git:
   ```bash
   git clone https://github.com/MannuMourya/Network-Security-Visualizer-Project.git
   ```

4. **Navigate to the Project Directory**:
   ```bash
   cd Network-Security-Visualizer-Project
   ```

5. **Install Required Packages**: Install the necessary Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Application**: Start the application by running the following command:
   ```bash
   python3 network_security_visualizer.py
   ```

## Usage Instructions

1. **Input Number of Devices**: Enter the number of devices you want to simulate in the designated field.

2. **Input Attack Percentage**: Enter the attack percentage (0-100) to specify how much of the traffic should be considered malicious.

3. **Start Simulation**: Click the **"Start Simulation"** button to begin the network traffic simulation.

4. **Stop Simulation**: Click the **"Stop Simulation"** button to stop the traffic generation.

5. **Visualize Traffic**: Click the **"Visualize Traffic"** button to generate and display a pie chart showing the distribution of normal vs. malicious traffic.

## Conclusion
The Network Security Visualizer provides a simple interface for simulating network traffic and visualizing attack patterns, making it a useful tool for learning about network security.

## License
This project is licensed under the GNU General Public License v3.0 License. See the [LICENSE](LICENSE) file for details.
