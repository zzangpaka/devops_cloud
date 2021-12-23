import { useState } from "react";

function Counter() {
  const [value, setValue] = useState(10);
  const [color, setColor] = useState("red");

  const handleClick = () => {
    console.log(`clicked`);
    setValue(value + 1);
    setColor( value % 2 === 0 ? 'green' : 'red');
  };
  return ( 
    <div style={{ 
      backgroundColor: color,
      width: 100,
      height: 100,
      display: 'inline-block',
       
      }}>
      카운터 : {value}
      <button onClick={handleClick}>증가</button>
    </div>
  );
}


function App() {
  return (
    <div>
      <h1>안녕 리액트</h1>
      <Counter />
      <Counter />
      <Counter />
    </div>
  );
}


export default App;
