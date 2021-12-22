const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #9 좋아요수가 200,000이상인 곡들의 곡명 리스트를 만들어보세요. <<<<----`)
console.log(``)

// Array의 filter와 map 활용


const like_song = song_array
    .filter(
        ({ like }) => like >= 200_000
    )
    .map(
        ({ title }) => title
    );


console.log(like_song)
