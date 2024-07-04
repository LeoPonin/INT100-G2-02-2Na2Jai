import random

def main():
    characters = {}

    while True:
        print("\nMenu:")
        print("1. Add a new character")
        print("2. Check a character's stats")
        print("3. Delete a character")
        print("4. Display all characters")
        print("5. Roll a d20 for a character stat")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_character(characters)
        elif choice == '2':
            check_character_stats(characters)
        elif choice == '3':
            delete_character(characters)
        elif choice == '4':
            display_all_characters(characters)
        elif choice == '5':
            roll_d20_for_character_stat(characters)
        elif choice == '6':
            break
        else:
            print("Invalid option. Please choose again.")

    print("\nExiting program...")

def add_character(characters):
    name = input("Enter the character's name: ").strip()

    if name in characters:
        print(f"A character named {name} already exists.")
        return

    try:
        str_stat = int(input("Enter STR (Strength): "))
        dex_stat = int(input("Enter DEX (Dexterity): "))
        con_stat = int(input("Enter CON (Constitution): "))
        int_stat = int(input("Enter INT (Intelligence): "))
        wis_stat = int(input("Enter WIS (Wisdom): "))
        cha_stat = int(input("Enter CHA (Charisma): "))
    except ValueError:
        print("Invalid input. Please enter integer values for stats.")
        return

    characters[name] = {
        "STR": str_stat,
        "DEX": dex_stat,
        "CON": con_stat,
        "INT": int_stat,
        "WIS": wis_stat,
        "CHA": cha_stat
    }
    print(f"Character {name} added successfully!")

def check_character_stats(characters):
    name = input("Enter the character's name to check stats: ").strip()
    if name in characters:
        stats = characters[name]
        print(f"\nStats for {name}:")
        for stat, value in stats.items():
            print(f"{stat}: {value}")
    else:
        print(f"No character named {name} found.")

def delete_character(characters):
    name = input("Enter the character's name to delete: ").strip()
    if name in characters:
        confirm = input(f"Are you sure you want to delete {name}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del characters[name]
            print(f"Character {name} has been deleted.")
        else:
            print(f"Deletion of {name} canceled.")
    else:
        print(f"No character named {name} found.")

def display_all_characters(characters):
    if not characters:
        print("No characters stored.")
        return

    for character_name, stats in characters.items():
        print(f"\nName: {character_name}")
        for stat, value in stats.items():
            print(f"{stat}: {value}")

def roll_d20_for_character_stat(characters):
    name = input("Enter the character's name for the d20 roll: ").strip()
    if name in characters:
        print("Available stats to use:")
        print("1. STR (Strength)")
        print("2. DEX (Dexterity)")
        print("3. CON (Constitution)")
        print("4. INT (Intelligence)")
        print("5. WIS (Wisdom)")
        print("6. CHA (Charisma)")
        choice = input("Choose a stat to use for the d20 roll (1-6): ").strip()

        if choice == '1':
            stat_name = "STR"
        elif choice == '2':
            stat_name = "DEX"
        elif choice == '3':
            stat_name = "CON"
        elif choice == '4':
            stat_name = "INT"
        elif choice == '5':
            stat_name = "WIS"
        elif choice == '6':
            stat_name = "CHA"
        else:
            print("Invalid choice.")
            return

        stat_value = characters[name][stat_name]
        roll_result = random.randint(1, 20)
        final_result = roll_result + stat_value
        print(f"\n{name} rolled a d20 and got: {roll_result}")
        print(f"Using {stat_name} ({stat_value}), the final result is: {final_result}")
    else:
        print(f"No character named {name} found.")

if __name__ == "__main__":
    main()
