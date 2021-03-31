def main():
    user_input = int(input("Please enter an integer:"))
    print(summation(user_input))

def summation(number):
    total = 0
    for num in range(number + 1):
        total += num
    return total

if __name__ == "__main__":
    print(summation(6))