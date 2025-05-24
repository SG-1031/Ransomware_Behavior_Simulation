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

## Setup

1. Make sure you have Python 3 installed.  
2. Clone or download this repository.  
3. Create a folder named `sample_files` in the project directory.  
4. Add some dummy text files (e.g., `test1.txt`, `document2.txt`) to the `sample_files` folder.  

## Usage

Run the simulation with:

python3 ransomware_simulator.py
