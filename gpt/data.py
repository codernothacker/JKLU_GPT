import os

def accumulate_text(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.txt'):
                file_path = os.path.join(folder_path, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as in_file:
                        text = in_file.read()
                        out_file.write(text)
                        out_file.write('\n')  # Add a new line after each file's content
                except UnicodeDecodeError:
                    print(f"UnicodeDecodeError: Unable to decode file '{file_path}'")

# Specify the folder containing the .txt files
folder_path = r"D:\Minor_Project\ng-video-lecture-master\D1.7GB"

# Specify the output file where accumulated text will be saved
output_file = "accumulated_text.txt"

# Call the function to accumulate text
accumulate_text(folder_path, output_file)

print("Text accumulated successfully!")
