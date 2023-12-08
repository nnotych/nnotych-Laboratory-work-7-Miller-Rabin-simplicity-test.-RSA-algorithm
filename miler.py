import random

def miller_rabin(n, k):
  """
  Тест простоти Міллера — Рабіна.

  Вхідні дані:
    n>3, непарне натуральне число, яке потрібно перевірити на простоту;
    k - кількість раундів.

  Вихідні дані:
    Чи є n складеним або простим числом. Якщо просте, то з якою ймовірністю воно просте.
  """

  if n <= 3:
    return n <= 2
  s = 0
  d = n - 1
  while d % 2 == 0:
    s += 1
    d //= 2

  for _ in range(k):
    a = random.randint(2, n - 1)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
      continue
    for r in range(1, s):
      x = pow(x, 2, n)
      if x == n - 1:
        break
    else:
      return False
  return True


def main():
  n = int(input("Введіть число: "))
  k = int(input("Введіть кількість раундів: "))
  is_prime = miller_rabin(n, k)
  if is_prime:
    print(f"Число {n} є простим з ймовірністю 1 - 1/4^k = {1 - 1 / 4**k}")
  else:
    print(f"Число {n} є складеним")


if __name__ == "__main__":
  main()
