import { urls } from '../constants/urls';
import { apiService } from './apiService';

const carService = {
  getAll: () => apiService.get(urls.cars),
};

export { carService };
