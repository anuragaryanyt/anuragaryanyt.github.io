import os

BASE_DIR = "files"
PASSWORD = "yourpassword"  # Change this to your password

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🔐 Protected File Explorer - {path}</title>
<style>
  body {
    font-family: Arial, sans-serif;
    padding: 20px;
    background: #f2f2f2;
    margin: 0;
  }

  h1 {
    font-size: 1.4rem;
    margin-bottom: 20px;
  }

  #login {
    max-width: 400px;
    margin: 0 auto;
    padding: 16px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  }

  #files {
    display: none;
  }

  .file-list {
    max-width: 800px;
    margin: 0 auto;
  }

  .file-list ul {
    list-style-type: none;
    padding: 0;
  }

  .file-list li {
    margin: 6px 0;
    background: white;
    border-radius: 6px;
    padding: 12px 16px;
    font-size: 1rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .file-list li a {
    text-decoration: none;
    color: #0077cc;
    flex-grow: 1;
  }

  .file-list li a:hover {
    text-decoration: underline;
  }

  input[type="password"] {
    width: 100%;
    padding: 10px;
    font-size: 1rem;
    margin-bottom: 12px;
    border: 1px solid #ccc;
    border-radius: 6px;
  }

  button {
    width: 100%;
    padding: 10px;
    background-color: #0077cc;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1rem;
    cursor: pointer;
  }

  button:hover {
    background-color: #005fa3;
  }

  @media (max-width: 600px) {
    h1 {
      font-size: 1.1rem;
    }

    .file-list li {
      padding: 10px;
      font-size: 0.95rem;
    }

    input, button {
      font-size: 0.95rem;
    }
  }
</style>
</head>
<body>

<h1>🔐 Protected File Explorer - {path}</h1>

<div id="login">
  <p>Enter password to view files:</p>
  <form id="password-form">
    <input type="password" id="password-input" placeholder="Enter password">
    <button type="submit">Submit</button>
    <p id="error" style="color:red;"></p>
  </form>
</div>

<div id="files" class="file-list">
  <ul>
  {items}
  </ul>
</div>

<script>
const correctPassword = "{password}";

document.getElementById("password-form").addEventListener("submit", function(e) {
  e.preventDefault();
  const input = document.getElementById("password-input").value;
  if (input === correctPassword) {
    document.getElementById("login").style.display = "none";
    document.getElementById("files").style.display = "block";
  } else {
    document.getElementById("error").innerText = "Incorrect password.";
  }
});
</script>

</body>
</html>

"""


def generate_index(folder_path, web_path):
    items_html = []

    # Add parent link if not root
    if web_path != BASE_DIR:
        items_html.append('<li><a href="../">⬆️ ../ (Parent Directory)</a></li>')

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
        password=PASSWORD
    )

    index_file = os.path.join(folder_path, "index.html")
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Generated: {index_file}")

def main():
    if not os.path.exists(BASE_DIR):
        print(f"Error: '{BASE_DIR}' directory not found.")
        return
    generate_index(BASE_DIR, BASE_DIR)

if __name__ == "__main__":
    main()
