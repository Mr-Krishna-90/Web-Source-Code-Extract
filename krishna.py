import os
import requests

# Function to generate folder if not exists
def generate_folder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"\033[92mFolder created at: {path}\033[0m")
        else:
            print(f"\033[92mFolder already exists at: {path}\033[0m")
    except Exception as e:
        print("\033[91mError creating folder:", e, "\033[0m")

# Function to save HTML content to a file
def save_html_to_file(html_content, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"\033[92mHTML content saved to file: {file_path}\033[0m")
    except Exception as e:
        print("\033[91mError saving HTML content to file:", e, "\033[0m")

# Define the target website URL
target_url = input("\033[95mEnter the URL of the website you want to hack: \033[0m")

# Send a GET request to the website
response = requests.get(target_url)

# Check if the request was successful
if response.status_code == 200:
    # Define the folder path to save files
    folder_path = '/storage/emulated/0/Download/Krishna✓'

    # Generate folder if not exists
    generate_folder(folder_path)

    # Save HTML content to a file
    html_file_path = os.path.join(folder_path, 'index.html')
    save_html_to_file(response.text, html_file_path)

    # Save additional text to a file
    text_content = "\033[93mThanks for using our tool! This awesome tool was made by @krishna12120.\033[0m"
    text_file_path = os.path.join(folder_path, 'krishna.txt')
    with open(text_file_path, 'w') as f:
        f.write(text_content)

    print("\033[92mCongratulations! You've successfully hacked into the website.\033[0m")
    print("\033[92mFiles saved successfully.\033[0m")
else:
    print("\033[91mOops! Something went wrong. It seems we couldn't hack into the website.\033[0m")