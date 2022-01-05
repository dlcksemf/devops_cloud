import { useReducer } from 'react';
import './Counter.css';

const ACTION_TYPE = {
  CLICKED: 'CLICKED',
  RIGHT_CLICKED: 'RIGHT_CLICKED',
};

function reducer(prevValue, action) {
  const { type } = action;
  switch (type) {
    case ACTION_TYPE.CLICKED:
      return prevValue + 1;
    case ACTION_TYPE.RIGHT_CLICKED:
      return prevValue - 1;
    default:
      return prevValue;
  }
}

function Counter() {
  const [value, dispatch] = useReducer(reducer, 0);

  const handleMinus = () => dispatch({ type: ACTION_TYPE.RIGHT_CLICKED });

  return (
    <>
      <div
        className="Counter"
        onClick={() => dispatch({ type: ACTION_TYPE.CLICKED })}
        onContextMenu={(e) => {
          e.preventDefault();
          handleMinus();
        }}
      >
        {value}
      </div>
    </>
  );
}

export default Counter;
