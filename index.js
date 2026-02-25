/**
 * Food Expiration Tracker - Web Entry Point
 */

import { AppRegistry } from 'react-native';
import App from './App';
import { name as appName } from './package.json';

// Register the app for web
AppRegistry.registerComponent(appName, () => App);

// For web, we need to render the app manually
if (typeof window !== 'undefined') {
  const rootTag = document.getElementById('root');
  AppRegistry.runApplication(appName, { initialProps: {}, rootTag });
}