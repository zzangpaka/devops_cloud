import { useState } from "react";

function PageLotto() {
    const [numbers, setNumbers] = useState([10, 11, 12, 13, 14, 15, 16, 17]);
    const handleClick = () => {
        console.log("clicked");
    }
    return (
        <div> 
            <h2>Lotto</h2>
            <button onClick={handleClick}>예지</button> <br /> <br />
                {numbers.map((number) => {return (<span 
                style={{margin:'1rem'}} key={number}>
                    {number} </span>);})}
        </div>
    );
}



export default PageLotto;