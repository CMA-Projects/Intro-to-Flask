// static/script.js
document.addEventListener('DOMContentLoaded', function() {
    const todoList = document.getElementById('todoList');
    const addForm = document.getElementById('addForm');

    addForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const newTodo = document.getElementById('todo').value;
        if (newTodo.trim() !== '') {
            addTodoToList(newTodo);
            addForm.reset();
        }
    });

    todoList.addEventListener('click', function(event) {
        const target = event.target;
        if (target.classList.contains('completeButton')) {
            completeTodoItem(target);
        } else if (target.classList.contains('removeButton')) {
            removeTodoItem(target);
        }
    });

    function addTodoToList(todoText) {
        const li = document.createElement('li');
        li.innerHTML = `
            <span class="todoText">${todoText}</span>
            <button class="completeButton">Complete</button>
            <button class="removeButton">Remove</button>
        `;
        todoList.appendChild(li);
    }

    function completeTodoItem(button) {
        const todoText = button.parentElement.querySelector('.todoText');
        todoText.classList.toggle('completed');
    }

    function removeTodoItem(button) {
        const listItem = button.parentElement;
        listItem.remove();
    }
});
