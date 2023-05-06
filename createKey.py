from Crypto.PublicKey import RSA

# Tạo khóa RSA với độ dài khóa là 2048 bits
key = RSA.generate(2048)

# Tạo khóa riêng
private_key = key.export_key()

# Tạo khóa công khai
public_key = key.publickey().export_key()

# Lưu khóa riêng vào một file vào cùng folder với file đang thực thi
with open('private.pem', 'wb') as f:
    f.write(private_key)

# Lưu khóa công khai vào một file vào cùng folder với file đang thực thi
with open('public.pem', 'wb') as f:
    f.write(public_key)
