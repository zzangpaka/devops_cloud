const { melon_data: song_array } = require("./melon_data");

Array.prototype.max = function (key_fn) {
    return this.reduce((acc, song) => {
        return key_fn(acc) < key_fn(song) ? song : acc;
    });
};

Array.prototype.min = function (key_fn) {
    return this.reduce((acc, song) => {
        return key_fn(acc) > key_fn(song) ? song : acc;
    });
};


console.log(``)
console.log(`---->>>> TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은? <<<<----`)
console.log(``)


// Array의 filter와 reduce를 활용해주세요


const top_song = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .max(song => song.like);


console.log(top_song)


const top_rank = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .min(song => song.rank);


console.log(top_rank)


// const top_song = song_array
//     .filter(({ artist }) => artist === "방탄소년단")
//     .reduce((acc, song) => {
//         return acc.like < song.like ? song : acc;
//     });


// console.log(top_song)
