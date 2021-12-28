import Lotto from "components/Lotto";
import { useState } from "react/cjs/react.development";

function PageLotto() {

    const [number, setnumber] = useState([]);

    const handleClick = () => {
        setnumber(number);
      };

    return (
        <div>
            <button onClick={handleClick}>
                Pick Up!
            </button>
            <h2>Lotto</h2>
                <Lotto color={"yellow"} border={"1px solid yellow"} />
                <Lotto color={"yellow"} border={"1px solid yellow"} />
                <Lotto color={"yellow"} border={"1px solid yellow"} />
                <Lotto color={"red"} border={"1px solid red"} />
                <Lotto color={"red"} border={"1px solid red"} />
                <Lotto color={"grey"} border={"1px solid grey"} />
        </div>
    );
}

export default PageLotto;