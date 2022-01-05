import useFieldValues from 'hooks/useFieldValues';
import { useState } from 'react';
import Todo from './Todo';
import TodoForm from './TodoForm';
import './TodoList.css';

const INITIAL_STATE = [
  { content: '2002', state: false },
  { content: '03', state: false },
  { content: '25', state: false },
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

  //   const changedInputText = (e) => {
  //     setInputText(e.target.value);
  //   };

  //   const appendInputText = (e) => {
  //     if (e.key === 'Enter') {
  //       // todoList 배열 끝에 inputText를 추가합니다.
  //       // inputText를 다시 비웁니다. => input 박스 UI가 비워보이진 않을거에요. => value={inputText}
  //       setTodoList((prevValue) => [
  //         ...prevValue,
  //         { content: inputText, state: false },
  //       ]);
  //       setInputText('');
  //     }
  //   };

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

  return (
    <div className="todo-list">
      <h2>Todo List</h2>

      <TodoForm handleChange={handleChange} fieldValues={fieldValues} />
      <hr />
      {JSON.stringify(fieldValues)}

      <button
        onClick={() => clearFieldValues()}
        className="bg-red-500 text-gray-100 cursor-pointer"
      >
        clear
      </button>

      {/* <input
        type="text"
        value={inputText}
        onChange={changedInputText}
        onKeyPress={appendInputText}
      /> */}

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
