S_BOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

RCON_WORDS = [
    0x8d000000, 0x01000000, 0x02000000, 0x04000000, 0x08000000, 
    0x10000000, 0x20000000, 0x40000000, 0x80000000, 0x1b000000, 0x36000000
]

MIX_MATRIX = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

# Converte 16B em uma matriz de estado 4x4
def bytes2state(data: bytes) -> list[list[int]]:
    state = [[0] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            state[r][c] = data[r + 4 * c]
    return state

# Converte uma matriz de estado 4x4 em 16B 
def state2bytes(state: list[list[int]]) -> bytes:
    out = bytearray(16)
    for r in range(4):
        for c in range(4):
            out[r + 4 * c] = state[r][c]
    return bytes(out)

# Preenchimento padrão (PKCS#7) para atingir um múltiplo de block_size
def pad_pkcs7(data: bytes, block_size: int = 16) -> bytes:
    padding_len = block_size - (len(data) % block_size)
    return data + bytes([padding_len] * padding_len)

# Tratamento de chave recebida
def parse_key(key_input: str) -> bytes:
    # Hexa
    if len(key_input) == 32:
        try:
            return bytes.fromhex(key_input)
        except ValueError:
            raise ValueError("Erro: a chave possui 32 caracteres, mas contém digitos hexadecimais invalidos!")

    # String
    key_bytes = key_input.encode('utf-8')
    
    if len(key_bytes) == 16:
        return key_bytes

    raise ValueError(
        f"Erro: chave invalida. Tamanho recebido: {len(key_bytes)}B.\n"
        f"A chave do AES-128 deve conter:\n"
        f" - 16 caracteres para Texto Simples (ASCII/UTF-8) ou\n"
        f" - 32 caracteres para Hexadecimal"
    )
    
def rot_word(word: list[int]) -> list[int]:
    return word[1:] + word[:1]

def sub_bytes(state: list[list[int]]):
    for r in range(4):
        for c in range(4):
            state[r][c] = S_BOX[state[r][c]]

def sub_word(word: list[int]) -> list[int]:
    return [S_BOX[b] for b in word]

def key_expansion(key: bytes) -> list[list[list[int]]]:
    w = []

    for i in range(4):
        w.append([key[4*i], key[4*i + 1], key[4*i + 2], key[4*i + 3]])

    for i in range(4, 44):
        temp = w[i - 1][:]

        if i % 4 == 0:
            temp = sub_word(rot_word(temp))
            rcon_byte = (RCON_WORDS[i // 4] >> 24) & 0xFF
            temp[0] ^= rcon_byte

        word_i = [w[i - 4][b] ^ temp[b] for b in range(4)]
        w.append(word_i)

    k = []
    for r in range(11):
        round_words = w[4 * r : 4 * r + 4]

        key_matrix = [[0] * 4 for _ in range(4)]
        for col in range(4):
            for row in range(4):
                key_matrix[row][col] = round_words[col][row]

        k.append(key_matrix)

    return k

def shift_rows(state: list[list[int]]):
    state[1] = state[1][1:] + state[1][:1]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][3:] + state[3][:3]

def add_round_key(state: list[list[int]], round_key: list[list[int]]):
    for r in range(4):
        for c in range(4):
            state[r][c] ^= round_key[r][c]
            
# TAREFA B, SUBSTITUIR:
# Matriz multiplicativa constante para Cifragem (FIPS 197)
MIX_MATRIX_ENCRYPT = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

def gmul(a: int, b: int) -> int:
    """
    Multiplicação no Corpo de Galois GF(2^8) com o polinômio irredutível 0x11B.
    """
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a = (a << 1) & 0xFF
        if hi_bit_set:
            a ^= 0x1B
        b >>= 1
    return p

def mix_columns(state: list[list[int]], matrix: list[list[int]]):
    """
    Aplica a multiplicação matricial sobre cada COLUNA da matriz de estado.
    Aceita qualquer matriz multiplicativa constante 4x4.
    """
    for c in range(4):
        # Pega os 4 bytes da coluna 'c'
        col = [state[r][c] for r in range(4)]
        
        # Multiplica a matriz constante pela coluna
        for r in range(4):
            state[r][c] = (
                gmul(matrix[r][0], col[0]) ^
                gmul(matrix[r][1], col[1]) ^
                gmul(matrix[r][2], col[2]) ^
                gmul(matrix[r][3], col[3])
            )
            
# FIM TAREFA B

def encrypt_block(block: bytes, round_keys: list[list[list[int]]]) -> bytes:
    # Conversão dos bytes de entrada
    state = bytes2state(block)

    # Round 0
    add_round_key(state, round_keys[0])

    # Rounds 1 a 9
    for r in range(1, 10):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state, MIX_MATRIX_ENCRYPT)
        add_round_key(state, round_keys[r])

    # Round 10
    sub_bytes(state)
    shift_rows(state)
    add_round_key(state, round_keys[10])

    # Conversão da matriz
    return state2bytes(state)

def encrypt_message(message_str: str, key_input: str) -> str:
    key_bytes = parse_key(key_input)
    round_keys = key_expansion(key_bytes)
    
    message_bytes = message_str.encode('utf-8')
    padded_bytes = pad_pkcs7(message_bytes, 16)
    
    ciphertext = bytearray()
    
    for i in range(0, len(padded_bytes), 16):
        block = padded_bytes[i : i + 16]
        encrypted_block = encrypt_block(block, round_keys)
        ciphertext.extend(encrypted_block)
        
    return ciphertext.hex()

if __name__ == "__main__":
    # plaintext = "..."
    # key = "minhachavesecre1"

    plaintext = input("insira a mensagem: ")
    key = input("insira a chave: ")

    resultado_hex = encrypt_message(plaintext, key)

    print("\nResultado Cifrado (Hex):", resultado_hex)