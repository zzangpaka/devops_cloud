
function makeLottoNumbers() {
    const randomNumber = [];
  
    for (let i = 0; i < 7; i++) {
      const number = Math.floor(Math.random() * 45) + 1;
      if (randomNumber.indexOf(number) === -1) {
        randomNumber.push(number);
      } else {
        i--;
      }
    }
    randomNumber.sort((a, b) => a - b);
    return randomNumber;
  }
console.log(makeLottoNumbers());



function makeLottoNumbers2() {
    const range = [...Array(45).keys()];
    const randomInt = range
    .sort(() => Math.random() - Math.random())
    .map(( number ) => number +1)
    .slice(0,7)
    .sort((a, b) => a - b)
    return randomInt;
};
console.log(makeLottoNumbers2());