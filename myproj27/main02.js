const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TOOD: #2 방탄소년단의 곡명만 출력 <<<<----`)
console.log(``)

// 출력포맷 : `가수명 곡명 좋아요수`
// Array의 filter 활용


const bts_song_array = song_array
    .filter(({ artist }) => artist === "방탄소년단") // (song => True, False)

for (const { like, title, artist } of bts_song_array) {
    console.log(`[${artist}] ${title} ${like}`);
}
