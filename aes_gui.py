import os
import hashlib
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# ----------------------------
# ENCRYPT FUNCTION
# ----------------------------

def encrypt_file():

    # Select file
    filepath = filedialog.askopenfilename()

    if not filepath:
        return

    # Get password
    password = password_entry.get()

    if not password:
        messagebox.showerror("Error", "Please enter password")
        return

    # Generate AES-256 key
    key = hashlib.sha256(password.encode()).digest()

    # Read file
    with open(filepath, "rb") as f:
        data = f.read()

    # Generate IV
    iv = os.urandom(16)

    # Add padding
    padding = 16 - len(data) % 16
    data += bytes([padding]) * padding

    # Create AES Cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    # Encrypt data
    encrypted = encryptor.update(data) + encryptor.finalize()

    # Generate SHA-256 hash of original data
    file_hash = hashlib.sha256(data).digest()

    # Save encrypted file
    encrypted_file = filepath + ".encrypted"

    with open(encrypted_file, "wb") as f:

        # Save IV
        f.write(iv)

        # Save file hash
        f.write(file_hash)

        # Save encrypted data
        f.write(encrypted)

    messagebox.showinfo(
        "Success",
        "File Encrypted Successfully!\n\n"
        "AES-256 Encryption Applied\n"
        "SHA-256 Integrity Hash Generated"
    )

# ----------------------------
# DECRYPT FUNCTION
# ----------------------------

def decrypt_file():

    # Select encrypted file
    filepath = filedialog.askopenfilename()

    if not filepath:
        return

    # Get password
    password = password_entry.get()

    if not password:
        messagebox.showerror("Error", "Please enter password")
        return

    # Generate AES-256 key
    key = hashlib.sha256(password.encode()).digest()

    # Read encrypted file
    with open(filepath, "rb") as f:

        # Read IV
        iv = f.read(16)

        # Read stored hash
        stored_hash = f.read(32)

        # Read encrypted data
        encrypted_data = f.read()

    # Create AES Cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    try:

        # Decrypt data
        decrypted = decryptor.update(encrypted_data) + decryptor.finalize()

        # Remove padding
        padding = decrypted[-1]
        decrypted = decrypted[:-padding]

        # Generate new hash
        new_hash = hashlib.sha256(decrypted).digest()

        # Verify integrity
        if new_hash == stored_hash:

            integrity_message = "✅ File Integrity Verified"

        else:

            integrity_message = "❌ File Tampering Detected"

        # Save decrypted file
        output_file = "decrypted_" + os.path.basename(filepath).replace(".encrypted", "")

        with open(output_file, "wb") as f:
            f.write(decrypted)

        messagebox.showinfo(
            "Success",
            "File Decrypted Successfully!\n\n" + integrity_message
        )

    except:

        messagebox.showerror(
            "Error",
            "❌ Wrong Password or Corrupted File"
        )

# ----------------------------
# GUI WINDOW
# ----------------------------

root = tk.Tk()

root.title("AES-256 File Encryption System")

root.geometry("550x350")

root.configure(bg="#f0f0f0")

# ----------------------------
# HEADING
# ----------------------------

title = tk.Label(
    root,
    text="AES-256 Secure File Encryption System",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#222222"
)

title.pack(pady=20)

# ----------------------------
# PASSWORD LABEL
# ----------------------------

password_label = tk.Label(
    root,
    text="Enter Password:",
    font=("Arial", 12),
    bg="#f0f0f0"
)

password_label.pack()

# ----------------------------
# PASSWORD ENTRY
# ----------------------------

password_entry = tk.Entry(
    root,
    show="*",
    width=35,
    font=("Arial", 12)
)

password_entry.pack(pady=10)

# ----------------------------
# ENCRYPT BUTTON
# ----------------------------

encrypt_button = tk.Button(
    root,
    text="Encrypt File",
    command=encrypt_file,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20,
    height=2
)

encrypt_button.pack(pady=15)

# ----------------------------
# DECRYPT BUTTON
# ----------------------------

decrypt_button = tk.Button(
    root,
    text="Decrypt File",
    command=decrypt_file,
    bg="blue",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20,
    height=2
)

decrypt_button.pack(pady=10)

# ----------------------------
# FOOTER
# ----------------------------

footer = tk.Label(
    root,
    text="Cyber Security Final Year Project",
    font=("Arial", 10),
    bg="#f0f0f0",
    fg="gray"
)

footer.pack(side="bottom", pady=15)

# ----------------------------
# RUN GUI
# ----------------------------

root.mainloop()
