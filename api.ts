/**
 * API Configuration
 *
 * This file handles API endpoint configuration based on the environment.
 * For Android Emulator: Uses 10.0.2.2 (special alias for host's localhost)
 * For Physical Device: Uses the actual device IP or domain
 */

import { Platform } from 'react-native';

// Default API configuration
const API_CONFIG = {
  // Android Emulator: 10.0.2.2 is a special alias that refers to the host's localhost
  // Physical Device/Real Environment: Replace with your actual backend URL
  BASE_URL: 'http://10.0.2.2:8000',
  API_VERSION: 'v1',
};

/**
 * Get the API base URL based on environment
 *
 * For Android Emulator: http://10.0.2.2:8000
 * For Physical Device: http://<YOUR_DEVICE_IP>:8000
 * For Development: http://localhost:8000
 */
export const getApiBaseUrl = (): string => {
  // You can add environment-based logic here
  // For now, use the configured base URL
  return API_CONFIG.BASE_URL;
};

/**
 * Get full API endpoint URL
 */
export const getApiEndpoint = (path: string): string => {
  const baseUrl = getApiBaseUrl();
  const version = API_CONFIG.API_VERSION;

  // Remove leading slash if present
  const cleanPath = path.startsWith('/') ? path.substring(1) : path;

  return `${baseUrl}/api/${version}/${cleanPath}`;
};

/**
 * API Endpoints
 */
export const API_ENDPOINTS = {
  // Auth endpoints
  REGISTER: getApiEndpoint('auth/register'),
  LOGIN: getApiEndpoint('auth/login'),
  LOGOUT: getApiEndpoint('auth/logout'),
  AUTH_ME: getApiEndpoint('auth/me'),

  // Products endpoints
  PRODUCTS: getApiEndpoint('products'),
  PRODUCTS_EXPIRING: getApiEndpoint('products/expiring'),
  PRODUCT_BY_ID: (id: number) => getApiEndpoint(`products/${id}`),

  // Categories endpoints
  CATEGORIES: getApiEndpoint('categories'),
  CATEGORY_BY_ID: (id: number) => getApiEndpoint(`categories/${id}`),

  // Notifications endpoints
  NOTIFICATIONS: getApiEndpoint('notifications'),
  NOTIFICATIONS_UNREAD: getApiEndpoint('notifications/unread'),
  NOTIFICATION_BY_ID: (id: number) => getApiEndpoint(`notifications/${id}`),
};

/**
 * Default axios configuration
 */
export const getAxiosConfig = (token?: string) => ({
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
    ...(token && { Authorization: `Bearer ${token}` }),
  },
});

export default API_CONFIG;

