import { useState } from 'react';

const INITIAL_STATE = [
  { content: '2002' },
  { content: '03' },
  { content: '25' },
];

function TodoList() {
  const [inputText, setInputText] = useState('');
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  const changedInputText = (e) => {
    setInputText(e.target.value);
  };

  const appendInputText = (e) => {
    if (e.key === 'Enter') {
      // todoList 배열 끝에 inputText를 추가합니다.
      // inputText를 다시 비웁니다. => input 박스 UI가 비워보이진 않을거에요. => value={inputText}
      setTodoList((prevValue) => [...prevValue, { content: inputText }]);
      setInputText('');
    }
  };

  return (
    <div>
      <h2>Todo List</h2>

      <input
        type="text"
        value={inputText}
        onChange={changedInputText}
        onKeyPress={appendInputText}
      />

      <ul>
        {todoList.map((todo, index) => (
          <>
            <li>
              {todo.content}
              <button onClick={() => removeTodo(index)}>Delete</button>
            </li>
          </>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
