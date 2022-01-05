import { useState } from 'react';
import Todo from './Todo.jsx';
import TodoForm from './TodoForm.jsx';
import useFieldValues from 'hooks/useFieldValues.js';

const INITIAL_STATE = [
  { content: 'hello', color: 'Azure' },
  { content: 'my name is', color: 'FloralWhite' },
  { content: '가나다', color: 'DarkGray' },
];

const INITIAL_INPUT = {
  content: '',
  color: 'AliceBlue',
};

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange, clearFieldValues] =
    useFieldValues(INITIAL_INPUT);

  const removeTodo = (todoIndex) => {
    setTodoList(todoList.filter((_, index) => todoIndex !== index));
  };

  const appendTodo = () => {
    setTodoList((prevTodo) => [...prevTodo, { ...fieldValues }]);
    clearFieldValues();
  };

  return (
    <div className="w-1/2 m-auto">
      <TodoForm
        handleChange={handleChange}
        handleSubmit={appendTodo}
        fieldValues={fieldValues}
      />
      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)} />
      ))}
    </div>
  );
}

export default TodoList;
