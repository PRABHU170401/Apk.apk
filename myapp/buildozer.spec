[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
version = 0.1
source.include_exts = py,png,jpg,kv

# CRITICAL: These specific versions are required to fix the 'long' type error
requirements = python3,kivy==2.3.0,pyjnius==1.6.1,cython==0.29.36

# Recommended stable Android settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
