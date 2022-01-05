import './Todo.css';

function Todo({ todo, changeState, removeTodo }) {
  return (
    <>
      <div
        onClick={changeState}
        className="bg-blue-200 hover:bg-blue-400 m-1 p-1 rounded-2xl text-lg border-blue-200 border-2 hover:border-blue-500 hover:scale-105 cursor-pointer"
      >
        <span
          className="content select-none"
          style={
            todo.state ? { color: 'red', textDecoration: 'line-through' } : {}
          }
        >
          {todo.content}
        </span>
        <button onClick={removeTodo}>Delete</button>
      </div>
    </>
  );
}

export default Todo;
