import { useReducer } from 'react';

const range = (size) => [...Array(size).keys()];

function shuffleArray(array) {
  return array.sort(() => Math.random() - Math.random());
}

function randomNumbers() {
  const random_numbers = shuffleArray(range(45))
    .map((number) => number + 1)
    .slice(0, 7);
  return random_numbers;
}

function reducer(state, action) {
  switch (action.type) {
    case 'GENERATE_NUMBERS':
      return { ...state, numbers: randomNumbers() };
    case 'SHUFFLE_NUMBERS':
      return {
        ...state,
        numbers: shuffleArray(state.numbers),
      };
    case 'SHUFFLE_COLORS':
      return {
        ...state,
        colors: shuffleArray(state.colors),
      };
    default:
      return state;
  }
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
              ...defaultStyle,
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

const defaultStyle = {
  width: '100px',
  height: '100px',
  borderRadius: '50px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  userSelect: 'none',
  margin: '1rem',
};

export default SevenNumbers;
