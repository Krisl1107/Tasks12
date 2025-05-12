def lucky_ticket(number):

    number = number.replace(" ", "")

    if len(number) % 2 != 0:
        return False
    half= len(number) // 2
    first_half = number[:half]
    second_half = number[half:]

    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)
    return sum_first_half == sum_second_half

def main():
    ticket_count = 0
    while True:
        number = input("Введите номер билета: ")
        ticket_count += 1
        if lucky_ticket(number):
            print(f"Счастливый билет найден! Порядковый номер: {ticket_count}")
            break

main()
