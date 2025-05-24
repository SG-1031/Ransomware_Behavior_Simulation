# Ransomware Behavior Simulation

## Overview

This project simulates ransomware behavior in a safe and controlled environment. It mimics the encryption process by appending a ransom note to files and renaming them with a `.locked` extension. The purpose is to help cybersecurity professionals understand ransomware attack patterns and practice incident response without causing real damage.

## Features

- Simulates file encryption by appending a ransom note  
- Renames files to indicate encryption (`.locked` extension)  
- Logs all simulated activity with timestamps  
- Runs continuous simulation cycles with adjustable delay  
- Safe to use on dummy files in a controlled folder  
- Easy to start and stop with keyboard interrupt  

## Setup Instructions

1. **Install Python 3**  
   Make sure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Download the Project Files**  
   Clone this repository or download the project ZIP and extract it.

3. **Create the Target Folder**  
   Inside the project directory, create a folder named `sample_files` where the simulation will operate.

4. **Add Sample Files**  
   Place some dummy text files (e.g., `test1.txt`, `document.txt`) inside the `sample_files` folder. These files will be “encrypted” during the simulation.

5. **Run the Simulator**  
   Open a terminal or command prompt, navigate to the project directory, and run:

   ```bash
   python3 ransomware_simulator.py
