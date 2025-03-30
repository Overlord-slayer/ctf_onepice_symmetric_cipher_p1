def xor_decrypt(hex_data, key):
    data = bytes.fromhex(hex_data)  # Convertir hex a bytes
    key = key.encode()  # Convertir clave a bytes
    decrypted = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
    return decrypted.decode(errors="ignore")  # Intentar decodificar a texto

# Texto en hexadecimal
hex_string = "747d70776d045300075503510a04555100505105000450000605065356010a015506015201"

# Tu carné (reemplázalo por el tuyo)
carnet = "211024"

# Intentar descifrar
flag = xor_decrypt(hex_string, carnet)
print("Flag:", flag)
