import { useState } from 'react';

function useFieldValues(InitialValues) {
  const [fieldValues, setFieldValues] = useState(InitialValues);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFieldValues((prevValue) => ({ ...prevValue, [name]: value }));
  };

  const clearFieldValues = () => setFieldValues(InitialValues);

  return [fieldValues, handleChange, clearFieldValues];
}

export default useFieldValues;
