
def to_8bit_binary(n):
    """Convert a signed integer to 8-bit 2's complement."""
    if n < -128 or n > 127:
        raise ValueError("Number is outside the 8-bit range.")
    return format(n & 0xFF, "08b")


def signed_value(binary):
    """Convert an 8-bit 2's complement bit pattern to decimal."""
    value = int(binary, 2)
    if value & 0x80:  # Most significant bit is 1
        value -= 256
    return value


def binary_addition(a, b):
    """Add two signed 8-bit numbers and detect overflow."""
    bin_a = to_8bit_binary(a)
    bin_b = to_8bit_binary(b)

    # Perform 8-bit addition; carry beyond bit 7 is discarded.
    result_unsigned = (int(bin_a, 2) + int(bin_b, 2)) & 0xFF
    result_bin = format(result_unsigned, "08b")
    result_dec = signed_value(result_bin)

    # Overflow occurs when operands have the same sign
    # but the result has the opposite sign.
    sign_a = bin_a[0]
    sign_b = bin_b[0]
    sign_result = result_bin[0]
    overflow = (sign_a == sign_b and sign_result != sign_a)

    print(f"Operand A: {a:+d} = {bin_a}")
    print(f"Operand B: {b:+d} = {bin_b}")
    print(f"Binary addition: {bin_a} + {bin_b}")
    print(f"Result (8-bit): {result_bin}")
    print(f"Result (decimal): {result_dec}")
    print(f"Overflow: {'Yes' if overflow else 'No'}")
    print("-" * 45)


print("Expression (a): 25 + (+18)")
binary_addition(25, 18)

print("Expression (b): (-25) + (-18)")
binary_addition(-25, -18)
