import { useState } from "react";

function dispatch(action, prevState) {
  const { type, amount } = action;
  if (type === "PLUS") {
    return prevState + amount;
  } else if (type === "MINUS") {
    return prevState - amount;
  }
  return prevState;
}

function Counter() {
  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  // const handlePlus = () => {
  //   setValue((prevValue) => prevValue + 1);
  // };

  // const handleMinus = () => {
  //   setValue((prevValue) => prevValue - 1);
  // };

  const handlePlus = () => {
    const action = { type: "PLUS", amount: 1 };
    setValue((prevValue) => {
      return dispatch(action, prevValue);
    });
  };

  const handleMinus = () => {
    const action = { type: "MINUS", amount: 1 };
    setValue((prevValue) => {
      return dispatch(action, prevValue);
    });
  };

  return (
    <div>
      <h2>Counter</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
    </div>
  );
}

const defaultStyle = {
  width: "100px",
  height: "100px",
  borderRadius: "50px",
  lineHeight: "100px",
  textAlign: "center",
  display: "inline-block",
  fonstSize: "3rem",
  userSelect: "none",
};

export default Counter;
