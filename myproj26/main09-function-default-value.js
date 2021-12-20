
const get_default_value = () => {
    console.log("get_default_value() 함수 호출");
    return 10;
};

// const get_default_value = () => {
//     return 10;
// };

// function get_default_value() {
//     return 10;
// }


// 디폴트 값이 필요한 시점에 함수가 호출이 됨
function hello(name, age = get_default_value()) {
    console.log(`안녕. 나는 ${name}이야. ${age}살이지.`);
}

hello("Tom", 10);
hello("Steve", 14);
hello("John", 15);

console.log(hello);