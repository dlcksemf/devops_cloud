const range = (size) => [...Array(size).keys()];

function makeLottoNumber() {
  const lotto = range(45)
    // .map((number) => ({ number, random: Math.random() }))
    .sort(() => Math.random() - Math.random())
    .map((number) => number + 1)
    .slice(0, 7)
    .sort((a, b) => a - b);
  return lotto;
}

console.log(makeLottoNumber());
