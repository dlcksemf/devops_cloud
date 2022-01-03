import { useState } from 'react';

// { type: "PLUS", amount: 1 }
// { type: "MINUS", amount: 1 }
function reducer(action, prevState) {
  // 순수함수로서 구현이 되어야만 합니다.
  // 같은 값의 인자가 주어지만, 항상 같은 값의 리턴을 해야만 하고
  // 인자 외에 다른 어떤 값, 어떤 통신을 해서도 안 됩니다.
  const { type, amount } = action;
  if (type === 'PLUS') {
    return prevState + amount;
  } else if (type === 'MINUS') {
    return prevState - amount;
  }
  // 버그 !!!
  return prevState;
}

function reducer_color(action) {
  const { type, color } = action;
  if (type === 'CHANGE_COLOR') {
    return color;
  }
}

function Counter2() {
  // TODO: color와 value
  const [value, setValue] = useState(0);
  const [color, setColor] = useState('red');

  const handlePlus = () => {
    const action = { type: 'PLUS', amount: 1 };
    setValue((prevValue) => {
      // dispatch 함수를 호출하여, 새로운 상탯값을 계산해냅니다.
      return reducer(action, prevValue);
    });
  };

  const handleMinus = () => {
    const action = { type: 'MINUS', amount: 1 };
    setValue((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  const handleColor = (color) => () => {
    const action = { type: 'CHANGE_COLOR', color: color };
    setColor(() => {
      return reducer_color(action);
    });
  };

  return (
    <div>
      <h2>Counter2</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>

      <hr />

      {/* <button onClick={() => setValue(value + 1)}>증가</button>
      <button onClick={() => setValue(value - 1)}>감소</button> */}

      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>

      {/* <button onClick={() => setColor("red")}>Red</button>
      <button onClick={() => setColor("green")}>Green</button>
      <button onClick={() => setColor("blue")}>Blue</button> */}

      <button onClick={handleColor('red')}>Red</button>
      <button onClick={handleColor('green')}>Green</button>
      <button onClick={handleColor('blue')}>Blue</button>
    </div>
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

export default Counter2;
