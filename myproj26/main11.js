const fs = require("fs");
const fsPromises = fs.Promises;

async function main() {
    try {
        const files = await fsPromises.readdir("c:/Dev");
        console.log("loaded :", files);
    }
    catch (error) {
        console.error(error);
    }
}

main();

// 2: Promise
// fsPromises.readdir("c:/Dev")
//     .then(files => console.log("loaded :", files))
//     .catch(error => console.error(error));

// 1번
// fs.readdir("c:/Dev", function (err, files) {
//     if (err) {
//         console.error(err);
//     }
//     else {
//         console.log(files);
//     }
// });

console.log("ENDED");