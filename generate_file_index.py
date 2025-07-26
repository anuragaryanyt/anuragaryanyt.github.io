import os

BASE_DIR = "files"
PASSWORD = "yourpassword"  # Change this to your password

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>File Explorer - {path}</title>
<style>
body {{ font-family: Arial, sans-serif; padding: 20px; }}
h1 {{ font-size: 22px; }}
ul {{ list-style-type: none; padding: 0; }}
li {{ margin: 4px 0; }}
a {{ text-decoration: none; color: blue; }}
a:hover {{ text-decoration: underline; }}
#files {{ display: none; }}
</style>
</head>
<body>
<h1>Protected File Explorer - {path}</h1>

<div id="login">
  <p>Enter password to view files:</p>
  <input type="password" id="password">
  <button onclick="checkPassword()">Submit</button>
  <p id="error" style="color:red;"></p>
</div>

<div id="files">
  <ul>
  {items}
  </ul>
</div>

<script>
const correctPassword = "{password}";

function checkPassword() {{
  const input = document.getElementById("password").value;
  if (input === correctPassword) {{
    document.getElementById("login").style.display = "none";
    document.getElementById("files").style.display = "block";
  }} else {{
    document.getElementById("error").innerText = "Incorrect password.";
  }}
}}
</script>

</body>
</html>
"""

def generate_index(folder_path, web_path):
    items_html = []

    # Add link to parent directory if not root
    if web_path != BASE_DIR:
        items_html.append('<li><a href="../">../ (Parent Directory)</a></li>')

    for item in sorted(os.listdir(folder_path)):
        if item == "index.html":
            continue
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            items_html.append(f'<li>📁 <a href="{item}/">{item}/</a></li>')
            generate_index(item_path, f"{web_path}/{item}")
        else:
            items_html.append(f'<li>📄 <a href="{item}">{item}</a></li>')

    html_content = HTML_TEMPLATE.format(
        path=web_path,
        items="\n".join(items_html),
        password=anurag718
    )

    index_file = os.path.join(folder_path, "index.html")
    with open(index_file, "w") as f:
        f.write(html_content)

    print(f"✅ Generated: {index_file}")

def main():
    if not os.path.exists(BASE_DIR):
        print(f"Error: '{BASE_DIR}' directory not found.")
        return
    generate_index(BASE_DIR, BASE_DIR)

if __name__ == "__main__":
    main()
