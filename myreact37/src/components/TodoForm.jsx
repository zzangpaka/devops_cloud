function TodoForm({ fieldValues, handleChange, handleSubmit }) {
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <div className="border-2 border-red-500 p-3">
      <h2 className="text-lg underline">TodoForm</h2>
      <select onChange={handleChange} name="color" value={fieldValues.color}>
        <option>LavenderBlush</option>
        <option>Azure</option>
        <option>GhostWhite</option>
        <option>Bisque</option>
        <option>RosyBrown</option>
        <option>DarkSeaGreen</option>
      </select>

      <input
        type="text"
        className="border-2 border-gray-200"
        onChange={handleChange}
        onKeyPress={handleKeyPress}
        name="content"
        value={fieldValues.content}
      />

      <button onClick={() => handleSubmit()}>저장</button>
    </div>
  );
}

export default TodoForm;
