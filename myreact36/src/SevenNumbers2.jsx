import Circle from 'Circle';
import { useReducer } from 'react';
import { shuffle_array, zip } from 'utils';

const INITIAL_STATE = {
  numbers: [0, 0, 0, 0, 0, 0, 0],
  colors: [
    '#1B62BF',
    '#1755A6',
    '#37A647',
    '#F29F05',
    '#F23838',
    'purple',
    'pink',
  ],
};

const get_lotto_numbers = () =>
  [...Array(45).keys()]
    .map((index) => index + 1)
    .sort(() => Math.random() - Math.random())
    .slice(0, 7)
    .sort((number1, number2) => number1 - number2);

const ACTION_TYPES = {
  GENERATE_NUMBERS: 'GENERATE_NUMBERS',
  SHUFFLE_NUMBERS: 'SHUFFLE_NUMBERS',
  SHUFFLE_COLORS: 'SHUFFLE_COLORS',
};

function reducer(prevState, action) {
  const { type } = action;

  if (type === ACTION_TYPES.GENERATE_NUMBERS) {
    return {
      ...prevState,
      numbers: get_lotto_numbers(),
    };
  } else if (type === ACTION_TYPES.SHUFFLE_NUMBERS) {
    return {
      ...prevState,
      numbers: shuffle_array(prevState.numbers),
    };
  } else if (type === ACTION_TYPES.SHUFFLE_COLORS) {
    return {
      ...prevState,
      colors: shuffle_array(prevState.colors),
    };
  }

  return prevState;
}

function SevenNumbers2() {
  const [state, dispatch] = useReducer(reducer, INITIAL_STATE);

  const generateNumbers = () => {
    const action = { type: ACTION_TYPES.GENERATE_NUMBERS };
    dispatch(action);
  };

  const shuffleNumbers = () => {
    const action = { type: ACTION_TYPES.SHUFFLE_NUMBERS };
    dispatch(action);
  };

  const shuffleColors = () => {
    const action = { type: ACTION_TYPES.SHUFFLE_COLORS };
    dispatch(action);
  };

  return (
    <div>
      {zip(state.numbers, state.colors).map(([number, color]) => (
        <Circle
          number={number}
          backgroundColor={color}
          onClick={() => console.log('clicked')}
          onContextMenu={() => console.log('right clicked')}
        />
      ))}
      <hr />
      <button onClick={generateNumbers}>GENERATE_NUMBERS</button>
      <button onClick={shuffleNumbers}>SHUFFLE_NUMBERS</button>
      <button onClick={shuffleColors}>SHUFFLE_COLORS</button>
      <hr />
    </div>
  );
}

export default SevenNumbers2;
