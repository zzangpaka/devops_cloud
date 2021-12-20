const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
];

// TODO: 현재 timestamp
const start = new Date();

// TODO: shuffle 
// -- Fisher-Yates shuffle algorithm 이라는데 제대로 이해 X..어렴풋...
function shuffle(animal_names) {
    for (let i = animal_names.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        let temp = animal_names[i];
        animal_names[i] = animal_names[j];
        animal_names[j] = temp;
    }
    return animal_names;
}

// TODO: slicing
const shuffle_name = shuffle(animal_names.slice(0, 5));

// TODO: input 받기 (친구들 과제 참조...)
const { question } = require("readline-sync");

let ok_count = 0;

for (random_name of shuffle_name) {
    console.log(`>>>> ${random_name} <<<<`);
    const line = question("*--------- Answer : ");

    if (line === random_name) {
        ok_count += 1;
        console.log("");
    }
    else {
        console.log("땡!");
    }
}

const end = new Date();

const time = end.getSeconds() - start.getSeconds();

if (ok_count === 5) {
    console.log("*-- 만점 축하! --*")
} else if (ok_count === 0) {
    console.log("@@@ 엥? 빵점... @@@")
}
else {
    console.log(`${ok_count} 번 정답!`)
}
console.log(`총 입력 시간 : ${time} 초!`);
