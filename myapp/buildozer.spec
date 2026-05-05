[app]
# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain
package.domain = org.test

# (str) Source code where the main.py lives (REQUIRED)
source.dir = .

# (str) Application versioning (REQUIRED)
version = 0.1

# (list) Source files to include
source.include_exts = py,png,jpg,kv

# (list) Application requirements
# Pinning these versions prevents the 'long' type error in Python 3
requirements = python3,kivy==2.3.0,pyjnius==1.6.1,cython==0.29.36

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Auto-accept SDK licenses
android.accept_sdk_license = True

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
