function copyCode(button) {
    // Get the code block content
    var codeBlock = button.previousElementSibling; // Previous element is the <code> block
    var codeText = codeBlock.textContent || codeBlock.innerText; // Get the text inside <code>

    // Create a temporary text area to copy the text
    var textArea = document.createElement('textarea');
    textArea.value = codeText; // Set the code text
    document.body.appendChild(textArea); // Append to body to make it selectable

    textArea.select(); // Select the text
    document.execCommand('copy'); // Copy the selected text to clipboard

    document.body.removeChild(textArea); // Remove the text area

    // Provide feedback to the user
    alert('Code copied to clipboard!');
}