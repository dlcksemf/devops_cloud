import { useState } from 'react';

function Counter3() {
  const [value, setValue] = useState(0);
  const [color, setColor] = useState('red');

  const handlePlus = () => {
    setValue((prevValue) => prevValue + 1);
  };

  const handleMinus = () => {
    setValue((prevValue) => prevValue - 1);
  };

  const handleGreen = () => {
    setColor(() => 'green');
  };

  const handleRed = () => {
    setColor(() => 'red');
  };

  const handleBlue = () => {
    setColor(() => 'blue');
  };

  return (
    <>
      <h2>Counter3</h2>

      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>

      <hr />

      {/* <button onClick={() => setValue(value + 1)}>Plus</button>
      <button onClick={() => setValue(value - 1)}>Minus</button> */}

      <button onClick={handlePlus}>Plus</button>
      <button onClick={handleMinus}>Minus</button>

      {/* <button onClick={() => setColor('red')}>Red</button>
      <button onClick={() => setColor('green')}>Green</button>
      <button onClick={() => setColor('blue')}>Blue</button> */}

      <button onClick={handleRed}>Red</button>
      <button onClick={handleGreen}>Green</button>
      <button onClick={handleBlue}>Blue</button>
    </>
  );
}

const defaultStyle = {
  width: '100px',
  height: '100px',
  borderRadius: '50px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  userSelect: 'none',
};

export default Counter3;
