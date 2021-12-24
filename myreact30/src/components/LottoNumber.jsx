import { useState } from 'react';
import Ball from './Ball';

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
      <button onClick={handleChange}>로또 숫자 뽑기</button>
      <hr />
      {numberList.map((number) => (
        <Ball number={number} />
      ))}
    </>
  );
}

export default LottoNumber;
