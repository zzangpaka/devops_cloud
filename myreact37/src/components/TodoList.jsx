import { useState } from 'react';
import Todo from './Todo';
import './TodoList.css';
import TodoForm from './TodoForm';
import useFieldValues from 'hooks/useFieldValues';

const INITIAL_STATE = [
  { content: '2022년' },
  { content: '호랑이해' },
  { content: '멋있어' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  const [fieldValues, handleChange] = useFieldValues();

  const removeTodo = (TodoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== TodoIndex),
    );
  };

  //   const changedInputText = (e) => {
  //     setInputText(e.target.value);
  //   };

  //   const appendInputText = (e) => {
  //     console.log('e.key :', e.key);
  //     if (e.key === 'Enter') {
  //       // todoList 배열 끝에 inputText를 추가하고
  //       // inputText를 다시 비움 => value={inputText}
  //       console.log('inputText :', inputText);

  //       setTodoList((prevTodoList) => {
  //         return [...prevTodoList, { content: inputText }];
  //       });
  //       setInputText('');
  //     }
  //   };

  return (
    <div className="todo-list">
      <h2>Todo List</h2>

      <TodoForm handleChange={handleChange} />
      <hr />
      {JSON.stringify(fieldValues)}

      {/* <input
        type="text"
        value={inputText}
        onChange={changedInputText}
        onKeyPress={appendInputText}
      /> */}

      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)} key={index} />
      ))}
    </div>
  );
}

export default TodoList;
