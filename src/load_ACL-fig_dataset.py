from datasets import load_dataset

# If the dataset is gated/private, make sure you have run huggingface-cli login
dataset = load_dataset("citeseerx/ACL-fig")
dataset.save_to_disk("/Users/m041946/Documents/2024-1-Winter/AIHC-5010/final_project/data/ACL-fig")