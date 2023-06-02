from flask import Flask, render_template, request
from assembly import execute_assembly_program

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        program = request.form['program']
        instructions = program.split('\n')
        registers = execute_assembly_program(instructions)
        return render_template('index.html', registers=registers)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
