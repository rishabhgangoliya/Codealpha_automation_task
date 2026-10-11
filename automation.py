import os
import re
import shutil

import requests


# ---------- Option 1: Move all .jpg files to a new folder ----------
def move_jpg_files(source_folder, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    moved = 0

    for name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, name)
        if os.path.isfile(source_path) and name.lower().endswith((".jpg", ".jpeg")):
            shutil.move(source_path, os.path.join(destination_folder, name))
            moved += 1
            print(f"Moved: {name}")

    print(f"\nDone! {moved} file(s) moved to '{destination_folder}'.")


# ---------- Option 2: Extract email addresses from a .txt file ----------
def extract_emails(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    emails = sorted(set(re.findall(pattern, text)))

    with open(output_file, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"Done! {len(emails)} unique email(s) saved to '{output_file}'.")


# ---------- Option 3: Scrape the title of a fixed webpage ----------
def scrape_title(url, output_file):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.I | re.S)
    title = match.group(1).strip() if match else "No title found"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(title + "\n")

    print(f"Page title: {title}")
    print(f"Saved to '{output_file}'.")


# ---------- Menu ----------
def main():
    print("=== Task Automation ===")
    print("1. Move all .jpg files to a new folder")
    print("2. Extract email addresses from a .txt file")
    print("3. Scrape the title of a webpage")
    choice = input("Choose 1, 2 or 3: ").strip()

    try:
        if choice == "1":
            source = input("Source folder path: ").strip()
            destination = input("New folder name/path: ").strip()
            move_jpg_files(source, destination)

        elif choice == "2":
            input_file = input("Input .txt file: ").strip()
            output_file = input("Output file (e.g. emails.txt): ").strip() or "emails.txt"
            extract_emails(input_file, output_file)

        elif choice == "3":
            url = input("Webpage URL (e.g. https://example.com): ").strip() or "https://example.com"
            scrape_title(url, "title.txt")

        else:
            print("Invalid choice. Please run again and pick 1, 2 or 3.")

    except FileNotFoundError:
        print("Error: file or folder not found. Check the path and try again.")
    except requests.RequestException as error:
        print(f"Error: could not load the webpage ({error}).")


if __name__ == "__main__":
    main()