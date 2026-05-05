[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
version = 0.1

# CRITICAL: Use these exact versions to fix the 'long' builtin error
requirements = python3,kivy==2.3.0,pyjnius==1.6.1,cython==0.29.36

# Android-specific settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
