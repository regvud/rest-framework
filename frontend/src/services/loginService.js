import { urls } from '../constants/urls';
import { apiService } from './apiService';

const loginService = {
  async login(user) {
    const {
      data: { access },
    } = await apiService.post(urls.auth.login, user);
    localStorage.setItem('token', access);
  },
};

export { loginService };
