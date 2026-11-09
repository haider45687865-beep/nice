def generate_fibonacci_up_to(limit):
    """Generate Fibonacci sequence starting from 0 up to values less than or equal to limit."""
    if limit < 0:
        return []
    
    sequence = [0]
    if limit >= 1:
        sequence.append(1)
        while True:
            next_val = sequence[-1] + sequence[-2]
            if next_val > limit:
                break
            sequence.append(next_val)
            
    return sequence


if __name__ == "__main__":
    fib_series = generate_fibonacci_up_to(100)
    print(fib_series)
