
const tom = {
    name: "Tom",
    age: 10,
    region: "Daejeon",
}

// const name = tom.name;
// const age = tom["age"];

// 키명과 저장할 변수명이 같은 경우
// const { name, age } = tom;
// console.log(name, age);

const { name: otherName } = tom;
console.log(otherName);


const steve = {
    name: {
        first: "Steve",
        last: "Jobs",
    },
    age: 10,
    region: "Daejeon",
}

const { name: otherName2 } = steve;
console.log(otherName2);

const { name: { first: firstName } } = steve;
console.log(firstName);