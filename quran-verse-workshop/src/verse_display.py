# verse_display.py

def display_verses():
    try:
        with open("data/quran_verses.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("The file 'quran_verses.txt' was not found.")

if __name__ == "__main__":
    display_verses()
