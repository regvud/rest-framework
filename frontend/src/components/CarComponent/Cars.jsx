import React, { useEffect, useState } from 'react';
import { carService } from '../../services/carService';
import { Car } from './Car';

const Cars = () => {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    carService.getAll(({ data }) => setCars(data));
  }, []);

  return (
    <>
      {cars.map((car) => (
        <Car key={car.id} car={car} />
      ))}
    </>
  );
};

export { Cars };
