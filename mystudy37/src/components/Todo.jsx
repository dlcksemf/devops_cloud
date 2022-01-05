function Todo({ todo, onClick }) {
  return (
    <>
      <h2 onClick={onClick}>{todo.content}</h2>
    </>
  );
}

export default Todo;
