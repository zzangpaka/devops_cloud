const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요? <<<<----`)
console.log(``)

// reduce, Set

const singer = song_array.map(
    (song) => (song.artist));

const popular = singer.reduce(function (allsinger, singer) {
    if (singer in allsinger) {
        allsinger[singer]++;
    }
    else {
        allsinger[singer] = 1;
    }
    return allsinger;
}, {});


console.log(popular)
