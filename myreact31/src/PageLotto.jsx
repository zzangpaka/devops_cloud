import { useState } from "react";

function PageLotto() {
    const Numbers = useState([10, 11, 12, 13, 14, 15, 16, 17]);
    return (
        <> 
        <h2>Lotto</h2>
        {Numbers}
        </>
    );
}



export default PageLotto;