# AES
implementing the Advanced Encryption Standard (AES)

## Orientação de Compilação e Execução

### 1. Requisitos e Bibliotecas
* **Linguagem:** Python 3.10 ou superior.
* **Bibliotecas Externas:** Nenhuma. A implementação utiliza exclusivamente recursos nativos da linguagem.

---

### 2. Instruções de Execução

A interação com o programa ocorre de forma direta via terminal interativo:

1. Abra o terminal na pasta onde está o arquivo do projeto (`aes.py`);

2. Execute o comando:
   ```bash
   python aes.py

3. O programa solicitará as entradas em sequência:

    Modo: Digite **c** para cifrar ou **d** para decifrar.

    Mensagem:
        Na cifragem: digite o texto plano desejado.
        Na decifragem: digite a string cifrada em formato hexadecimal.

    Chave: Digite a chave de 128 bits (16 caracteres de texto ASCII ou 32 caracteres Hexadecimais).