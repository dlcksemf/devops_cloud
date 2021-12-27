import { useState } from "react";
const range = (size) => [...Array(size).keys()];

function makeLottoNumber() {
  const lotto = range(45)
    .sort(() => Math.random() - Math.random())
    .map((number) => number + 1)
    .slice(0, 7)
    .sort((a, b) => a - b);
  return lotto;
}

function getColor(index) {
  if (index === 0 || index === 1 || index === 6) {
    return "yellow";
  } else if (index === 2) {
    return "lightblue";
  } else if (index === 3) {
    return "red";
  } else {
    return "gray";
  }
}

function PageLotto() {
  const [lotto, setLotto] = useState([]);

  const produceNumber = () => setLotto(makeLottoNumber);

  return (
    <>
      <h2>Lotto</h2>
      <button onClick={produceNumber}>예지</button>
      <hr />
      {lotto.map((number, index) => {
        const color = getColor(index);
        return (
          <div style={{ ...style, backgroundColor: color }} key={index}>
            {number}
          </div>
        );
      })}
    </>
  );
}

const style = {
  display: "inline-block",
  margin: "1rem",
  width: "100px",
  height: "100px",
  borderRadius: "50%",
  textAlign: "center",
  lineHeight: "100px",
};

export default PageLotto;
