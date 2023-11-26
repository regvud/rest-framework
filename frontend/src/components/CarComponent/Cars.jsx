import React, { useEffect, useState } from 'react';
import { carService } from '../../services/carService';
import { Car } from './Car';
import { useSearchParams } from 'react-router-dom';

const Cars = ({ refreshTrigger }) => {
  const [cars, setCars] = useState([]);
  const [params, setParams] = useSearchParams();
  const page = params.get('page');

  useEffect(() => {
    carService.getAll(page).then(({ data }) => setCars(data.data));
  }, [refreshTrigger]);
  console.log();
  return (
    <>
      {cars?.map((car) => (
        <Car key={car.id} car={car} />
      ))}
    </>
  );
};

export { Cars };
