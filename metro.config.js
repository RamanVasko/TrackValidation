/**
 * Metro configuration for React Native
 * https://github.com/facebook/react-native
 *
 * @format
 */

const { getDefaultConfig, mergeConfig } = require('@react-native/metro-config');

const config = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
        inlineRequires: true,
      },
    }),
  },
  resolver: {
    sourceExts: ['jsx', 'js', 'ts', 'tsx', 'web.tsx', 'web.ts', 'web.jsx', 'web.js'],
    assetExts: ['png', 'jpg', 'jpeg', 'gif', 'svg', 'ico'],
  },
  serializer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
        inlineRequires: true,
      },
    }),
  },
};

// Add web-specific configuration
if (process.env.RN_PLATFORM === 'web') {
  config.resolver.sourceExts.push('web.js', 'web.ts', 'web.jsx', 'web.tsx');
  config.transformer.babelTransformerPath = require.resolve('react-native-web/dist/transformer');
}

module.exports = mergeConfig(getDefaultConfig(__dirname), config);
