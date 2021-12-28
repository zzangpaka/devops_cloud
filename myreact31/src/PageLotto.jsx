import { useState } from "react";

function PageLotto() {
    const [numbers, setNumbers] = useState([10, 11, 12, 13, 14, 15, 16, 17]);
    return (
        <div> 
            <h2>Lotto</h2>
                {numbers.map((number) => {return (<span 
                style={{margin:'1rem'}}>
                    {number} </span>);})}
        </div>
    );
}



export default PageLotto;