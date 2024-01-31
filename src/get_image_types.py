import os
import mimetypes

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

def print_formatted_table(directory_counts):
    print(f"{'Directory':<20} | {'Image Count':>12}")
    print("-" * 35)
    for dir_name, count in directory_counts.items():
        print(f"{dir_name:<20} | {count:>12}")

directory = '/Users/m041946/Documents/2024-1-Winter/AIHC-5010/final_project/data/ACL-fig/training_data/train'
image_types, total_images, directory_counts = get_image_types_and_counts(directory)

print_formatted_table(directory_counts)
print(f"\nTotal images processed: {total_images}")
print("Image types found:", image_types)
