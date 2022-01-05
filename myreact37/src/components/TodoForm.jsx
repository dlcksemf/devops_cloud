function TodoForm({ fieldValues, handleChange }) {
  return (
    <>
      <input
        type="text"
        className="border-2 border-gray-200"
        name="content"
        onChange={handleChange}
        value={fieldValues.content}
      />

      <select onChange={handleChange} name="color" value={fieldValues.color}>
        <option>Amber</option>
        <option>Orange</option>
        <option>Yellow</option>
      </select>
    </>
  );
}

export default TodoForm;
