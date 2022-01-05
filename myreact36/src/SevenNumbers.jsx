import Circle from 'Circle';
import { useReducer } from 'react';
import { shuffle_array, zip } from 'utils';

const INITIAL_STATE = {
  numbers: [], //[0, 0, 0, 0, 0, 0, 0],
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
  CHANGE_COLORS: 'CHANGE_COLORS',
  DELETE_CIRCLE: 'DELETE_CIRCLE',
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
  } else if (type === ACTION_TYPES.CHANGE_COLORS) {
    return {
      ...prevState,
      colors: prevState.colors.map((number, index) => {
        if (index === action.payload.index) {
          return `#${Math.round(Math.random() * 0xffffff).toString(16)}`;
        }
        return number;
      }),
    };
  } else if (type === ACTION_TYPES.DELETE_CIRCLE) {
    const filtered_list = zip(prevState.numbers, prevState.colors).filter(
      (_, index) => index !== action.payload.index,
    );
    return {
      numbers: filtered_list.map(([number]) => number),
      colors: filtered_list.map(([, color]) => color),
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

  const changeColor = (index) => {
    const action = {
      type: ACTION_TYPES.CHANGE_COLORS,
      payload: { index: index },
    };
    dispatch(action);
  };

  const removeCircle = (index) => {
    const action = {
      type: ACTION_TYPES.DELETE_CIRCLE,
      payload: { index: index },
    };
    dispatch(action);
  };

  return (
    <div>
      {zip(state.numbers, state.colors).map(
        ([number, backgroundColor], index) => (
          <Circle
            number={number}
            backgroundColor={backgroundColor}
            onClick={() => changeColor(index)}
            onContextMenu={(e) => {
              e.preventDefault();
              removeCircle(index);
            }}
          />
        ),
      )}
      <hr />
      <button onClick={generateNumbers}>GENERATE_NUMBERS</button>
      <button onClick={shuffleNumbers}>SHUFFLE_NUMBERS</button>
      <button onClick={shuffleColors}>SHUFFLE_COLORS</button>
      <hr />
    </div>
  );
}

export default SevenNumbers2;
