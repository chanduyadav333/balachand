def numbers():
    numbers_list = []
    while True:
        try:
            num = input("Enter a number (0 to stop): ")
            if num == '0':
                break
            numbers_list.append(float(num))
        except ValueError:
            print("Invalid input.")
    return numbers_list


def words():
    words_list = []
    while True:
        word = input("Enter a word (END to stop): ")
        if word.lower() == 'end':
            break
        words_list.append(word)
    return words_list


def main():
    numbers_obj = numbers()

    if numbers_obj:
        print("Ascending order:", sorted(numbers_obj))
        print("Descending order:", sorted(numbers_obj, reverse=True))

    words_obj = words()
    if words_obj:
        print("Ascending order:", sorted(words_obj))
        print("Descending order:", sorted(words_obj, reverse=True))


if __name__ == "__main__":
    main()
