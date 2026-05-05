[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
version = 0.1
source.include_exts = py,png,jpg,kv

# CRITICAL: These versions are required to bridge the Python 2/3 gap
requirements = python3,kivy==2.3.0,pyjnius==1.6.1,cython==0.29.36

# Android-specific settings for GitHub runner stability
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
