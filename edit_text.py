# Read the original lines
with open('Media to consume.txt', 'r') as file:
    lines = file.readlines()

# Ensure only unique, valid lines and append '|'
cleaned_lines = []
for line in lines:
    stripped_line = line.strip()  # Remove extra spaces/newlines
    if stripped_line and stripped_line not in cleaned_lines:  # Avoid duplicates
        cleaned_lines.append(stripped_line + 'No|Hrs|G|S|\n')

# Overwrite the file with cleaned-up lines
with open('Media to consume.txt', 'w') as file:
    file.writelines(cleaned_lines)