import useFieldValues from 'hooks/useFieldValues';
import { useState } from 'react';
import Todo from './Todo';
import TodoForm from './TodoForm';
import './TodoList.css';

const INITIAL_STATE = [
  { content: '2002', state: false, color: 'blue' },
  { content: '03', state: false, color: 'orange' },
  { content: '25', state: false, color: 'orange' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange, clearFieldValues] = useFieldValues({
    content: '',
    color: 'orange',
  });

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  const changeState = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.map((todo, index) => {
        if (index === todoIndex) {
          return { ...todo, state: !todo.state };
        }
        return todo;
      }),
    );
  };

  const appendTodo = () => {
    const todo = { ...fieldValues };
    setTodoList((prevTodoList) => [...prevTodoList, todo]);
    clearFieldValues();
  };

  return (
    <div className="todo-list">
      <h2>Todo List</h2>

      <TodoForm
        handleSubmit={appendTodo}
        handleChange={handleChange}
        fieldValues={fieldValues}
      />
      <hr />
      {JSON.stringify(fieldValues)}

      <button
        onClick={() => clearFieldValues()}
        className="bg-red-500 text-gray-100 cursor-pointer"
      >
        clear
      </button>

      {todoList.map((todo, index) => (
        <Todo
          todo={todo}
          changeState={() => changeState(index)}
          removeTodo={() => removeTodo(index)}
        />
      ))}
    </div>
  );
}

export default TodoList;
