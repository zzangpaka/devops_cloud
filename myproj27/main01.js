const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #1 like 오름차순으로 정렬 <<<<----`)
console.log(``)


song_array.sort(
    (song1, song2) => song1.like - song2.like
);

for (const { like, title } of song_array) {
    console.log(`[${like}]`, title);
}