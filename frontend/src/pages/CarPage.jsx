import { Cars } from '../components/CarComponent/Cars';
import { CarForm } from '../components/CarComponent/CarForm';
import { useState } from 'react';

const CarPage = () => {
  const [refreshTrigger, setRefreshTrigger] = useState(null);
  return (
    <>
      <CarForm setRefreshTrigger={setRefreshTrigger} />
      <Cars refreshTrigger={refreshTrigger} />
    </>
  );
};

export { CarPage };
