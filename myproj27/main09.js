const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #9 좋아요수가 200,000이상인 곡들의 곡명 리스트를 만들어보세요. <<<<----`)
console.log(``)

// Array의 filter와 map 활용

filter_array = song_array.filter(song => song.like >= 200000);

const mapping_song = filter_array.map(
    (song) => (song.title));

for (const song of mapping_song) {
    console.log(`[${song}]`);
}