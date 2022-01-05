function TodoForm({ fieldValues, handleChange, handleSubmit }) {
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <div className="border-2 border-red-500 p-3">
      <h2 className="text-lg underline">Todo Form</h2>

      <select onChange={handleChange} name="color" value={fieldValues.color}>
        <option>amber</option>
        <option>orange</option>
        <option>yellow</option>
      </select>

      <input
        type="text"
        className="border-2 border-gray-200"
        name="content"
        onChange={handleChange}
        onKeyPress={handleKeyPress}
        value={fieldValues.content}
      />
      <button onClick={handleSubmit}>save</button>
    </div>
  );
}

export default TodoForm;
