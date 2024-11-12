import os

# Step 1: Create Project Structure
project_name = "quran-verse-workshop"
os.makedirs(f"{project_name}/data", exist_ok=True)
os.makedirs(f"{project_name}/src", exist_ok=True)

# Step 2: Create README.md
readme_content = """# Quran Verse Workshop
This is a simple GitHub workshop project where participants add their favorite Quran verse to `data/quran_verses.txt` and test the Python script that displays all the entries.
"""
with open(f"{project_name}/README.md", "w") as readme_file:
    readme_file.write(readme_content)

# Step 3: Create data/quran_verses.txt
with open(f"{project_name}/data/quran_verses.txt", "w") as data_file:
    data_file.write("")  # Create an empty file

# Step 4: Create src/verse_display.py
python_script = """# verse_display.py

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
"""
with open(f"{project_name}/src/verse_display.py", "w") as python_file:
    python_file.write(python_script)

print(f"Project '{project_name}' has been created with the necessary files!")
