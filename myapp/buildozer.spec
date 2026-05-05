[app]
title = MyApp
package.name = myapp
package.domain = org.test

# (str) Source code where the main.py lives (REQUIRED)
source.dir = .

# (str) Application versioning (REQUIRED)
version = 0.1

source.include_exts = py,png,jpg,kv

requirements = python3,kivy

# (str) Custom source folders for requirements
# This is usually fine as default, but entrypoint must be handled by Buildozer
