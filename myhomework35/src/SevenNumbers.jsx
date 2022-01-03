import { useReducer } from 'react';

const range = (size) => [...Array(size).keys()];

function reducer(state, action) {
  switch (action.type) {
    case 'GENERATE_NUMBERS':
      return { ...state, numbers: randomNumbers() };
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

  return (
    <>
      <h2>Seven Numbers</h2>

      {state.numbers.map((number) => {
        return (
          <div style={{ display: 'inline-block', margin: '5px' }}>{number}</div>
        );
      })}

      <button onClick={generateNumbers}>GENERATE NUMBERS</button>
    </>
  );
}

export default SevenNumbers;
