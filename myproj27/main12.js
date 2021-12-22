const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요? <<<<----`)
console.log(``)

// reduce, Set


const artist_count_object = song_array
    .reduce((acc, { artist }) => {
        // if(!acc[artist]) acc[artist] = 0;
        acc[artist] ||= 0;
        // i = i || 1
        // i ||= 1
        acc[artist] += 1;
        return acc;
    }, {});

const artist_count = Object.values(artist_count_object)
    .filter(number => number >= 2)
    .length;


console.log(`총 ${artist_count}팀 입니다.`)


// python version
//
// if artist not in acc:
//      acc[artist] = 0















// const singer = song_array.map(
//     (song) => (song.artist));

// const popular = singer.reduce(function (allsinger, singer) {
//     if (singer in allsinger) {
//         allsinger[singer]++;
//     }
//     else {
//         allsinger[singer] = 1;
//     }
//     return allsinger;
// }, {});


// console.log(popular)
