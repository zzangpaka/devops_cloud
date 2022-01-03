import { useState } from "react";

function Counter() {
  const [state, setState] = useState({ value: 0, color: "red" });
  const { value, color } = state;

  const handlePlus = () => {
    setState((prevState) => ({
      ...prevState,
      value: prevState.value + 1,
    }));
  };
  const handleMinus = () => {
    setState((prevState) => ({
      ...prevState,
      value: prevState.value - 1,
    }));
  };

  const handleGreen = () => {
    setState((prevState) => ({
      ...prevState,
      color: "green",
    }));
  };
  const handleBlue = () => {
    setState((prevState) => ({
      ...prevState,
      color: "blue",
    }));
  };
  const handleRed = () => {
    setState((prevState) => ({
      ...prevState,
      color: "red",
    }));
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
