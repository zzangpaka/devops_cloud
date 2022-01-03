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

function Counter2() {
  // 상탯값 정의
  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  // 상탯값 변경하는 함수들
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

  const handleGreen = () => {
    setColor((prevValue) => prevValue === "Green");
  };

  const handleBlue = () => {};

  const handleRed = () => {};

  // 보여지는 것들을 정의
  return (
    <div>
      <h2>Counter</h2>
      {value}
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
      <button onClick={handleGreen}>초록</button>
      <button onClick={handleBlue}>파랑</button>
      <button onClick={handleRed}>빨강</button>
    </div>
  );
}

export default Counter2;
