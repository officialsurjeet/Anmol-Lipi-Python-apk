[app]

# (str) Title of your application
title = Anmol-Lipi-Python-apk

# (str) Package name
package.name = anmol_lipi_python_apk

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py file is located
source.dir = src

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,openpyxl

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 16

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/images/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/images/icon.png

# (str) Application entry point
entrypoint = main.py

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Pattern to exclude files/folders from the application
#source.exclude_patterns = license,images/*/*.png,images/*/*.jpg
