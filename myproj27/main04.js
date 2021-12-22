const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #4 좋아요수가 200,000 이상인 곡명만 출력하기 <<<<----`)
console.log(``)

// Array의 filter 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`


const filtered_song_array = song_array
    .filter(song => song.like >= 200_000)

for (const song of filtered_song_array) {
    console.log(`[${song.like}]`, song.title, song.artist);
}