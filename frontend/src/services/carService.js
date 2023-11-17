import { urls } from '../constants/urls';
import { apiService } from './apiService';

const carService = {
  getAll: (page) =>
    apiService.get(urls.cars.base, {
      params: { page },
    }),
  postCar: async (car) => await apiService.post(urls.cars.base, car),
};

export { carService };
