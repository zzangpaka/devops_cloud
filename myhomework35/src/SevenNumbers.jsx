import Circle from 'Circle';
import { useState } from 'react';
import { shuffle_array, zip } from 'utils';

const INITIAL_STATE = {
  numbers: [0, 0, 0, 0, 0, 0, 0],
  colors: [
    '#1B62BF',
    '#1755A6',
    '#37A647',
    '#F29F05',
    '#F23838',
    'purple',
    'pink',
  ],
};

const getNumbers = () =>
  [...Array(45).keys()]
    .map((index) => index + 1)
    .sort(() => Math.random() - Math.random())
    .slice(0, 7)
    .sort((number1, number2) => number1 - number2);

function SevenNumbers() {
  const [state, setState] = useState(INITIAL_STATE);

  const generateNumbers = () => {
    setState((prevState) => ({
      ...prevState,
      numbers: getNumbers(),
    }));
  };

  const shuffleNumbers = () => {
    setState((prevState) => ({
      ...prevState,
      numbers: shuffle_array(prevState.numbers),
    }));
  };

  const shuffleColors = () => {
    setState((prevState) => ({
      ...prevState,
      colors: shuffle_array(prevState.colors),
    }));
  };

  const changeCircleColor = (circleIndex) => {
    setState((prevState) => ({
      ...prevState,
      colors: prevState.colors.map((color, index) => {
        if (circleIndex === index) {
          return `#${Math.round(Math.random() * 0xffffff).toString(16)}`;
        } else {
          return color;
        }
      }),
    }));
  };

  const removeCircle = (circleIndex) => {
    setState((prevState) => ({
      ...prevState,
      numbers: prevState.numbers.filter((number, index) => {
        if (circleIndex === index) {
          return 0;
        } else {
          return number;
        }
      }),
      colors: prevState.colors.filter((color, index) => {
        if (circleIndex === index) {
          return null;
        } else {
          return color;
        }
      }),
    }));
  };

  return (
    <div>
      <h2>7개의 숫자</h2>
      {zip(state.numbers, state.colors).map(([number, color], index) => (
        <Circle
          key={index}
          number={number}
          backgroundColor={color}
          onClick={() => changeCircleColor(index)}
          onContext={(e) => {
            e.preventDefault();
            removeCircle(index);
          }}
        />
      ))}
      <hr />
      <button onClick={generateNumbers}>GENERATE_NUMBERS</button>
      <button onClick={shuffleNumbers}>SHUFFLE_NUMBERS</button>
      <button onClick={shuffleColors}>SHUFFLE_COLORS</button>
      <hr />
      <pre>{JSON.stringify(state, null, 4)}</pre>
    </div>
  );
}

export default SevenNumbers;
