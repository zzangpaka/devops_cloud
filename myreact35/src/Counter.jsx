import { useState } from "react";

function Counter() {
  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  // const handlePlus = () => {
  //   setValue(value + 1);
  // };

  // const handleMinus = () => {
  //   setValue(value - 1);
  // };

  const handlePlus = () => {
    setValue((prevValue) => prevValue + 1);
  };

  const handleMinus = () => {
    setValue((prevValue) => prevValue - 1);
  };

  // const handleGreen = () => {
  //   setColor("green");
  // };

  // const handleBlue = () => {
  //   setColor("blue");
  // };

  // const handleRed = () => {
  //   setColor("red");
  // };

  const handleGreen = () => {
    setColor(() => "green");
  };

  const handleBlue = () => {
    setColor(() => "blue");
  };

  const handleRed = () => {
    setColor(() => "red");
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
