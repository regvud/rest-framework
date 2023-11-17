import React from 'react';
import { useForm } from 'react-hook-form';
import { loginService } from '../services/loginService';
import { useNavigate } from 'react-router-dom';

const LoginPage = () => {
  const { handleSubmit, register } = useForm();
  const navigate = useNavigate();

  const saveForm = async (user) => {
    await loginService.login(user);
    navigate('cars');
  };

  return (
    <>
      <form onSubmit={handleSubmit(saveForm)}>
        <input type="text" placeholder="email" {...register('email')} />
        <input
          type="password"
          placeholder="password"
          {...register('password')}
        />
        <button>login</button>
      </form>
    </>
  );
};

export { LoginPage };
