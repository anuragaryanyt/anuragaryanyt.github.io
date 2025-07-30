import os

BASE_DIR = "files"
PASSWORD = "anurag718"  # Change this to your password

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>File Explorer - {path}</title>
  <style>
    body {{
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      padding: 20px;
      background: #f0f0f0;
      color: #222;
      max-width: 100%;
    }}

    h1 {{
      font-size: 2rem;
      text-align: center;
      margin-bottom: 20px;
    }}

    #login {{
      text-align: center;
      padding: 10px;
    }}

    input[type="password"] {{
      padding: 14px;
      width: 90%;
      max-width: 350px;
      font-size: 18px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }}

    button {{
      padding: 14px 28px;
      font-size: 18px;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }}

    button:hover {{
      background-color: #0056b3;
    }}

    #error {{
      color: red;
      margin-top: 10px;
      font-size: 16px;
    }}

    #files {{
      display: none;
      margin-top: 20px;
    }}

    ul {{
      list-style-type: none;
      padding: 0;
    }}

    li {{
      font-size: 1.2rem;
      margin: 12px 0;
      padding: 12px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}

    a {{
      color: #007BFF;
      text-decoration: none;
      word-wrap: break-word;
    }}

    a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>

<h1>🔐 Protected File Explorer - {path}</h1>

<div id="login">
  <p style="font-size:18px;">Enter password to access files:</p>
  <input type="password" id="password" placeholder="Enter password..."><br>
  <button onclick="checkPassword()">Unlock</button>
  <p id="error"></p>
</div>

<div id="files">
  <ul>
    {items}
  </ul>
</div>

<script>
  const correctPassword = "{password}";

  function checkPassword() {{
    const inputElem = document.getElementById("password");
    const input = inputElem.value;
    if (input === correctPassword) {{
      document.getElementById("login").style.display = "none";
      document.getElementById("files").style.display = "block";
    }} else {{
      document.getElementById("error").innerText = "Incorrect password.";
      inputElem.value = "";
      inputElem.focus();
    }}
  }}

  document.addEventListener("DOMContentLoaded", function () {{
    const passwordInput = document.getElementById("password");
    passwordInput.addEventListener("keypress", function (e) {{
      if (e.key === "Enter") {{
        checkPassword();
      }}
    }});
  }});

  (function () {{
    document.addEventListener('contextmenu', function (e) {{
      e.preventDefault();
    }});

    document.addEventListener('keydown', function (e) {{
      if (
        e.key === "F12" ||
        (e.ctrlKey && e.shiftKey && ['I', 'J', 'C'].includes(e.key)) ||
        (e.ctrlKey && e.key === 'U')
      ) {{
        e.preventDefault();
      }}
    }});

    const threshold = 160;
    setInterval(() => {{
      const t0 = performance.now();
      debugger;
      const t1 = performance.now();
      if (t1 - t0 > threshold) {{
        alert("DevTools is disabled!");
        location.reload();
      }}
    }}, 1000);
  }})();
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
        print(f"❌ Error: '{BASE_DIR}' directory not found.")
        return
    generate_index(BASE_DIR, BASE_DIR)

if __name__ == "__main__":
    main()
