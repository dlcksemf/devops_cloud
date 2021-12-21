const { melon_data: song_array } = require("./melon_data");

// TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬
// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`

console.log("--- TODO # 5 ---");

const likes_sorted_songs = song_array.filter(
    (song) => (song.like >= 200000)
).sort(
    // (a, b) => ( a.title - b.title )
    function(a, b) {
        return a.title < b.title ? -1 : a.title > b.title ? 1 : 0;
    }
);

for (const song of likes_sorted_songs ) {
    console.log(`[${song.like}] ${song.title} ${song.artist}`);
}