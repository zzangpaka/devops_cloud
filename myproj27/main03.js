const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #3 좋아요수 top10을 출력 <<<<----`)
console.log(``)

// Array의 sort 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

song_array.sort(function (song1, song2) {
    return song2.like - song1.like;
});

const slice_name = song_array.slice(0, 10)

for (const song of slice_name) {
    console.log(`[${song.like}]`, song.title, song.artist);
}