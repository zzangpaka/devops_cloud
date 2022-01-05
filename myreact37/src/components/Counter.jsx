import { useState } from 'react';
import './Counter.css';

function Counter() {
  const [value, setValue] = useState(0);

  const Plus = () => {
    setValue((prevValue) => prevValue + 1);
  };

  const Minus = (e) => {
    e.preventDefault();
    setValue((prevValue) => prevValue - 1);
  };

  return (
    <div
      className="counter"
      style={{ backgroundColor: 'red' }}
      onClick={Plus}
      onContextMenu={Minus}
    >
      {value}
    </div>
  );
}

export default Counter;
