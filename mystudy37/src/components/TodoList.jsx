import { useState } from 'react';
import Todo from './Todo.jsx';
import TodoForm from './TodoForm.jsx';

const INITIAL_STATE = [
  { content: 'hello' },
  { content: 'my name is' },
  { content: '가나다' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  const deleteHandler = (todoIndex) => {
    setTodoList(todoList.filter((_, index) => todoIndex !== index));
  };

  return (
    <>
      <TodoForm />
      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => deleteHandler(index)} />
      ))}
    </>
  );
}

export default TodoList;
