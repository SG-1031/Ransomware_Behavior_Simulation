import os
import time
import logging

# Configure logging
logging.basicConfig(filename='ransomware_simulation.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Folder to simulate encryption on
TARGET_FOLDER = 'sample_files'

# Simulated ransom note text
RANSOM_NOTE = "\n---\nThis file is locked by Ransomware Simulator. Do not worry, this is a test."

def simulate_encryption(file_path):
    try:
        with open(file_path, 'a') as f:
            f.write(RANSOM_NOTE)
        new_name = file_path + '.locked'
        os.rename(file_path, new_name)
        logging.info(f"Encrypted: {file_path} -> {new_name}")
        print(f"Encrypted: {file_path}")
    except Exception as e:
        logging.error(f"Error encrypting {file_path}: {e}")

def run_simulation():
    print("Starting ransomware simulation...")
    logging.info("Ransomware simulation started.")
    while True:
        for filename in os.listdir(TARGET_FOLDER):
            file_path = os.path.join(TARGET_FOLDER, filename)
            if os.path.isfile(file_path) and not filename.endswith('.locked'):
                simulate_encryption(file_path)
        print("Simulation cycle complete. Waiting 10 seconds before next cycle...")
        time.sleep(10)  # Wait 10 seconds before next simulation cycle

if __name__ == "__main__":
    # Ensure target folder exists
    if not os.path.exists(TARGET_FOLDER):
        os.makedirs(TARGET_FOLDER)
        print(f"Created folder '{TARGET_FOLDER}'. Please add sample files to simulate.")
    else:
        try:
            run_simulation()
        except KeyboardInterrupt:
            print("\nSimulation stopped by user.")
            logging.info("Ransomware simulation stopped by user.")
