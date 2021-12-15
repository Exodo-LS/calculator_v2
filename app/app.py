"""A simple flask web app"""
# pylint: disable=(no-name-in-module)
# pylint: disable=(import-error)
from flask import Flask
from werkzeug.debug import DebuggedApplication
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.full_result_controller import FullResultController
from app.controllers.glossary_controller import GlossaryController
from app.controllers.commands_controller import CommandsController
from app.controllers.git_controller import GitController
from app.controllers.docker_controller import DockerController


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    """Get Index"""
    return IndexController.get()
@app.route("/calculator", methods=['GET'])
def calculator_get():
    """Get Calculator"""
    return CalculatorController.get()
@app.route("/calculator", methods=['POST'])
def calculator_post():
    """Post to Calculator"""
    return CalculatorController.post()
@app.route("/result", methods=['GET'])
def result_history_get():
    """Get History"""
    return FullResultController.get()
@app.route("/glossary", methods=['GET'])
def glossary_get():
    """Get Glossary"""
    return GlossaryController.get()
@app.route("/command", methods=['GET'])
def commands_get():
    """Get Commands"""
    return CommandsController.get()
@app.route("/git", methods=['GET'])
def git_get():
    """Get Git Tutorial"""
    return GitController.get()
@app.route("/docker", methods=['GET'])
def docker_get():
    """Get Docker Tutorial"""
    return DockerController.get()
