const fs = require('fs');
const path = require('path');

// --- Configuration ---
// The directory where your PDFs are stored, relative to the project root.
const pdfDirectory = path.join(__dirname, '/');
// The path to your gallery HTML file, relative to the project root.
const galleryHtmlPath = path.join(pdfDirectory, 'gallery.html');
// --- End Configuration ---

console.log(`Scanning for PDF files in: ${pdfDirectory}`);

// 1. Find all .pdf files in the directory
const pdfFiles = fs.readdirSync(pdfDirectory).filter(file => {
  return path.extname(file).toLowerCase() === '.pdf';
});

if (pdfFiles.length === 0) {
  console.log('No PDF files found. No changes made.');
  return;
}

console.log(`Found ${pdfFiles.length} PDF(s):`, pdfFiles);

// 2. Read the gallery.html file
let htmlContent = fs.readFileSync(galleryHtmlPath, 'utf8');

// 3. Create the new array string
const pdfsArrayString = JSON.stringify(pdfFiles, null, 2).replace(/"/g, '  "');

// 4. Replace the old PDFS array with the new one
const regex = /const PDFS = \[[\s\S]*?\];/;
const newHtmlContent = htmlContent.replace(regex, `const PDFS = [\n${pdfFiles.map(f => `      "${f}"`).join(',\n')}\n    ];`);

// 5. Write the updated content back to the file
fs.writeFileSync(galleryHtmlPath, newHtmlContent, 'utf8');

console.log(`✅ Successfully updated ${path.basename(galleryHtmlPath)} with the new file list!`);