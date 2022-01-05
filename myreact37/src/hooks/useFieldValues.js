import { useState } from 'react';

function useFieldValues(initialValues) {
  const [fieldValues, setFieldValues] = useState(initialValues);

  const clearFieldValues = () => setFieldValues(initialValues);

  const handleChange = (e) => {
    const { name, value } = e.target;

    // setter에 값 지정
    setFieldValues({
      ...fieldValues,
      [name]: value,
    });

    // setter에 함수 지정
    setFieldValues((prevFieldValues) => ({
      ...prevFieldValues,
      [name]: value,
    }));
  };

  return [fieldValues, handleChange, clearFieldValues];
}

export default useFieldValues;
