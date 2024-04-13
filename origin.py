import threading
import subprocess
import os
from flask import Flask, send_from_directory

app = Flask(__name__)


def run_project(project_dir):
    subprocess.run(["python", "app.py"], cwd=project_dir)


@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'origin.html')


def run_projects():
    project1_dir = os.path.join(os.getcwd(), "ml-spam", "ML-Spam-Detection")
    project2_dir = os.path.join(
        os.getcwd(), "web-vul-scanner", "Web-AI-Scanner")

    # Create threads for each project and start them
    thread1 = threading.Thread(target=run_project, args=(project1_dir,))
    thread2 = threading.Thread(target=run_project, args=(project2_dir,))

    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    projects_thread = threading.Thread(target=run_projects)
    projects_thread.start()

    # Run Flask app to serve origin.html
    app.run(debug=True)
