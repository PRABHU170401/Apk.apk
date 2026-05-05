[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
version = 0.1
source.include_exts = py,png,jpg,kv

# CRITICAL: These versions prevent the 'long' type error in Python 3
requirements = python3,kivy==2.3.0,pyjnius==1.6.1,cython==0.29.36

# Stable Android settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
