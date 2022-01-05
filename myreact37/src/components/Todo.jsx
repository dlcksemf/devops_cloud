import './Todo.css';

function Todo({ todo, changeState, removeTodo }) {
  return (
    <>
      <div
        onClick={changeState}
        className={`bg-${todo.color}-200 hover:bg-${todo.color}-400 m-1 p-1 rounded-2xl text-lg border-${todo.color}-200 border-2 hover:border-${todo.color}-500 hover:scale-105 cursor-pointer`}
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
