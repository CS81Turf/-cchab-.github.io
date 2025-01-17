from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
        return jsonify({'status': 'success', 'task': task, 'tasks': tasks})
    return jsonify({'status': 'error', 'message': 'No task provided'})

@app.route('/remove_task', methods=['POST'])
def remove_task():
    task_index = int(request.form.get('task_index'))
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        return jsonify({'status': 'success', 'removed_task': removed_task, 'tasks': tasks})
    return jsonify({'status': 'error', 'message': 'Invalid task index'})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)