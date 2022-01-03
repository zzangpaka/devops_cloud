function Lotto({color, border}) {

    const randomLottoArray = [(min, max)]
        min = Math.ceil(1);
        max = Math.floor(45);
        return Math.floor(Math.random() * (max - min +1)) + min
        .sort(
            (number1, number2) => number1 - number2
        )
        .slice(0, 6)
    const myLottoSet = new Set(myLottoArray);
    

    return <div
        style={{ ...style, backgroundColor: color, border }}>
        {myLottoSet}
        </div>
};

const style = {
    width: "100px",
    height: "100px",
    borderRadius: "50px",
    lineHeight: "100px",
    textAlign: "center",
    display: "inline-block",
    fontSize: "3rem",
    margin: "1rem",
    userSelect: "none",
};

export default Lotto;