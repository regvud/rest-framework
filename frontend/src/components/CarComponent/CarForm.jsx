import React from 'react';
import { useForm } from 'react-hook-form';

const CarForm = () => {
    const { handleSubmit, register, reset } = useForm();
    
  return (
    <div>
      <h1>CarForm</h1>
    </div>
  );
};

export { CarForm };
