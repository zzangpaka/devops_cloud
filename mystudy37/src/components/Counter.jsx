import { useState } from 'react';
import './Counter.css';

function Counter() {
  const [value, setvalue] = useState(0);

  const PlusValue = () => {
    setvalue((prevValue) => prevValue + 1);
  };
  const MinusValue = (e) => {
    e.preventDefault();
    setvalue((prevValue) => prevValue - 1);
  };

  return (
    <div
      className="counter"
      style={{ backgroundColor: 'lightpink' }}
      onClick={PlusValue}
      onContextMenu={MinusValue}
    >
      {value}
    </div>
  );
}

export default Counter;
