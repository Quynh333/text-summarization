from flask import Flask, render_template, request
from summarizer import summarize
import docx

app = Flask(__name__)

# đọc file txt
def read_txt(file):
    return file.read().decode("utf-8")

# đọc file docx
def read_docx(file):
    doc = docx.Document(file)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)


@app.route("/", methods=["GET", "POST"])
def index():

    summary = ""
    original_text = ""

    if request.method == "POST":

        text_input = request.form.get("text")
        file = request.files.get("file")

        if file and file.filename != "":

            if file.filename.endswith(".txt"):
                original_text = read_txt(file)

            elif file.filename.endswith(".docx"):
                original_text = read_docx(file)

        elif text_input and text_input.strip() != "":
            original_text = text_input

        
        if original_text.strip() != "":
            summary = summarize(original_text)

    return render_template(
        "index.html",
        summary=summary,
        original_text=original_text
    )


if __name__ == "__main__":
    app.run(debug=True)