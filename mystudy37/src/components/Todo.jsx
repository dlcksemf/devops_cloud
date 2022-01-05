function Todo({ todo, onClick }) {
  return (
    <div
      className={`m-1 p-1 rounded-2xl text-lg hover:scale-105 cursor-pointer`}
      style={{ background: todo.color }}
      onClick={onClick}
    >
      <h2>{todo.content}</h2>
    </div>
  );
}

export default Todo;
