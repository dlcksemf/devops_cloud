const { question } = require("readline-sync");

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
]

let shuffled_animal_names = animal_names
  .map((value) => ({ value, sort: Math.random() }))
  .sort((a, b) => a.sort - b.sort)
  .map(({ value }) => value)

const sliced_animal_names = shuffled_animal_names.slice(0, 5);

let ok_counter = 0;

const start_time = new Date();

for (random_name of sliced_animal_names) {
    console.log(random_name);
    const line = question(">> ");

    if (line === random_name){
        ok_counter++;
        console.log("정확합니다.");
    }
    else {
        console.log("오타가 있어요.");
    }
}

const end_time = new Date();

const time = end_time.getTime() - start_time.getTime();

console.log(`${ ok_counter }번 성공하셨습니다.`);
console.log(`총 ${ time/1000 }초가 걸리셨어요.`);
