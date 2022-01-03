import { useState } from "react";

const range = (size) => [...Array(size).keys()];

function makeLottoNumbers() {
  const randomInt = range(45)
    .sort(() => Math.random() - Math.random())
    .map((number) => number + 1)
    .slice(0, 7)
    .sort((a, b) => a - b);
  return randomInt;
}

function PageLotto() {
  const [numbers, setNumbers] = useState([10, 11, 12, 13, 14, 15, 16, 17]);
  const handleClick = () => {
    setNumbers(makeLottoNumbers());
  };
  return (
    <div>
      <h2>Lotto</h2>
      <button onClick={handleClick}>예지</button> <br /> <br />
      {numbers.map((number) => {
        return (
          <span style={{ margin: "1rem" }} key={number}>
            {number}{" "}
          </span>
        );
      })}
    </div>
  );
}

export default PageLotto;
