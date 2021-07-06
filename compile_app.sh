#!/bin/bash

if [ "$WITHOUT_COMPILE" = true ]; then
  echo "[INFO] Use previously saved copy of application"
  cp /home/npermyakov/Downloads/app-kassa-debug.apk ./app/
else
  echo "[INFO] Use new application on build"
  cd ./project
  ./gradlew app:assembleKassa
  ls app/build/outputs/apk/kassa/debug
  mv app/build/outputs/apk/kassa/debug/app-kassa-debug.apk ../app/
fi