# Zadanie 1

# Cel: Zaimplementuj dekorator conditional_decorator, który przyjmuje dwa argumenty:
# funkcję warunkową condition oraz dekorator decorator.
# Dekorator powinien stosować decorator do funkcji dekorowanej tylko wtedy,
# gdy warunek zwrócony przez condition jest prawdziwy.

def conditional_decorator(condition, decorator):
    """
    Implementacja dekoratora warunkowego.
    
    Args:
    condition (function): Funkcja zwracająca wartość boolowską.
    decorator (function): Dekorator do zastosowania, jeśli warunek jest spełniony.

    Returns:
    function: Nowy dekorator.
    """
    pass

# Przykładowe zastosowanie
def some_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2  # Przykładowa operacja
    return wrapper

@conditional_decorator(lambda x: x > 10, some_decorator)
def test_function(x):
    return x

# Testowanie
print('Zadanie 1')
print(test_function(5))  # Powinno zwrócić 5
print(test_function(15)) # Powinno zwrócić 30 (15 * 2)


# Zadanie 2

# Cel: Napisz funkcję simple_cache_system, która symuluje działanie prostego systemu cachingu.
# Powinna ona przechowywać wyniki funkcji z ograniczeniem czasowym.
# Po upływie określonego czasu, wynik powinien zostać usunięty z pamięci podręcznej.

import time

def simple_cache_system(timeout):
    """
    Implementacja prostego systemu cachingu z ograniczeniem czasowym.

    Args:
    timeout (int): Czas życia cache w sekundach.

    Returns:
    function: Dekorator do cachowania wyników funkcji.
    """
    pass


# Przykładowe zastosowanie
def nth_prime(n):
    """
    Funkcja oblicza n-tą liczbę pierwszą.
    Jest to proces czasochłonny, zwłaszcza dla większych wartości n.
    """
    def is_prime(num):
        """Pomocnicza funkcja do sprawdzania, czy liczba jest pierwsza."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = 0
    num = 1
    while prime_count < n:
        num += 1
        if is_prime(num):
            prime_count += 1
    return num

# Przykładowe zastosowanie
@simple_cache_system(4)
def cached_heavy_computation(x):
    return nth_prime(x)

# Testowanie
print('Zadanie 2')
start = time.time()
print(cached_heavy_computation(10000)) 
print("Czas obliczeń:", time.time() - start)

start = time.time()
print(cached_heavy_computation(10000)) 
print("Czas pobrania z cache:", time.time() - start)

time.sleep(5)  

start = time.time()
print(cached_heavy_computation(10000))  # Powinno ponownie obliczyć, ponieważ cache wygasł
print("Czas ponownych obliczeń:", time.time() - start)