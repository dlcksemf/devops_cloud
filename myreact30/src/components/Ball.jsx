import React, { memo } from 'react';

const Ball = memo(({ number }) => {
  let background;
  if (number <= 10) {
    background = 'yellow';
  } else if (number <= 20) {
    background = 'skyblue';
  } else if (number <= 30) {
    background = 'red';
  } else if (number <= 40) {
    background = 'gray';
  } else {
    background = 'yellowgreen';
  }
  return (
    <div className="ball" style={{ ...style, backgroundColor: background }}>
      {number}
    </div>
  );
});

const style = {
  width: '100px',
  height: '100px',
  borderRadius: '50px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  margin: '1rem',
  userSelect: 'none',
};

export default Ball;
