const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #11 멜론 top100 리스트에 랭크된 가수는 총 몇 팀인가요? <<<<----`)
console.log(``)

// Set와 속성 .size를 활용

const mapping_song = song_array.map(
    (song) => (song.artist));

const artist_set = new Set(mapping_song);


console.log(`총 ${artist_set.size} 팀`);
