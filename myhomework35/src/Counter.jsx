import { useState } from "react";

function Counter({ initialValue }) {
  // 상탯값 정의
  const [value, setValue] = useState(initialValue);

  // 상탯값 변경하는 함수들
  const handleClick = () => {
    // setValue(value + 1); // 비동기 세상
    // setValue(value + 2);

    setValue((prevValue) => prevValue + 1);
    setValue((prevValue) => prevValue + 1);
    setValue((prevValue) => prevValue + 1);
  };

  // 보여지는 것들을 정의
  return (
    <div>
      <h2>Counter</h2>
      {value}
      <hr />
      <button onClick={handleClick}>+</button>
    </div>
  );
}

export default Counter;
