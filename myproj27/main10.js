const { melon_data: song_array } = require("./melon_data");

Array.prototype.sum = function () {
    return this.reduce((acc, element) => {
        return acc + element;
    }, 0);
};


console.log(``)
console.log(`---->>>> TODO: #10 방탄소년단의 좋아요의 총 합은? <<<<----`)
console.log(``)

// Array의 filter와 reduce를 활용해주세요.


const bts_result = song_array
    .filter(
        ({ artist }) => artist === "방탄소년단"
    )
    // .reduce((acc, { like }) => acc + like, 0);
    .map(({ like }) => like)
    .sum();


console.log("총 합 :", `[${bts_result}]`)
