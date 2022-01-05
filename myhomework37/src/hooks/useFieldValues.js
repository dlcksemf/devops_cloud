import { useState } from 'react';

function useFieldValues(initialValues) {
  const [fieldValues, setFieldValues] = useState(initialValues);
  return [];
}

export default useFieldValues();
