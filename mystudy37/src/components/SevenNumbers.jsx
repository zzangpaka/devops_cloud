import { useState } from 'react';
import './SevenNumbers.css';

const INITIAL_VALUES = {
  numbers: [0, 0, 0, 0, 0, 0, 0],
  colors: ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple'],
};

const getNumbers = () =>
  [...Array(45).keys()]
    .map((index) => index + 1)
    .sort(() => Math.random() - Math.random())
    .slice(0, 7)
    .sort((number1, number2) => number1 - number2);

function SevenNumbers() {
  const [state, setState] = useState(INITIAL_VALUES);

  return (
    <div
      className="counter"
      style={{ backgroundColor: 'lightpink' }}
      onClick={PlusValue}
      onContextMenu={MinusValue}
    >
      {state}
    </div>
  );
}

export default SevenNumbers;
