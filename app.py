from flask import Flask, render_template, request, redirect, url_for

# Create a flask application instance
app = Flask(__name__)

# Initialize an empty list
todos = []

# This is a decorator that associates the following function with the root URL ('/'). When a user accesses the root URL, the index function will be called.
@app.route('/')

# This function renders the 'index.html' template using render_template. It passes the todos list to the template, allowing dynamic content generation.
def index():
    return render_template('index.html', todos=todos)

# This decorator associates the following function with the '/add' URL and specifies that it should only handle POST requests.
@app.route('/add', methods=['POST'])

# This function handles the addition of a new to-do item. It retrieves the new to-do item from the submitted form data using request.form.get('todo'). 
# If the new to-do item is not empty, it is appended to the todos list. Finally, the function redirects the user back to the 'index' route using redirect(url_for('index')).
def add_todo():
    new_todo = request.form.get('todo')
    if new_todo:
        todos.append(new_todo)
    return redirect(url_for('index'))

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')


# This conditional statement ensures that the Flask app is only run when the script is executed directly (not when imported as a module). 
# If the script is the main program, it calls app.run(debug=True) to start the development server with debugging enabled.
if __name__ == '__main__':
    app.run(debug=True)
