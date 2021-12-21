const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #10 방탄소년단의 좋아요의 총 합은? <<<<----`)
console.log(``)

// Array의 filter와 reduce를 활용해주세요.

filter_array = song_array.filter(song => song.artist === "방탄소년단");

const result = filter_array.reduce((acc, cur) => { return acc += cur.like; }, 0);


console.log(`총 합 : [${result}]`);
