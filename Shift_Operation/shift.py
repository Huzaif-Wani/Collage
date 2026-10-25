
def logical_left_shift(binary, positions):
    print("Original number:", binary)

    result = binary
    for i in range(positions):
        result = result[1:] + "0"
        print(f"After left shift {i + 1}:  {result}")

    return result


def logical_right_shift(binary, positions):
    print("Original number:", binary)

    result = binary
    for i in range(positions):
        result = "0" + result[:-1]
        print(f"After right shift {i + 1}: {result}")

    return result


# (a) Logical left shift by 2 positions
print("(a) Logical Left Shift")
left_result = logical_left_shift("10110110", 2)
print("Final result:", left_result)
print("Verification:", left_result == "11011000")

print()

# (b) Logical right shift by 2 positions
print("(b) Logical Right Shift")
right_result = logical_right_shift("11010100", 2)
print("Final result:", right_result)
print("Verification:", right_result == "00110101")
