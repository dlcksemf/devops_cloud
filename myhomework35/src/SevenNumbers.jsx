import { useReducer } from 'react';

const range = (size) => [...Array(size).keys()];

function reducer(state, action) {
  switch (action.type) {
    case 'GENERATE_NUMBERS':
      return { ...state, numbers: randomNumbers() };
    case 'SHUFFLE_NUMBERS':
      return {
        ...state,
        numbers: state.numbers.sort(() => Math.random() - Math.random()),
      };
    case 'SHUFFLE_COLORS':
      return {
        ...state,
        colors: state.colors.sort(() => Math.random() - Math.random()),
      };
    default:
      return state;
  }
}

function randomNumbers() {
  const random_numbers = range(45)
    .sort(() => Math.random() - Math.random())
    .map((number) => number + 1)
    .slice(0, 7);
  return random_numbers;
}

function SevenNumbers() {
  const [state, dispatch] = useReducer(reducer, {
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
  });

  const generateNumbers = () => {
    dispatch({ type: 'GENERATE_NUMBERS' });
  };

  const shuffleNumbers = () => {
    dispatch({ type: 'SHUFFLE_NUMBERS' });
  };

  const shuffleColors = () => {
    dispatch({ type: 'SHUFFLE_COLORS' });
  };

  return (
    <>
      <h2>Seven Numbers</h2>

      {state.numbers.map((number, index) => {
        return (
          <div
            style={{
              display: 'inline-block',
              margin: '5px',
              backgroundColor: state.colors[index],
            }}
          >
            {number}
          </div>
        );
      })}

      <hr />

      <button onClick={generateNumbers}>GENERATE NUMBERS</button>
      <button onClick={shuffleNumbers}>SHUFFLE NUMBERS</button>
      <button onClick={shuffleColors}>SHUFFLE COLORS</button>
    </>
  );
}

export default SevenNumbers;
