from flask import Flask, request
import PyPDF2

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']

    if file.filename == '':
        return "No selected file", 400

    if file and file.filename.endswith('.pdf'):
        # PDF ko read karen (PyPDF2 ka latest version use karte hue)
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text, 200
    else:
        return "Invalid file format. Please upload a PDF.", 400

if __name__ == '__main__':
    app.run(debug=True)
