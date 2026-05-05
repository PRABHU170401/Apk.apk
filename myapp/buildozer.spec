[app]
title = Cone Calculator
package.name = conecalculator
package.domain = org.ken

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2