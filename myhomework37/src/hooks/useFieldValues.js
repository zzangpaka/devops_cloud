import { useState } from 'react';

function useFieldValues(initialFieldValues) {
  const [fieldValues, setFieldValues] = useState(initialFieldValues);

  const clearFieldValues = () => setFieldValues(initialFieldValues);

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFieldValues({
      ...fieldValues,
      [name]: value,
    });
  };

  return [fieldValues, handleChange, clearFieldValues];
}

export default useFieldValues;