import os

def generate_music_list():
    # Supported audio formats
    audio_extensions = {'.mp3', '.ogg', '.wav', '.flac'}

    # Get current directory
    current_dir = os.getcwd()

    # Output file path
    output_file = os.path.join(current_dir, "music_list.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        for filename in os.listdir(current_dir):
            # Check extension
            _, ext = os.path.splitext(filename)
            if ext.lower() in audio_extensions:
                f.write(filename + "\n")

    print(f"music_list.txt created in: {current_dir}")

if __name__ == "__main__":
    generate_music_list()
