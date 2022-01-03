import Counter from "components/Counter";

function PageCounter() {
  return (
    <div>
    <h2>Counter</h2>
    <Counter initial={10} color={"red"} />
    <Counter initial={10} color={"yellow"} />
    <Counter initial={10} color={"green"} />
    </div>
  );
}

export default PageCounter;