function copyCode(button) {
    const codeElement = button.parentElement.querySelector("code");
    const text = codeElement.innerText.trim();
  
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text).then(() => {
        button.textContent = "Copied!";
        setTimeout(() => button.textContent = "Copy", 2000);
      }).catch(err => fallbackCopy(text, button));
    } else {
      fallbackCopy(text, button);
    }
  }
  
  function fallbackCopy(text, button) {
    const textarea = document.createElement("textarea");
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand("copy");
      button.textContent = "Copied!";
      setTimeout(() => button.textContent = "Copy", 2000);
    } catch (err) {
      alert("Copy not supported.");
    }
    document.body.removeChild(textarea);
  }
  