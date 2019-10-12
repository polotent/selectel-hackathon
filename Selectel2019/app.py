from flask import Flask, request, send_from_directory, render_template
from text_processor import TextProcessor
from git_api import GitProcessor


app = Flask(__name__, static_url_path='/static/')


@app.route('/')
def hello():
    return render_template("main.html")


@app.route('/link-request', methods=['POST'])
def response():
    link = request.form['link']

    text_processor = TextProcessor()

    if text_processor.validate_link(link):
        git_processor = GitProcessor(link)
        git_history = git_processor.get_history(5)
        return render_template("report_generator.html", history=git_history)
    else:
        return render_template("main.html", text="Invalid Git Repository Link")

# Sering Static File
@app.route('/<path:path>')
def send_files(path):
    return send_from_directory('/', path)
