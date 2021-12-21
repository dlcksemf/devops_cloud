const { melon_data: song_array } = require("./melon_data");


// TODO: #1 like 오름차순으로 정렬
// 출력포맷 : `[좋아요수] 곡명`
// Array의 sort 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort

console.log("--- TODO # 1 ---");

song_array.sort(
    (a, b) => (a.like - b.like)
);

for (const song of song_array) {
    console.log(`[${song.like}] ${song.title}`);
}