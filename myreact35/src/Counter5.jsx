import { useState } from 'react';

// function reducer(action, prevState) {
//   const { type, amount } = action;

//   if (type === 'PLUS') {
//     return prevState + amount;
//   } else if (type === 'MINUS') {
//     return prevState - amount;
//   }
//   return prevState;
// }

function reducer(action, prevState) {
  const { type, amount, color } = action;
  if (type === 'PLUS') {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === 'MINUS') {
    return { ...prevState, value: prevState.value - amount };
  } else if (type === 'CHANGE_COLOR') {
    return { ...prevState, color };
  }
  return prevState;
}

function Counter5() {
  const [state, setState] = useState({
    value: 0,
    color: 'red',
  });

  const handlePlus = () => {
    const action = { type: 'PLUS', amount: 1 };
    setState((prevState) => reducer(action, prevState));
  };

  const handleMinus = () => {
    const action = { type: 'MINUS', amount: 1 };
    setState((prevState) => reducer(action, prevState));
  };

  const handleColor = (color) => {
    const action = { type: 'CHANGE_COLOR', color: color };
    setState((prevState) => reducer(action, prevState));
  };

  return (
    <>
      <h2>Counter5</h2>

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

export default Counter5;
