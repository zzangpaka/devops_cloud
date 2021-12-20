// 객체 복사

const obj1 = { value1: 10 };
const obj2 = obj1; // 얕은 복사

// 깊은 복사하는 방법 중의 하나. (깊은 복사를 지원하는 js 라이브러리가 굉장히 다양히 존재함)
// 아래 방법은 가장 무식한 방법....?!

const json_string = JSON.stringify(obj1)
const obj3 = JSON.parse(json_string);


obj1.value1 += 1;

console.log(obj1);
console.log(obj2);
console.log(obj3);









// ----------------

// const obj1 = { value1: 10, "p-1": 20, };

// // 지정 속성이 없으면 undefined를 반환
// // console.log(obj1.name);

// // js에서는 함수가 아무런 값도 리턴하지 않으면 undefined를 반환
// function fn() { }
// console.log(fn());

// obj1["value1"]
// obj1.value1

// obj1["p-1"]
// obj1.p-1 => p - 1 이 된다. 이렇게는 쓸 수 없음(변수명으로 사용할 수 없는 이름일 시)