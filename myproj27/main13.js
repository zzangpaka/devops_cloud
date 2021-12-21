const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은? <<<<----`)
console.log(``)

// Array의 filter와 reduce를 활용해주세요

const BTS = song_array.filter(song => song.artist === "방탄소년단")

console.log(BTS)