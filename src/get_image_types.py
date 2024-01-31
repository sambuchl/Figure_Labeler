import os
import mimetypes
from datetime import datetime

def get_image_types_and_counts(directory):
    image_extensions = set()
    total_image_count = 0
    directory_counts = {}

    for dirpath, dirnames, filenames in os.walk(directory):
        directory_name = os.path.basename(dirpath)
        directory_image_count = 0

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type and mime_type.startswith('image'):
                extension = os.path.splitext(filename)[1].lower()
                image_extensions.add(extension)
                directory_image_count += 1

        if directory_image_count > 0:
            directory_counts[directory_name] = directory_image_count
            total_image_count += directory_image_count

    return image_extensions, total_image_count, directory_counts

def print_formatted_table(directory_counts, file):
    file.write(f"{'Directory':<20} | {'Image Count':>12}\n")
    file.write("-" * 35 + "\n")
    for dir_name, count in directory_counts.items():
        file.write(f"{dir_name:<20} | {count:>12}\n")

directory = '/Users/m041946/Documents/2024-1-Winter/AIHC-5010/final_project/Figure_Labeler/data/ACL-fig/training_data/train'
image_types, total_images, directory_counts = get_image_types_and_counts(directory)

# Get current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

# File to save the results
output_file_path = f'image_class_report_{current_datetime}.txt'

with open(output_file_path, 'w') as file:
    file.write(f"Report generated on {current_datetime}\n")
    file.write(f"Source Folder: {directory}\n\n")
    print_formatted_table(directory_counts, file)
    file.write(f"\nTotal images processed: {total_images}\n")
    file.write("Image types found: " + ", ".join(image_types) + "\n")

print(f"Report saved to {output_file_path}")