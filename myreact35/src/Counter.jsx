import { useState } from "react";

function reducer(action, prevState) {
  const { type, amount, color } = action;
  if (type === "PLUS") {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === "MINUS") {
    return { ...prevState, value: prevState.value - amount };
  } else if (type === "CHANGE") {
    return { ...prevState, color };
  }
  return { ...prevState };
}

function Counter() {
  const [state, setState] = useState({ value: 0, color: "red" });
  const { value, color } = state;

  const handlePlus = () => {
    const action = { type: "PLUS", amount: 1 };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };
  const handleMinus = () => {
    const action = { type: "MINUS", amount: 1 };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  const handleGreen = () => {
    const action = { type: "CHANGE", color: "green" };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };
  const handleBlue = () => {
    const action = { type: "CHANGE", color: "blue" };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };
  const handleRed = () => {
    const action = { type: "CHANGE", color: "red" };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  return (
    <div>
      <h2>Counter</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
      <button onClick={handleGreen}>초록</button>
      <button onClick={handleBlue}>파랑</button>
      <button onClick={handleRed}>빨강</button>
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
  fontSize: "3rem",
  userSelect: "none",
};

export default Counter;
