const { melon_data: song_array } = require("./melon_data");

console.log(``)
console.log(`---->>>> TODO: #11 멜론 top100 리스트에 랭크된 가수는 총 몇 팀인가요? <<<<----`)
console.log(``)

// Set와 속성 .size를 활용


const artist_array = song_array
    .map(({ artist }) => artist);

const artiest_set = new Set(artist_array);
console.log(`총 ${artiest_set.size} 팀`);


// reduce를 활용


const artist_count = song_array
    .map(({ artist }) => artist)
    .reduce((acc, artist) => {
        acc.add(artist);
        return acc;
    }, new Set())
    .size;


console.log(`총 ${artist_count} 팀`);
