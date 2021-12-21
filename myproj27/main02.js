const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TOOD: #2 방탄소년단의 곡명만 출력 <<<<----`)
console.log(``)

// 출력포맷 : `가수명 곡명 좋아요수`
// Array의 filter 활용

filter_array = song_array.filter(song => song.artist === "방탄소년단");

filter_array.sort(function (song1, song2) {
    return song1.like - song2.like;
});

for (const song of filter_array) {
    console.log(`[${song.artist}]`, song.title, song.like);
}