from flask import Flask, request, send_from_directory, render_template
from text_processor import TextProcessor
from git_api import GitProcessor
from time_parser import TimeParser

app = Flask(__name__, static_url_path='/static/')
INITIAL_COMMITS = 10


@app.route('/')
def index():
    return render_template("main.html")


@app.route('/debug')
def debug():
    return render_template("report_generator.html")


@app.route('/link-request', methods=['POST'])
def response():
    link = request.form['link']
    if TextProcessor.validate_link(link):
        git_history = GitProcessor.get_history(repo_link=link, num_of_commits=INITIAL_COMMITS)
        return render_template("report_generator.html", history=git_history, repo_link=link)
    else:
        return render_template("main.html", text="Invalid Git Repository Link")


@app.route('/get_history', methods=['POST'])
def get_history():
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    link = request.form['repo_link']
    data = {
        "data": GitProcessor.get_history(repo_link=link,
                                         start_time=TimeParser.parse_time(time=start_time, param="web->git"),
                                         end_time=TimeParser.parse_time(time=end_time, param="web->git"))
    }
    return data

# Serving Static File
@app.route('/<path:path>')
def send_files(path):
    return send_from_directory('/', path)
