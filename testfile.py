import numpy as np

file_path = r"C:\Users\marco\PycharmProjects\InDuDoNet\deeplesion\train\trainmask.npy"
try:
    train_mask = np.load(file_path)  # Attempt to load the file
    print("File loaded successfully! Shape:", train_mask.shape)  # Print the shape of the data
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"Error loading file: {e}")
