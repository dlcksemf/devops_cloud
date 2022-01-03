import { useState } from 'react';

function Counter4() {
  const [state, setState] = useState({
    value: 0,
    color: 'red',
  });

  const handlePlus = () => {
    setState((prevValue) => ({ ...prevValue, value: prevValue.value + 1 }));
  };

  const handleMinus = () => {
    setState((prevValue) => {
      return { ...prevValue, value: prevValue.value - 1 };
    });
  };

  const handleColor = (color) => {
    setState((prevValue) => {
      return { ...prevValue, color };
    });
  };

  return (
    <>
      <h2>Counter4</h2>

      <div style={{ ...defaultStyle, backgroundColor: state.color }}>
        {state.value}
      </div>

      <hr />

      <button onClick={handlePlus}>Plus</button>
      <button onClick={handleMinus}>Minus</button>

      <button onClick={() => handleColor('red')}>Red</button>
      <button onClick={() => handleColor('green')}>Green</button>
      <button onClick={() => handleColor('blue')}>Blue</button>
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

export default Counter4;
