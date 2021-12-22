const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #3 좋아요수 top10을 출력 <<<<----`)
console.log(``)

// Array의 sort 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`


const like_top10 = song_array
    .sort(
        (song1, song2) => song2.like - song1.like,
    )
    .slice(0, 10);

for (const [index, { like, title, artist }] of like_top10.entries()) {
    console.log(`${index + 1} [${like}] ${title} by ${artist}`);
}
