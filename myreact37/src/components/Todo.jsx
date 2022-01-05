import './Todo.css';

function Todo({ todo, changeState, removeTodo }) {
  return (
    <>
      <div
        onClick={changeState}
        className={`m-1 p-1 rounded-2xl text-lg hover:scale-105 cursor-pointer`}
        style={{ background: todo.color }}
      >
        <span
          className="content select-none"
          style={
            todo.state ? { color: 'red', textDecoration: 'line-through' } : {}
          }
        >
          {todo.color}
          {todo.content}
        </span>
        <button onClick={removeTodo}>Delete</button>
      </div>
    </>
  );
}

export default Todo;
