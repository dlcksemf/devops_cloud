const { melon_data: song_array } = require("./melon_data");

// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set

const countedArtist = song_array.reduce(function (allArtist, song) {
  if (song.artist in allArtist) {
    allArtist[song.artist]++
  }
  else {
    allArtist[song.artist] = 1
  }
  return allArtist
}, {});

console.log(countedArtist)

const filtered_artist = Object.values(countedArtist).filter(
  (value) => (value > 1)
);

console.log(filtered_artist.length);