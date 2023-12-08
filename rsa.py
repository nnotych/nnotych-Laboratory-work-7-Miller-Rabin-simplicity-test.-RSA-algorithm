import random
import math

def is_prime(n, k=5):
    """
    Перевірка, чи є число простим за допомогою тесту Міллера-Рабіна.
    """
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Знаходження s та d для подання n-1 у вигляді 2^s * d
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Проведення k ітерацій тесту Міллера-Рабіна
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    """
    Генерація випадкового простого числа з бажаною кількістю біт.
    """
    while True:
        number = random.getrandbits(bits)
        if is_prime(number):
            return number

def extended_gcd(a, b):
    """
    Розширений алгоритм Евкліда для знаходження оберненого за модулем.
    Повертає (gcd, x, y), таке що ax + by = gcd.
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def generate_keypair(bits):
    """
    Генерація відкритого та закритого ключів для RSA.
    """
    p = generate_prime(bits)
    q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Вибір експоненти для відкритого ключа
    e = random.randrange(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Знаходження оберненої експоненти за допомогою розширеного алгоритму Евкліда
    _, d, _ = extended_gcd(e, phi)
    d %= phi

    return (e, n), (d, n)

def encrypt(message, public_key):
    """
    Шифрування повідомлення за відкритим ключем.
    """
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text

def decrypt(cipher_text, private_key):
    """
    Розшифрування за допомогою закритого ключа.
    """
    d, n = private_key
    plain_text = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(plain_text)

# Генерація ключів
bits = 512
public_key, private_key = generate_keypair(bits)

# Tecт
message = "Hello, Nikita!"
print("Початкове повідомлення:", message)

# Шифрування
cipher_text = encrypt(message, public_key)
print("Зашифроване повідомлення:", cipher_text)

# Розшифрування
decrypted_text = decrypt(cipher_text, private_key)
print("Розшифроване повідомлення:", decrypted_text)
