import { useState } from 'react';

function LottoNumber() {
  const [numberList, setNumberList] = useState([]);

  const range = [...Array(45).keys()];

  const randomInt = range
    .map((number) => ({ number, sort: Math.random() }))
    .sort((a, b) => a.sort - b.sort)
    .map(({ number }) => number + 1)
    .slice(0, 7)
    .sort((a, b) => {
      return a - b;
    });

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
