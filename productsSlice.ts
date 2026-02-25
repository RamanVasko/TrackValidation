/**
 * Products Redux Slice
 */

import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';
import { API_ENDPOINTS, getAxiosConfig } from '../../config/api';

interface Product {
  id: number;
  name: string;
  category_id?: number;
  barcode?: string;
  shop_name?: string;
  purchase_date?: string;
  expiration_date: string;
  amount?: number;
  unit?: string;
  notes?: string;
  image_url?: string;
  is_active: boolean;
  days_until_expiration: number;
  is_expired: boolean;
  is_near_expiration: boolean;
  created_at: string;
  updated_at?: string;
}

interface ProductsState {
  products: Product[];
  expiringProducts: Product[];
  isLoading: boolean;
  error: string | null;
}

const initialState: ProductsState = {
  products: [],
  expiringProducts: [],
  isLoading: false,
  error: null,
};

// Async thunks
export const fetchProducts = createAsyncThunk(
  'products/fetchProducts',
  async (_, { getState, rejectWithValue }) => {
    try {
      const state = getState() as any;
      const token = state.auth.token;
      
      const response = await axios.get(API_ENDPOINTS.PRODUCTS, getAxiosConfig(token));

      return response.data;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to fetch products');
    }
  }
);

export const fetchExpiringProducts = createAsyncThunk(
  'products/fetchExpiringProducts',
  async (_, { getState, rejectWithValue }) => {
    try {
      const state = getState() as any;
      const token = state.auth.token;
      
      const response = await axios.get(API_ENDPOINTS.PRODUCTS_EXPIRING, getAxiosConfig(token));

      return response.data;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to fetch expiring products');
    }
  }
);

export const createProduct = createAsyncThunk(
  'products/createProduct',
  async (productData: FormData, { getState, rejectWithValue }) => {
    try {
      const state = getState() as any;
      const token = state.auth.token;
      
      const response = await axios.post(API_ENDPOINTS.PRODUCTS, productData, {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'multipart/form-data',
        }
      });
      
      return response.data;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to create product');
    }
  }
);

export const updateProduct = createAsyncThunk(
  'products/updateProduct',
  async ({ id, productData }: { id: number; productData: FormData }, { getState, rejectWithValue }) => {
    try {
      const state = getState() as any;
      const token = state.auth.token;
      
      const response = await axios.put(API_ENDPOINTS.PRODUCT_BY_ID(id), productData, {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'multipart/form-data',
        }
      });
      
      return response.data;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to update product');
    }
  }
);

export const deleteProduct = createAsyncThunk(
  'products/deleteProduct',
  async (productId: number, { getState, rejectWithValue }) => {
    try {
      const state = getState() as any;
      const token = state.auth.token;
      
      await axios.delete(API_ENDPOINTS.PRODUCT_BY_ID(productId), getAxiosConfig(token));

      return productId;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to delete product');
    }
  }
);

export const scanBarcode = createAsyncThunk(
  'products/scanBarcode',
  async (barcode: string, { getState, rejectWithValue }) => {
    try {
      const state = getState() as any;
      const token = state.auth.token;
      
      const response = await axios.post(
        API_ENDPOINTS.PRODUCTS + '/scan',
        { barcode },
        getAxiosConfig(token)
      );
      
      return response.data;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to scan barcode');
    }
  }
);

const productsSlice = createSlice({
  name: 'products',
  initialState,
  reducers: {
    clearError: (state) => {
      state.error = null;
    },
    clearProducts: (state) => {
      state.products = [];
      state.expiringProducts = [];
    },
  },
  extraReducers: (builder) => {
    builder
      // Fetch Products
      .addCase(fetchProducts.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchProducts.fulfilled, (state, action) => {
        state.isLoading = false;
        state.products = action.payload;
      })
      .addCase(fetchProducts.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      })
      // Fetch Expiring Products
      .addCase(fetchExpiringProducts.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchExpiringProducts.fulfilled, (state, action) => {
        state.isLoading = false;
        state.expiringProducts = action.payload;
      })
      .addCase(fetchExpiringProducts.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      })
      // Create Product
      .addCase(createProduct.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(createProduct.fulfilled, (state, action) => {
        state.isLoading = false;
        state.products.push(action.payload);
      })
      .addCase(createProduct.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      })
      // Update Product
      .addCase(updateProduct.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(updateProduct.fulfilled, (state, action) => {
        state.isLoading = false;
        const index = state.products.findIndex(p => p.id === action.payload.id);
        if (index !== -1) {
          state.products[index] = action.payload;
        }
      })
      .addCase(updateProduct.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      })
      // Delete Product
      .addCase(deleteProduct.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(deleteProduct.fulfilled, (state, action) => {
        state.isLoading = false;
        state.products = state.products.filter(p => p.id !== action.payload);
        state.expiringProducts = state.expiringProducts.filter(p => p.id !== action.payload);
      })
      .addCase(deleteProduct.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      })
      // Scan Barcode
      .addCase(scanBarcode.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(scanBarcode.fulfilled, (state, action) => {
        state.isLoading = false;
        // Handle barcode scan result
      })
      .addCase(scanBarcode.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });
  },
});

export const { clearError, clearProducts } = productsSlice.actions;
export default productsSlice.reducer;