const { melon_data: song_array } = require("./melon_data");

// TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은?
// Array의 filter와 reduce를 활용해주세요.

console.log("--- TODO # 13 ---");

const filtered_song = song_array.filter(
    (song) => (song.artist === "방탄소년단")
).reduce(
    function (previousSong, currentSong) {
        if ( !previousSong || currentSong.like > previousSong.like) {
            return currentSong;
        }
        else {
            return previousSong;
        }
    }, null
);

console.log(filtered_song.title)
