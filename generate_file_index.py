import os

BASE_DIR = "files"
PASSWORD = "anurag718"  # Change this to your password

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Protected Files</title>
  <style>
    body {{
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }}
    #login, #files {{
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      flex-direction: column;
    }}
    input {{
      padding: 10px;
      font-size: 16px;
      margin-bottom: 10px;
    }}
    button {{
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
    }}
    #files ul {{
      list-style-type: none;
      padding: 0;
    }}
    #files li {{
      margin: 5px 0;
    }}
  </style>
</head>
<body>

<div id="login">
  <h2>Enter Password to Access Files</h2>
  <input type="password" id="password" placeholder="Password" />
  <button onclick="checkPassword()">Submit</button>
  <p id="error" style="color:red;"></p>
</div>

<div id="files" style="display:none;">
  <h2>Available Files</h2>
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

(function() {{
  document.addEventListener('contextmenu', e => e.preventDefault());

  document.addEventListener('keydown', function(e) {{
    if (
      e.key === "F12" ||
      (e.ctrlKey && e.shiftKey && ['I','J','C'].includes(e.key)) ||
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
        print(f"Error: '{BASE_DIR}' directory not found.")
        return
    generate_index(BASE_DIR, BASE_DIR)

if __name__ == "__main__":
    main()
