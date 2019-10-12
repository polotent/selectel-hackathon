from flask import Flask, request, send_from_directory, render_template
from text_processor import TextProcessor
from git_api import GitProcessor


app = Flask(__name__, static_url_path='/static/')


@app.route('/')
def index():
    return render_template("main.html")


@app.route('/debug')
def debug():
    return render_template("report_generator.html")


@app.route('/link-request', methods=['POST'])
def response():
    link = request.form['link']

    text_processor = TextProcessor()

    if text_processor.validate_link(link):
        git_processor = GitProcessor(link)
        git_initial_history = git_processor.get_initial_history(5)
        return render_template("report_generator.html", history=git_initial_history, repo_link=link)
    else:
        return render_template("main.html", text="Invalid Git Repository Link")


@app.route('/get_history', methods=['POST'])
def get_history():
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    link = request.form['repo_link']
    git_processor = GitProcessor(link)
    return git_processor.get_history_by_period(start_time=start_time, end_time=end_time)


# Serving Static File
@app.route('/<path:path>')
def send_files(path):
    return send_from_directory('/', path)
