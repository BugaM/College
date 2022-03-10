def is_prime(n):
    """Function that recognizes if the integer n is prime"""
    prime = True
    if n < 2:
        prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                prime = False
    return prime


if __name__ == "__main__":  # main funtion for testing
    print(is_prime(107))
