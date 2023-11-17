import React from 'react';
import { useForm } from 'react-hook-form';
import { carService } from '../../services/carService';

const CarForm = ({ setRefreshTrigger }) => {
  const { handleSubmit, register, reset } = useForm();

  const submitForm = async (car) => {
    await carService.postCar(car);
    reset();
    setRefreshTrigger((prev) => !prev);
  };

  return (
    <>
      <form onSubmit={handleSubmit(submitForm)}>
        <input type="text" placeholder="brand" {...register('brand')} />
        <input type="text" placeholder="year" {...register('year')} />
        <input type="text" placeholder="price" {...register('price')} />
        <button>save</button>
      </form>
    </>
  );
};

export { CarForm };
