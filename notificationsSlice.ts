import { createSlice } from '@reduxjs/toolkit';

interface NotificationState {
  notifications: any[];
  loading: boolean;
}

const initialState: NotificationState = {
  notifications: [],
  loading: false,
};

const notificationsSlice = createSlice({
  name: 'notifications',
  initialState,
  reducers: {
    setNotifications: (state, action) => {
      state.notifications = action.payload;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
  },
});

export const { setNotifications, setLoading } = notificationsSlice.actions;
export default notificationsSlice.reducer;