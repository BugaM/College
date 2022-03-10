def sum_to(n):
    """Funtion that returns the sum of all integer numbers up to and including n."""
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s


if __name__ == "__main__":  # main function for testing
    print(sum_to(10))
