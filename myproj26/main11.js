const fs = require("fs")
const fsPromises = require("fs/promises")


// 3 : Async Await
// await는 promise 문법에 대한 축약
async function main() {
    try{
        const files = await fsPromises.readdir("c:/devops_cloud");
        console.log("loaded :", files);
    }
    catch(error) {
        console.error(error);
    }
}

main();

// 2 : Promise
// fsPromises.readdir("c:/devops_cloud33")
//     .then( files => console.log("loaded : ", files))
//     .catch(error => console.error(error));


// 1 : Callback
// fs.readdir("c:/devops_cloud", function(err, files){
//     if (err){
//         console.error(err);
//     }
//     else {
//         console.log(files);
//     }
// })

console.log("ENDED")