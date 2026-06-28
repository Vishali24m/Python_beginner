def display_profile(name, age, pet, favorite_color):
    """Display a profile card with proper alignment."""

    # Create a boxed profile display
    border = "+" + "-" * 32 + "+"
    empty_row = "|" + " " * 32 + "|"

    # Build profile content rows with alignment
    def format_row(label, value):
        label_text = f"{label}:"
        return f"|  {label_text:<12} {value:<18}|"

    # Print the profile card
    print("\n" + border)
    print(empty_row)
    print(f"|{'PROFILE':^32}|")
    print(empty_row)
    print(border)
    print(empty_row)
    print(format_row("Name", name))
    print(format_row("Age", f"{age} years old"))
    print(format_row("Pet", pet))
    print(format_row("Fav. Color", favorite_color))
    print(empty_row)
    print(border + "\n")

if __name__ == "__main__":
    # Sample profile data
    profile = {
        "name": "Alexandra Chen",
        "age": 28,
        "pet": "Golden Retriever",
        "favorite_color": "Teal"
    }

    display_profile(
        name=profile["name"],
        age=profile["age"],
        pet=profile["pet"],
        favorite_color=profile["favorite_color"]
    )
