import re

def main():
    regex_input = input("Enter a regular expression: ")
    try:
        pattern = re.compile(regex_input)
    except re.error as err:
        print(f"Invalid regular expression: {err}")
        return
    filename = "mbox.txt"
    match_count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.rstrip()
                if pattern.search(line):
                    match_count += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    print(f"{filename} had {match_count} lines that matched {regex_input}")
if __name__ == "__main__":
    main()
