import shutil
import os


# Function to move files into a selected_photos folder
def move_selected_photos(source_folder, selected_photos_folder, photos_to_move_file):
    """Moves files from a source folder to a selected_photos folder based on a list in a text file.

    Args:
      source_folder: The path to the folder containing the files to move.
      selected_photos_folder: The path to the folder where the selected photos should be moved.
      photos_to_move_file: The path to the text file containing the names of the photos to move.
    """

    # Create the selected_photos folder if it doesn't exist
    if not os.path.exists(selected_photos_folder):
        os.makedirs(selected_photos_folder)

    # Read the names of photos to move from the text file
    with open(photos_to_move_file, "r") as file:
        photos_to_move = [line.strip() for line in file]

    # Iterate through the files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file is in the list of photos to move
        if filename in photos_to_move:
            # Construct the full paths to the source and destination files
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(selected_photos_folder, filename)

            # Move the file
            shutil.move(source_file, destination_file)
            print(f"Moved {filename} to {selected_photos_folder}")

def main():
    # Replace these with your actual folder paths
    source_folder = "E:\\DCIM\\115D7000"
    selected_photos_folder = "E:\\DCIM\\115D7000\\selected_photos"
    photos_to_move_file = "E:\\DCIM\\115D7000\\photos_to_move.txt"

    move_selected_photos(source_folder, selected_photos_folder, photos_to_move_file)


if __name__ == "__main__":
    main()
