S_BOX = [
    0x63,
    0x7C,
    0x77,
    0x7B,
    0xF2,
    0x6B,
    0x6F,
    0xC5,
    0x30,
    0x01,
    0x67,
    0x2B,
    0xFE,
    0xD7,
    0xAB,
    0x76,
    0xCA,
    0x82,
    0xC9,
    0x7D,
    0xFA,
    0x59,
    0x47,
    0xF0,
    0xAD,
    0xD4,
    0xA2,
    0xAF,
    0x9C,
    0xA4,
    0x72,
    0xC0,
    0xB7,
    0xFD,
    0x93,
    0x26,
    0x36,
    0x3F,
    0xF7,
    0xCC,
    0x34,
    0xA5,
    0xE5,
    0xF1,
    0x71,
    0xD8,
    0x31,
    0x15,
    0x04,
    0xC7,
    0x23,
    0xC3,
    0x18,
    0x96,
    0x05,
    0x9A,
    0x07,
    0x12,
    0x80,
    0xE2,
    0xEB,
    0x27,
    0xB2,
    0x75,
    0x09,
    0x83,
    0x2C,
    0x1A,
    0x1B,
    0x6E,
    0x5A,
    0xA0,
    0x52,
    0x3B,
    0xD6,
    0xB3,
    0x29,
    0xE3,
    0x2F,
    0x84,
    0x53,
    0xD1,
    0x00,
    0xED,
    0x20,
    0xFC,
    0xB1,
    0x5B,
    0x6A,
    0xCB,
    0xBE,
    0x39,
    0x4A,
    0x4C,
    0x58,
    0xCF,
    0xD0,
    0xEF,
    0xAA,
    0xFB,
    0x43,
    0x4D,
    0x33,
    0x85,
    0x45,
    0xF9,
    0x02,
    0x7F,
    0x50,
    0x3C,
    0x9F,
    0xA8,
    0x51,
    0xA3,
    0x40,
    0x8F,
    0x92,
    0x9D,
    0x38,
    0xF5,
    0xBC,
    0xB6,
    0xDA,
    0x21,
    0x10,
    0xFF,
    0xF3,
    0xD2,
    0xCD,
    0x0C,
    0x13,
    0xEC,
    0x5F,
    0x97,
    0x44,
    0x17,
    0xC4,
    0xA7,
    0x7E,
    0x3D,
    0x64,
    0x5D,
    0x19,
    0x73,
    0x60,
    0x81,
    0x4F,
    0xDC,
    0x22,
    0x2A,
    0x90,
    0x88,
    0x46,
    0xEE,
    0xB8,
    0x14,
    0xDE,
    0x5E,
    0x0B,
    0xDB,
    0xE0,
    0x32,
    0x3A,
    0x0A,
    0x49,
    0x06,
    0x24,
    0x5C,
    0xC2,
    0xD3,
    0xAC,
    0x62,
    0x91,
    0x95,
    0xE4,
    0x79,
    0xE7,
    0xC8,
    0x37,
    0x6D,
    0x8D,
    0xD5,
    0x4E,
    0xA9,
    0x6C,
    0x56,
    0xF4,
    0xEA,
    0x65,
    0x7A,
    0xAE,
    0x08,
    0xBA,
    0x78,
    0x25,
    0x2E,
    0x1C,
    0xA6,
    0xB4,
    0xC6,
    0xE8,
    0xDD,
    0x74,
    0x1F,
    0x4B,
    0xBD,
    0x8B,
    0x8A,
    0x70,
    0x3E,
    0xB5,
    0x66,
    0x48,
    0x03,
    0xF6,
    0x0E,
    0x61,
    0x35,
    0x57,
    0xB9,
    0x86,
    0xC1,
    0x1D,
    0x9E,
    0xE1,
    0xF8,
    0x98,
    0x11,
    0x69,
    0xD9,
    0x8E,
    0x94,
    0x9B,
    0x1E,
    0x87,
    0xE9,
    0xCE,
    0x55,
    0x28,
    0xDF,
    0x8C,
    0xA1,
    0x89,
    0x0D,
    0xBF,
    0xE6,
    0x42,
    0x68,
    0x41,
    0x99,
    0x2D,
    0x0F,
    0xB0,
    0x54,
    0xBB,
    0x16,
]

RCON_WORDS = [
    0x8D000000,
    0x01000000,
    0x02000000,
    0x04000000,
    0x08000000,
    0x10000000,
    0x20000000,
    0x40000000,
    0x80000000,
    0x1B000000,
    0x36000000,
]

INV_SBOX = [
    0x52,
    0x09,
    0x6A,
    0xD5,
    0x30,
    0x36,
    0xA5,
    0x38,
    0xBF,
    0x40,
    0xA3,
    0x9E,
    0x81,
    0xF3,
    0xD7,
    0xFB,
    0x7C,
    0xE3,
    0x39,
    0x82,
    0x9B,
    0x2F,
    0xFF,
    0x87,
    0x34,
    0x8E,
    0x43,
    0x44,
    0xC4,
    0xDE,
    0xE9,
    0xCB,
    0x54,
    0x7B,
    0x94,
    0x32,
    0xA6,
    0xC2,
    0x23,
    0x3D,
    0xEE,
    0x4C,
    0x95,
    0x0B,
    0x42,
    0xFA,
    0xC3,
    0x4E,
    0x08,
    0x2E,
    0xA1,
    0x66,
    0x28,
    0xD9,
    0x24,
    0xB2,
    0x76,
    0x5B,
    0xA2,
    0x49,
    0x6D,
    0x8B,
    0xD1,
    0x25,
    0x72,
    0xF8,
    0xF6,
    0x64,
    0x86,
    0x68,
    0x98,
    0x16,
    0xD4,
    0xA4,
    0x5C,
    0xCC,
    0x5D,
    0x65,
    0xB6,
    0x92,
    0x6C,
    0x70,
    0x48,
    0x50,
    0xFD,
    0xED,
    0xB9,
    0xDA,
    0x5E,
    0x15,
    0x46,
    0x57,
    0xA7,
    0x8D,
    0x9D,
    0x84,
    0x90,
    0xD8,
    0xAB,
    0x00,
    0x8C,
    0xBC,
    0xD3,
    0x0A,
    0xF7,
    0xE4,
    0x58,
    0x05,
    0xB8,
    0xB3,
    0x45,
    0x06,
    0xD0,
    0x2C,
    0x1E,
    0x8F,
    0xCA,
    0x3F,
    0x0F,
    0x02,
    0xC1,
    0xAF,
    0xBD,
    0x03,
    0x01,
    0x13,
    0x8A,
    0x6B,
    0x3A,
    0x91,
    0x11,
    0x41,
    0x4F,
    0x67,
    0xDC,
    0xEA,
    0x97,
    0xF2,
    0xCF,
    0xCE,
    0xF0,
    0xB4,
    0xE6,
    0x73,
    0x96,
    0xAC,
    0x74,
    0x22,
    0xE7,
    0xAD,
    0x35,
    0x85,
    0xE2,
    0xF9,
    0x37,
    0xE8,
    0x1C,
    0x75,
    0xDF,
    0x6E,
    0x47,
    0xF1,
    0x1A,
    0x71,
    0x1D,
    0x29,
    0xC5,
    0x89,
    0x6F,
    0xB7,
    0x62,
    0x0E,
    0xAA,
    0x18,
    0xBE,
    0x1B,
    0xFC,
    0x56,
    0x3E,
    0x4B,
    0xC6,
    0xD2,
    0x79,
    0x20,
    0x9A,
    0xDB,
    0xC0,
    0xFE,
    0x78,
    0xCD,
    0x5A,
    0xF4,
    0x1F,
    0xDD,
    0xA8,
    0x33,
    0x88,
    0x07,
    0xC7,
    0x31,
    0xB1,
    0x12,
    0x10,
    0x59,
    0x27,
    0x80,
    0xEC,
    0x5F,
    0x60,
    0x51,
    0x7F,
    0xA9,
    0x19,
    0xB5,
    0x4A,
    0x0D,
    0x2D,
    0xE5,
    0x7A,
    0x9F,
    0x93,
    0xC9,
    0x9C,
    0xEF,
    0xA0,
    0xE0,
    0x3B,
    0x4D,
    0xAE,
    0x2A,
    0xF5,
    0xB0,
    0xC8,
    0xEB,
    0xBB,
    0x3C,
    0x83,
    0x53,
    0x99,
    0x61,
    0x17,
    0x2B,
    0x04,
    0x7E,
    0xBA,
    0x77,
    0xD6,
    0x26,
    0xE1,
    0x69,
    0x14,
    0x63,
    0x55,
    0x21,
    0x0C,
    0x7D,
]

AES_MIX = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02],
]

AES_INV_MIX = [
    [0x0E, 0x0B, 0x0D, 0x09],
    [0x09, 0x0E, 0x0B, 0x0D],
    [0x0D, 0x09, 0x0E, 0x0B],
    [0x0B, 0x0D, 0x09, 0x0E],
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
            raise ValueError(
                "Erro: a chave possui 32 caracteres, mas contem digitos hexadecimais invalidos!"
            )

    # String
    key_bytes = key_input.encode("utf-8")

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
    if len(key) != 16:
        raise ValueError("AES-128 exige chave de 16 bytes")

    w = []

    # 16B da chave recebida, ela e usada no primeiro round
    for i in range(4):
        w.append([key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]])

    # Construcao das demais round keys
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


def encrypt_block(block: bytes, round_keys: list[list[list[int]]]) -> bytes:
    if len(block) != 16:
        raise ValueError("O bloco deve ter exatamente 16 bytes.")
    # Conversão dos bytes de entrada
    state = bytes2state(block)

    # Round 0
    add_round_key(state, round_keys[0])

    # Rounds 1 a 9
    for r in range(1, 10):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state, AES_MIX)
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

    message_bytes = message_str.encode("utf-8")
    padded_bytes = pad_pkcs7(message_bytes, 16)

    ciphertext = bytearray()

    for i in range(0, len(padded_bytes), 16):
        block = padded_bytes[i : i + 16]
        encrypted_block = encrypt_block(block, round_keys)
        ciphertext.extend(encrypted_block)

    return ciphertext.hex()


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
                multiplicacao_gf(matrix[r][0], col[0])
                ^ multiplicacao_gf(matrix[r][1], col[1])
                ^ multiplicacao_gf(matrix[r][2], col[2])
                ^ multiplicacao_gf(matrix[r][3], col[3])
            )


def inv_mix_columns(state):
    mix_columns(state, AES_INV_MIX)


def inv_sub_bytes(estado):
    """
    substitui cada byte do estado pelo valor correspondente na InvSBox"""
    for r in range(4):
        for c in range(4):
            estado[r][c] = INV_SBOX[estado[r][c]]


def inv_shift_rows(estado: list[list[int]]):
    """
    deslocamentos p/ direita
    s0 -> 0 deslocamentos
    s1 -> 1 deslocamento
    s2 -> 2 deslocamentos
    s3 -> 3 deslocamentos
    """

    estado[1] = estado[1][-1:] + estado[1][:-1]
    estado[2] = estado[2][-2:] + estado[2][:-2]
    estado[3] = estado[3][-3:] + estado[3][:-3]


AES_POLY = 0x11B


def xtime(a: int) -> int:
    """
    multiplicacao por 0x02 em GF(2⁸) com polinomio 0x11B
    """
    a <<= 1
    if a & 0x100:
        a ^= AES_POLY
    return a


def multiplicacao_gf(a: int, b: int) -> int:
    """versao da multiplicacao em gf que implementa o que foi explicado na video aula"""
    r = 0

    for _ in range(8):
        if b & 1:
            r ^= a
        a = xtime(a)
        b >>= 1
    return r


def unpad_pkcs7(data: bytes, block_size: int = 16) -> bytes:
    """
    Remove o padding PKCS#7 adicionado em pad_pkcs7.
    O último byte indica quantos bytes de padding foram adicionados.
    """
    if not data:
        raise ValueError("Erro: dados vazios, não há padding para remover.")

    pad = data[-1]

    if pad < 1 or pad > block_size or pad > len(data):
        raise ValueError("Erro: padding PKCS#7 inválido.")

    if data[-pad:] != bytes([pad]) * pad:
        raise ValueError("Erro: padding PKCS#7 inconsistente.")

    return data[:-pad]


def parse_ciphertext(cifrado: str) -> bytes:
    """
    Aceita a mensagem cifrada em hexadecimal ou em decimal.
    Decimal pode vir separado por vírgula, espaço ou quebra de linha.
    """
    cifrado = cifrado.strip()

    # Tenta hexadecimal primeiro (ex.: "8f3a...")
    if not any(sep in cifrado for sep in " ,\n\t\r"):
        try:
            return bytes.fromhex(cifrado)
        except ValueError:
            pass

    # Tenta decimal (ex.: "143 58 ..." ou "143,58,...")
    partes = cifrado.replace(",", " ").split()

    try:
        valores = [int(x) for x in partes]
    except ValueError:
        raise ValueError("Erro: entrada cifrada inválida (não é hex nem decimal).")

    if any(v < 0 or v > 255 for v in valores):
        raise ValueError("Erro: valores decimais devem estar entre 0 e 255.")

    return bytes(valores)


def decrypt_block(bloco, round_keys):
    estado = bytes2state(bloco)

    add_round_key(estado, round_keys[10])

    for rodada in range(9, 0, -1):
        inv_shift_rows(estado)

        inv_sub_bytes(estado)

        add_round_key(estado, round_keys[rodada])

        inv_mix_columns(estado)

    inv_shift_rows(estado)

    inv_sub_bytes(estado)

    add_round_key(estado, round_keys[0])

    return state2bytes(estado)


def decrypt_message(cifrado_str: str, key_input: str) -> str:
    """
    Decifra a mensagem recebida (hexadecimal ou decimal) usando a chave fornecida.
    Retorna a string original (após remover o padding PKCS#7).
    """
    key_bytes = parse_key(key_input)
    round_keys = key_expansion(key_bytes)

    cipher_bytes = parse_ciphertext(cifrado_str)

    if len(cipher_bytes) == 0:
        raise ValueError("Erro: mensagem cifrada vazia.")

    if len(cipher_bytes) % 16 != 0:
        raise ValueError(
            f"Erro: o tamanho do cifrado ({len(cipher_bytes)}B) "
            f"não é múltiplo de 16 bytes."
        )

    plaintext = bytearray()

    for i in range(0, len(cipher_bytes), 16):
        block = cipher_bytes[i : i + 16]
        decrypted_block = decrypt_block(block, round_keys)
        plaintext.extend(decrypted_block)

    try:
        return unpad_pkcs7(bytes(plaintext), 16).decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError("erro: chave incorreta ou dados corrompidos")


if __name__ == "__main__":
    modo = input("cifrar (c) ou decifrar (d)? ").strip().lower()
    msg = input("insira a mensagem: ")
    key = input("insira a chave: ")
    
    if modo == "d":
        print("\nTexto claro:", decrypt_message(msg, key))
    else:
        print("\nResultado cifrado (Hex):", encrypt_message(msg, key))