import os

def generate_wallpaper_list():
    # Supported image formats
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'}

    # Current directory
    current_dir = os.getcwd()

    # Output file
    output_file = os.path.join(current_dir, "wallpaper_list.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        for filename in os.listdir(current_dir):
            _, ext = os.path.splitext(filename)
            if ext.lower() in image_extensions:
                f.write(filename + "\n")

    print(f"wallpaper_list.txt created in: {current_dir}")

if __name__ == "__main__":
    generate_wallpaper_list()
