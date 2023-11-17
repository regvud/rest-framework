import { createBrowserRouter } from 'react-router-dom';
import { MainLayout } from '../layouts/MainLayout';
import { CarPage } from '../pages/CarPage';
import { LoginPage } from '../pages/LoginPage';

const router = createBrowserRouter([
  {
    path: '',
    element: <MainLayout />,
    children: [
      {
        index: true,
        element: <LoginPage />,
      },
      {
        path: 'cars',
        element: <CarPage />,
      },
    ],
  },
]);

export { router };
