import sys
import os

# 1. Define the fields you want to replace
replacements = {
    "[Insert App Name]": "Collage Gold",
    "[Insert Date]": "2026-Dec-01",
    "[VERSION]": "v1.0",
    "[Insert Developer/Company Name]": "DITR Code Company",
    "[Insert Support Email]": "paugoert@gmail.com",
    "[Insert Business Address]": "Rm. 304, Ming Hoi Hse., Ming Nga Crt., Tai Po, N.T., H.K.",
    "[Insert Business Address - Required for Trader Status]": "Rm. 304, Ming Hoi Hse., Ming Nga Crt., Tai Po, N.T., H.K.",
    "[Insert Your Support Email]": "paugoert@gmail.com",
    "[Insert Your Business Address - Required for Traders]": "Rm. 304, Ming Hoi Hse., Ming Nga Crt., Tai Po, N.T., H.K.",
    "[Insert Link to Privacy Policy if available]": "https://abc.com",
    "[Insert Your Country/State]": "Hong Kong"
}

# 1. Check if a filename was provided via command line
if len(sys.argv) < 2:
    print("Error: No input file provided.")
    print("Syntax: python3 generate.py <file_name>")
    print("Example: python3 generate.py eula.md")
    sys.exit(1)

# Get the target file name from the arguments
input_filename = sys.argv[1]

# 2. Read the template dynamically
try:
    with open(input_filename, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' could not be found.")
    sys.exit(1)

# 3. Automate the swap (using your existing replacements dictionary)
for placeholder, value in replacements.items():
    content = content.replace(placeholder, value)

# 4. Save to generated_<file_name>
# os.path.basename ensures it works cleanly even if you pass a path like folder/eula.md
base_name = os.path.basename(input_filename)
output_filename = f"generated_{base_name}"

with open(output_filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully generated {output_filename}!")
