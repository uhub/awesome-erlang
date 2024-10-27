import yaml
import sys
from collections import defaultdict

def generate_readme(input_file, output_file):
    with open(input_file, 'r') as f:
        data = yaml.safe_load(f)

    categories = defaultdict(list)
    duplicates = []

    # Each item in the list is a dictionary with:
    # - category: The category of the repository
    # - repo_url: The URL of the repository
    # - description: A short description of the repository

    for item in data:
        category = item.get('category', 'Uncategorized')
        categories[category].append(item)

    # Sort categories and items
    sorted_categories = sorted(categories.items())

    with open(output_file, 'w') as f:
        for category, repos in sorted_categories:
            f.write(f"## {category}\n\n")
            for repo in sorted(repos, key=lambda x: x['repo_url']):
                repo_path = repo['repo_url'].split('/')
                repo_name = repo_path[-1]
                if repo_name in duplicates:
                    repo_name = repo_path[-2] + '/' + repo_path[-1]
                f.write(f"* [{repo_name}]({repo['repo_url']}) - {repo['description']}\n")
            f.write("\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_readme.py <input_file> <output_file>")
        sys.exit(1)

    generate_readme(sys.argv[1], sys.argv[2])

