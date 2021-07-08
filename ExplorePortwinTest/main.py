# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    with open("echantillon.txt", "r") as echantillonReader:
        buffer = echantillonReader.readlines()
        print(*buffer)
        last = buffer[len(buffer) - 1]
        print(last)
        last_index = int(last.split('\t')[0])
        print(last_index)
        if isinstance(last_index, int):
            print(f"last index is {last_index}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
