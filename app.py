from flask import Flask, redirect, render_template, url_for, request


app = Flask(__name__)
tasks = []


@app.route('/')
def tasks_page():
    return render_template('tasks.html', tasks=tasks)


@app.post('/add_task')
def add_task():
    tasks.append({"done": False, "text": request.form.get("text")})
    return redirect(url_for('tasks_page'))


@app.post('/change_task_status/<int:task_id>')
def change_task_status(task_id):
    tasks[task_id]["done"] = not tasks[task_id]["done"]
    return redirect(url_for('tasks_page'))


@app.post('/delete_task/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for('tasks_page'))
