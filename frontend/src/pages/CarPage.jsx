import React, { useEffect } from 'react';
import { Cars } from '../components/CarComponent/Cars';
import { carService } from '../services/carService';
import { CarForm } from '../components/CarComponent/CarForm';

const CarPage = () => {
  useEffect(() => {
    carService.getAll().then(({ data }) => console.log(data));
  }, []);

  return (
    <>
      <CarForm />
      {/* <Cars /> */}
    </>
  );
};

export { CarPage };
