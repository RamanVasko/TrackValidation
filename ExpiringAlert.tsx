import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const ExpiringAlert = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Expiring Alert Component</Text>
      <Text style={styles.subtitle}>This is a placeholder for expiring alerts</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: '#fff',
    borderRadius: 8,
    margin: 10,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  subtitle: {
    fontSize: 14,
    color: '#666',
    marginTop: 5,
  },
});

export default ExpiringAlert;