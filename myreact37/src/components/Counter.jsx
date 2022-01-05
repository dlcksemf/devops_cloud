import { useReducer } from 'react';
import './Counter.css';

const ACTION_TYPES = {
  INCREASE: 'INCREASE',
  DECREASE: 'DECREASE',
};

function reducer(prevValue, action) {
  const { type } = action;
  switch (type) {
    case ACTION_TYPES.INCREASE:
      return prevValue + 1;
    case ACTION_TYPES.DECREASE:
      return prevValue - 1;
    default:
      return prevValue;
  }
}

function Counter() {
  const [value, dispatch] = useReducer(reducer, 0);

  return (
    <>
      <div
        className="Counter"
        onClick={() => dispatch({ type: ACTION_TYPES.INCREASE })}
        onContextMenu={(e) => {
          e.preventDefault();
          dispatch({ type: ACTION_TYPES.DECREASE });
        }}
      >
        {value}
      </div>
    </>
  );
}

export default Counter;
