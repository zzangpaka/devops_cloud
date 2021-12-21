const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬 <<<<----`)
console.log(``)

// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`

filter_array = song_array.filter(song => song.like >= 200000);

filter_array.sort(function (song1, song2) {
    const titleA = song1.title.toUpperCase(); // ignore upper and lowercase
    const titleB = song2.title.toUpperCase(); // ignore upper and lowercase
    if (titleA < titleB) {
        return -1;
    }
    if (titleA > titleB) {
        return 1;
    }
    if (titleA === titleB) {
        return 0;
    }
});

for (const song of filter_array) {
    console.log(`[${song.like}]`, song.title, song.artist);
}