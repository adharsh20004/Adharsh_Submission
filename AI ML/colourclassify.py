def classify_color(rgb):
    red_range = range(150, 256)
    blue_range = range(0, 100)
    green_range = range(0, 100)

    r, g, b = rgb

    if r in red_range and g in green_range and b in blue_range:
        return "Red"
    elif r in blue_range and g in green_range and b in red_range:
        return "Blue"
    elif r in green_range and g in blue_range and b in red_range:
        return "Green"
    else:
        return "other"

# Prompt the user to enter RGB values
r = int(input("Enter the value of R (0-255): "))
g = int(input("Enter the value of G (0-255): "))
b = int(input("Enter the value of B (0-255): "))

rgb_values = (r, g, b)
color_category = classify_color(rgb_values)

print("Color Category:", color_category)
