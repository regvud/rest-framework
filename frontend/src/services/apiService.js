import axios from 'axios';
import { baseURL } from '../constants/urls';

const apiService = axios.create({ baseURL });

apiService.interceptors.request.use((request) => {
  const token = localStorage.getItem('token');

  if (token) {
    request.headers.Authorization = `Bearer ${token}`;
  }

  return request;
});

export { apiService };
