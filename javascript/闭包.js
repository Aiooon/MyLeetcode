let Todo = (function createTodoFactory() {
    let todoPrototype = {
        toString: function () {
            return this.id + " " + this.userName + ": " + this.title;
        }
    }
    return function (todo) {
        let newTodo = Object.create(todoPrototype);
        Object.assign(newTodo, todo);
        return newTodo;
    }
})();
let todo = Todo({ id: 1, title: "This is a title", userName: "Cristi", completed: false });

todo.toString();