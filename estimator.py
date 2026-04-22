# ==============================
# BUILDSMART ESTIMATOR
# ==============================

# Standard room sizes (meters)
ROOM_SIZES = {
    "bedroom": (3, 3),
    "bathroom": (2, 2),
    "kitchen": (3, 2.5),
    "dining": (3, 3),
    "sitting": (4, 3)
}

WALL_HEIGHT = 3
BLOCKS_PER_M2 = 50
CEMENT_PER_100_BLOCKS = 1


# ==============================
# PARSE DESCRIPTION
# ==============================
def parse_description(desc):
    desc = desc.lower()

    data = {
        "bedroom": 0,
        "bathroom": 0,
        "kitchen": 0,
        "dining": 0,
        "sitting": 0
    }

    if "1 bedroom" in desc:
        data["bedroom"] = 1
    elif "2 bedroom" in desc:
        data["bedroom"] = 2
    elif "3 bedroom" in desc:
        data["bedroom"] = 3
    elif "4 bedroom" in desc:
        data["bedroom"] = 4

    if "1 bathroom" in desc:
        data["bathroom"] = 1
    elif "2 bathroom" in desc:
        data["bathroom"] = 2

    if "kitchen" in desc:
        data["kitchen"] = 1

    if "dining" in desc:
        data["dining"] = 1

    if "sitting" in desc or "living room" in desc:
        data["sitting"] = 1

    return data


# ==============================
# CALCULATE MATERIALS
# ==============================
def calculate_materials(data):
    total_area = 0

    for room, count in data.items():
        if count > 0:
            length, width = ROOM_SIZES[room]
            total_area += length * width * count

    perimeter = (total_area ** 0.5) * 4
    wall_area = perimeter * WALL_HEIGHT

    blocks = wall_area * BLOCKS_PER_M2
    cement = blocks / 100

    # Foundation (stones)
    stones = total_area * 0.5

    # Iron sheets (roofing)
    roof_area = total_area * 1.2
    iron_sheets = roof_area / 1.5

    return total_area, wall_area, int(blocks), int(cement), int(stones), int(iron_sheets)


# ==============================
# DISPLAY RESULTS
# ==============================
def display_results(data, total_area, wall_area, blocks, cement, stones, iron_sheets):
    print("\n===== HOUSE SUMMARY =====")
    for room, count in data.items():
        if count > 0:
            print(f"{room.capitalize()}(s): {count}")

    print("\n===== MATERIAL ESTIMATION =====")
    print(f"Floor Area: {total_area:.2f} m²")
    print(f"Wall Area: {wall_area:.2f} m²")

    print("\n--- Materials ---")
    print(f"Bricks/Blocks: {blocks}")
    print(f"Cement: {cement} bags")
    print(f"Foundation Stones: {stones} units")
    print(f"Iron Sheets: {iron_sheets} sheets")

    print("\nNOTE: Estimates are based on standard assumptions.")


# ==============================
# EDIT / DELETE SYSTEM
# ==============================
def edit_or_delete_description(description):
    while True:
        print("\n===== CONFIRM YOUR INPUT =====")
        print("Your house description:")
        print(description)

        print("\nOptions:")
        print("1 - Edit description")
        print("2 - Delete and re-enter")
        print("3 - Continue")

        choice = input("Choose option: ")

        if choice == "1":
            description = input("\nEnter corrected description:\n> ")

        elif choice == "2":
            description = input("\nRe-enter house description:\n> ")

        elif choice == "3":
            return description

        else:
            print("Invalid option. Try again.")


# ==============================
# MAIN PROGRAM
# ==============================
def main():
    print("=== BUILDSMART ESTIMATOR ===")

    description = input("\nDescribe your house:\n> ")

    description = edit_or_delete_description(description)

    data = parse_description(description)

    if sum(data.values()) == 0:
        print("Could not understand input. Try again.")
        return

    total_area, wall_area, blocks, cement, stones, iron_sheets = calculate_materials(data)

    display_results(data, total_area, wall_area, blocks, cement, stones, iron_sheets)


# RUN PROGRAM
main()