import { useState } from 'react';

const INITIAL_STATE = [
  { content: '2022년' },
  { content: '호랑이해' },
  { content: '멋있어' },
];

function TodoList() {
  const [inputText, setInputText] = useState('');
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  const removeTodo = (TodoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== TodoIndex),
    );
  };

  const changedInputText = (e) => {
    setInputText(e.target.value);
  };

  const appendInputText = (e) => {
    console.log('e.key :', e.key);
    if (e.key === 'Enter') {
      // todoList 배열 끝에 inputText를 추가하고
      // inputText를 다시 비움
      console.log('inputText :', inputText);

      setTodoList((prevTodoList) => {
        return [...prevTodoList, { content: inputText }];
      });
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

      {todoList.map((todo, index) => (
        <div onClick={() => removeTodo(index)} key={index}>
          {todo.content}
        </div>
      ))}
    </div>
  );
}

export default TodoList;
