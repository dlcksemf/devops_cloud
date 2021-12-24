import { useState } from 'react';

function LottoNumber() {
  const [numberList, setNumberList] = useState([]);

  const randomInt = () => {
    let randomNumberList = [];

    for (let i = 0; i < 7; i++) {
      let num = Math.floor(Math.random() * 44) + 1;

      for (const j in randomNumberList) {
        if (num == randomNumberList[j]) {
          num = Math.floor(Math.random() * 44) + 1;
        }
      }

      randomNumberList.push(num);
    }

    randomNumberList.sort(function (a, b) {
      return a - b;
    });

    return randomNumberList;
  };

  const handleChange = () => {
    setNumberList(randomInt);
  };

  return (
    <>
      <h2>Lotto Number</h2>
      <button onClick={handleChange}>로또 숫자 뽑기</button>
      <hr />
      {numberList.map((number) => {
        return <div style={style}>{number}</div>;
      })}
    </>
  );
}
const style = {
  width: '100px',
  height: '100px',
  borderRadius: '50px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  margin: '1rem',
  userSelect: 'none',
  backgroundColor: 'red',
};

export default LottoNumber;
