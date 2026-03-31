def greatestCommonDivisor(a: int, b: int) -> int:
    """greatestCommonDivisor(a: int, b: int) -> int

    Calculates the greatest common divisor of two non-negative integers
    using the Euclidean algorithm: repeatedly replaces the larger value
    with the remainder of dividing the two, until the remainder is zero.

    Usage example:
        >>> greatestCommonDivisor(12, 8)
        4
        >>> greatestCommonDivisor(100, 75)
        25
    """
    while b:
        a, b = b, a % b
    return a
