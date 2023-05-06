import tkinter as tk
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def calculate_hash():
    text = text_entry.get()
    hash_value = hashlib.sha256(text.encode()).hexdigest()
    hash_label.config(text=f"Giá trị băm của đoạn tin là: {hash_value}")

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    private_key_entry.delete(0, tk.END)
    private_key_entry.insert(0, private_key.decode())
    public_key_entry.delete(0, tk.END)
    public_key_entry.insert(0, public_key.decode())

def encrypt():
    text = text_entry.get()
    public_key = public_key_entry.get()
    key = RSA.import_key(public_key.encode())
    cipher = PKCS1_OAEP.new(key)
    encrypted_text = cipher.encrypt(text.encode())
    encrypted_label.config(text=f"Đoạn tin đã được mã hóa: {encrypted_text.hex()}")

def decrypt():
    encrypted_text = encrypted_entry.get()
    private_key = private_key_entry.get()
    key = RSA.import_key(private_key.encode())
    cipher = PKCS1_OAEP.new(key)
    decrypted_text = cipher.decrypt(bytes.fromhex(encrypted_text))
    decrypted_label.config(text=f"Đoạn tin đã được giải mã: {decrypted_text.decode()}")

root = tk.Tk()
root.title("Tính toán giá trị băm và mã hóa RSA")

text_label = tk.Label(root, text="Nhập đoạn tin:")
text_label.pack()

text_entry = tk.Entry(root)
text_entry.pack()

calculate_button = tk.Button(root, text="Tính toán", command=calculate_hash)
calculate_button.pack()

hash_label = tk.Label(root, text="")
hash_label.pack()

keygen_button = tk.Button(root, text="Tạo khoá", command=generate_keys)
keygen_button.pack()

private_key_label = tk.Label(root, text="Khoá riêng:")
private_key_label.pack()

private_key_entry = tk.Entry(root)
private_key_entry.pack()

public_key_label = tk.Label(root, text="Khoá chung:")
public_key_label.pack()

public_key_entry = tk.Entry(root)
public_key_entry.pack()

encrypt_button = tk.Button(root, text="Mã hóa", command=encrypt)
encrypt_button.pack()

encrypted_label = tk.Label(root, text="")
encrypted_label.pack()

encrypted_text_label = tk.Label(root, text="Đoạn tin đã được mã hóa:")
encrypted_text_label.pack()

encrypted_entry = tk.Entry(root)
encrypted_entry.pack()

decrypt_button = tk.Button(root, text="Giải mã", command=decrypt)
decrypt_button.pack()

decrypted_label = tk.Label(root, text="")
decrypted_label.pack()

root.mainloop()
