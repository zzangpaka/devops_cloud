const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #8 곡명에 "사랑"이 포함된 곡들의 곡명 배열을 구성해주세요. <<<<----`)
console.log(``)

// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]

filter_array = song_array.filter(song => song.title.includes('사랑'));

const mapping_song = filter_array.map(
    (song) => (song.title));


console.log(mapping_song);