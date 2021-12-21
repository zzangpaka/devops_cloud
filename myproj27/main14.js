const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #14 방탄소년단의 곡 중에 좋아요 수가 가장 작은 곡명은? <<<<----`)
console.log(``)

// Array의 filter와 reduce를 활용해주세요.

const BTS = song_array.filter(song => song.artist === "방탄소년단")

console.log(BTS)