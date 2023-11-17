import React from 'react';

const Car = ({ car }) => {
  const { id, brand, price } = car;
  return (
    <div>
      <hr />
      <h1>{id}</h1>
      <h1>{brand}</h1>
      <h1>{price}</h1>
    </div>
  );
};

export { Car };
