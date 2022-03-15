from math import sqrt

def is_prime(n):
    """Function that recognizes if the integer n is prime"""
    prime = True
    if n < 2:
        prime = False
    else:
        for i in range(2, int(sqrt(n)) +1):
            if n % i == 0:
                prime = False
    return prime


if __name__ == "__main__":  # main funtion for testing
    print(is_prime(15))
