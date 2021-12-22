const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #6 "곡명 / 단어수" 배열을 구성해주세요. <<<<----`)
console.log(``)

// Array의 map 활용
// 100줄에서 한 줄 출력의 예: `Dynamite / 1`

// 1개의 song object를 문자열로 변환


const title_array = song_array.map(
    (song) => {
        const word_count = song.title.trim().split(/\s+/).length;
        return `${song.title} / ${word_count}`;
    },
);


console.log(title_array)


// 기존 song_array 배열에서 word_count라는 컬럼을 추가

const new_song_array = song_array.map(
    (song) => {
        const word_count = song.title.trim().split(/\s+/).length;
        return {
            ...song,
            word_count: word_count,
        };
    },
);


for (const new_song of new_song_array) {
    console.log(new_song); // 기존 song + word_count 컬럼
}