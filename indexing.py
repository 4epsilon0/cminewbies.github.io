import os

PDF_DIR = "pdf"  # folder containing PDFs
OUTPUT_FILE = "index.html"
SITE_TITLE = "Research Papers"

# Get list of PDFs in the directory
pdf_files = sorted([f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")])

# Generate HTML content
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{SITE_TITLE}</title>
</head>
<body>
    <h1>{SITE_TITLE}</h1>
    <ul>
"""

for pdf in pdf_files:
    html_content += f'        <li><a href="{PDF_DIR}/{pdf}">{pdf}</a></li>\n'

html_content += """    </ul>
</body>
</html>
"""

# Write to file
with open(OUTPUT_FILE, "w") as f:
    f.write(html_content)

print(f"✅ index.html generated with {len(pdf_files)} PDFs.")

