/**
 * Home Screen Component
 */

import React, { useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { useSelector, useDispatch } from 'react-redux';

// Components
import ProductCard from '../components/ProductCard';
import ExpiringAlert from '../components/ExpiringAlert';

// Selectors and Actions
import { RootState } from '../store';
import { fetchExpiringProducts } from '../store/slices/productsSlice';

const HomeScreen: React.FC = () => {
  const dispatch = useDispatch();
  const { expiringProducts, isLoading } = useSelector((state: RootState) => state.products);
  const { user } = useSelector((state: RootState) => state.auth);

  useEffect(() => {
    dispatch(fetchExpiringProducts());
  }, [dispatch]);

  const handleRefresh = () => {
    dispatch(fetchExpiringProducts());
  };

  const handleAddProduct = () => {
    // Navigate to Add Product screen
    Alert.alert('Add Product', 'Navigate to Add Product screen');
  };

  const handleViewAll = () => {
    // Navigate to Products screen
    Alert.alert('View All Products', 'Navigate to Products screen');
  };

  return (
    <ScrollView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.greeting}>
          Welcome back, {user?.username || 'User'}!
        </Text>
        <Text style={styles.subGreeting}>
          Let's keep track of your food expiration dates
        </Text>
      </View>

      {/* Quick Actions */}
      <View style={styles.quickActions}>
        <TouchableOpacity style={styles.actionButton} onPress={handleAddProduct}>
          <Text style={styles.actionText}>Add Product</Text>
        </TouchableOpacity>
        
        <TouchableOpacity style={styles.actionButton} onPress={handleViewAll}>
          <Text style={styles.actionText}>View All</Text>
        </TouchableOpacity>
      </View>

      {/* Expiring Soon Section */}
      <View style={styles.section}>
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Expiring Soon</Text>
          <TouchableOpacity onPress={handleRefresh}>
            <Text style={styles.refreshText}>Refresh</Text>
          </TouchableOpacity>
        </View>
        
        {isLoading ? (
          <Text style={styles.loadingText}>Loading...</Text>
        ) : expiringProducts.length > 0 ? (
          expiringProducts.map((product) => (
            <ExpiringAlert key={product.id} product={product} />
          ))
        ) : (
          <View style={styles.emptyState}>
            <Text style={styles.emptyStateText}>No products expiring soon!</Text>
            <Text style={styles.emptyStateSubtext}>
              Add some products to get started
            </Text>
          </View>
        )}
      </View>

      {/* Stats Section */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Quick Stats</Text>
        <View style={styles.statsContainer}>
          <View style={styles.statCard}>
            <Text style={styles.statNumber}>{expiringProducts.length}</Text>
            <Text style={styles.statLabel}>Near Expiration</Text>
          </View>
          
          <View style={styles.statCard}>
            <Text style={styles.statNumber}>
              {expiringProducts.filter(p => p.is_expired).length}
            </Text>
            <Text style={styles.statLabel}>Expired</Text>
          </View>
          
          <View style={styles.statCard}>
            <Text style={styles.statNumber}>3</Text>
            <Text style={styles.statLabel}>Notifications</Text>
          </View>
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    padding: 20,
    backgroundColor: '#fff',
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  greeting: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 4,
  },
  subGreeting: {
    fontSize: 14,
    color: '#666',
  },
  quickActions: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    padding: 20,
    backgroundColor: '#fff',
    marginVertical: 10,
  },
  actionButton: {
    backgroundColor: '#2196F3',
    paddingHorizontal: 20,
    paddingVertical: 12,
    borderRadius: 25,
    flexDirection: 'row',
    alignItems: 'center',
  },
  actionText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
    marginLeft: 8,
  },
  section: {
    backgroundColor: '#fff',
    marginHorizontal: 20,
    marginVertical: 10,
    borderRadius: 12,
    padding: 16,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 3.84,
    elevation: 5,
  },
  sectionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  loadingText: {
    textAlign: 'center',
    paddingVertical: 20,
    color: '#666',
  },
  emptyState: {
    alignItems: 'center',
    paddingVertical: 30,
  },
  emptyStateText: {
    fontSize: 16,
    color: '#666',
    marginTop: 12,
    fontWeight: '600',
  },
  emptyStateSubtext: {
    fontSize: 14,
    color: '#999',
    marginTop: 4,
  },
  statsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  statCard: {
    flex: 1,
    alignItems: 'center',
    padding: 16,
    backgroundColor: '#f8f9fa',
    borderRadius: 12,
    marginHorizontal: 4,
  },
  statNumber: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginTop: 8,
  },
  statLabel: {
    fontSize: 12,
    color: '#666',
    marginTop: 4,
    textTransform: 'uppercase',
  },
  refreshText: {
    fontSize: 14,
    color: '#2196F3',
    fontWeight: '600',
  },
});

export default HomeScreen;