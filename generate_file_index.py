import os

folder = "files"
files = sorted(os.listdir(folder))

html = """<!DOCTYPE html>
<html>
<head>
<title>File Explorer</title>
<style>
body { font-family: Arial, sans-serif; padding: 20px; }
h1 { font-size: 24px; }
ul { list-style: none; padding: 0; }
li { margin: 5px 0; }
a { text-decoration: none; color: blue; }
a:hover { text-decoration: underline; }
</style>
</head>
<body>
<h1>Download Files</h1>
<ul>
"""

for f in files:
    if f != "files.html":
        html += f'<li><a href="{f}">{f}</a></li>\n'

html += "</ul></body></html>"

with open(os.path.join(folder, "files.html"), "w") as f:
    f.write(html)

print("✅ files.html generated successfully!")
