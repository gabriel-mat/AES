# teste_fips.py
from aes import encrypt_block, decrypt_block, key_expansion

pt_hex = "00112233445566778899aabbccddeeff"
key_hex = "000102030405060708090a0b0c0d0e0f"
esperado = "69c4e0d86a7b0430d8cdb78070b4c55a"

round_keys = key_expansion(bytes.fromhex(key_hex))
ct = encrypt_block(bytes.fromhex(pt_hex), round_keys)

print("Cifrado  :", ct.hex())
print("Esperado :", esperado)
assert ct.hex() == esperado, "Cifragem falhou!"

pt = decrypt_block(ct, round_keys)
print("Decifrado:", pt.hex())
assert pt.hex() == pt_hex, "Decifragem falhou!"
