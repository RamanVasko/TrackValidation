# React Native Frontend Setup Guide

## Prerequisites

Before running the frontend, ensure you have:

1. **Node.js** (version 16 or higher)
2. **React Native development environment** set up
3. **Android Studio** (for Android development) or **Xcode** (for iOS development)

## Installation

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Configure React Native

The following configuration files have been created:
- `metro.config.js` - Metro bundler configuration
- `babel.config.js` - Babel transpilation configuration  
- `tsconfig.json` - TypeScript configuration

### 3. Link Native Modules (if needed)

For React Native 0.60+, most modules are auto-linked. If you encounter issues:

```bash
# For iOS
cd ios && pod install && cd ..

# For Android (usually not needed)
npx react-native-asset
```

## Running the Application

### Prerequisites Setup (First Time Only)

#### Android Environment
If you haven't set up the Android environment yet:

```bash
# Run the setup script (Windows PowerShell)
powershell.exe -ExecutionPolicy Bypass -File "../setup-android-env.ps1"

# Or manually set environment variables:
# ANDROID_HOME = C:\Users\<YourUsername>\AppData\Local\Android\Sdk
# Add to PATH: %ANDROID_HOME%\platform-tools
```

Verify ADB is working:
```bash
adb devices
# Should show: emulator-XXXX or your device
```

#### Start Android Emulator

1. Open Android Studio
2. Go to: **Tools → Device Manager**
3. Click the **Play (►)** button to start an emulator
4. Wait for it to fully boot (watch the logcat window)

**OR** via command line:
```bash
emulator -list-avds          # List available emulators
emulator -avd MyEmulator &   # Start an emulator
adb devices                  # Verify connection
```

### Start Metro Bundler

```bash
npm start
```

### Run on Android

```bash
npm run android
```

**Requirements for Android:**
- Android Studio installed
- Android SDK configured (ANDROID_HOME environment variable set)
- Android emulator running OR device connected via USB
- Metro dev server already running (`npm start` in another terminal)

### Run on iOS

```bash
npm run ios
```

**Prerequisites for iOS:**
- Xcode installed (macOS only)
- iOS device connected or simulator running

## Troubleshooting

### Common Issues

1. **Metro cache issues:**
   ```bash
   npx react-native start --reset-cache
   ```

2. **Node modules issues:**
   ```bash
   rm -rf node_modules
   rm package-lock.json
   npm install
   ```

3. **iOS build issues:**
   ```bash
   cd ios
   pod install --repo-update
   cd ..
   ```

4. **Android build issues:**
   - Ensure Android SDK is properly configured
   - Check `android/build.gradle` for correct Gradle version
   - Clean and rebuild:
     ```bash
     cd android
     ./gradlew clean
     cd ..
     npm run android
     ```

### Missing Dependencies

If you encounter missing dependency errors, install them individually:

```bash
# Core dependencies
npm install react react-native react-redux redux redux-thunk axios

# Navigation
npm install @react-navigation/native @react-navigation/bottom-tabs @react-navigation/stack

# UI and utilities
npm install react-native-vector-icons react-native-permissions react-native-camera

# Development tools
npm install --save-dev @types/react @types/react-native
```

## Development

### Code Structure

```
src/
├── screens/           # Main application screens
├── components/        # Reusable components
├── store/            # Redux store and slices
├── services/         # API services
└── utils/            # Utility functions
```

### Adding New Screens

1. Create new screen in `src/screens/`
2. Add navigation route in `src/navigation/`
3. Update Redux store if needed

### Adding New Components

1. Create component in `src/components/`
2. Export from `src/components/index.ts`
3. Import and use in screens

## Environment Variables

Create a `.env` file in the frontend directory for any environment-specific configuration:

```env
# API Configuration
API_BASE_URL=http://localhost:8000/api/v1

# Firebase Configuration (optional)
FIREBASE_API_KEY=your-api-key
FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
```

## Building for Production

### Android

```bash
cd android
./gradlew assembleRelease
```

### iOS

```bash
cd ios
xcodebuild -workspace YourApp.xcworkspace -scheme YourApp -configuration Release -archivePath YourApp.xcarchive archive
```

## Testing

```bash
npm test
```

## Linting

```bash
npm run lint
```

## Next Steps

1. **Start Backend First:**
   ```bash
   cd ../backend
   python install_personal.py
   uvicorn app.main:app --reload
   ```

2. **Then Start Frontend:**
   ```bash
   cd ../frontend
   npm start
   ```

3. **Access the Application:**
   - Backend API: http://localhost:8000/docs
   - Frontend: Runs on your device/simulator

## Support

If you encounter issues:
1. Check the React Native documentation
2. Review the troubleshooting section above
3. Check the backend is running on http://localhost:8000
4. Ensure your device can reach the backend server