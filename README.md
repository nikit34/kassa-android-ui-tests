 Kassa ui tests
===================================================================================================


### Remote
##### docker runner
```
sudo gitlab-runner register -n --url https://gitlab.rambler.ru/ --registration-token ТОКЕН --executor docker --description "Docker Runner" --docker-image "docker:19.03.12" --docker-privileged --docker-volumes "/certs/client"
```


### Local
##### Сетап зависимостей для запуска тестов на локальной машине CI/CD.
<b>ЯП: Python3</b><br>
<b>Мобильный драйвер: Appium</b><br>
<b>Тестовый фреймворк: Pytest</b><br>
<b>Отчетность: Pytest-html</b><br>
<b>Паттерн проектирования: Page Objects</b><br>

# Необходимые пакеты для работы на андроид симуляторах:
1. Установить brew `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
2. Установить adb: `brew cask install android-platform-tools`
3. Установить Python 3.6+: `brew install python3`
4. Установить зависимости для python: `pip3 install -r requirements.txt`
5. Установить npm: `brew install npm`
6. Установить Appium server: `npm install -g appium`
7. Установить appium-doctor: `npm install -g appium-doctor` 
8. Установить Appium inspector: https://github.com/appium/appium-desktop/releases
9. Установить android-driver для appium: `npm install -g appium-uiautomator2-driver --unsafe-perm=true`
10. Установить chromedriver (Для вебвью, проверить актуальную версию драйвера - (https://chromedriver.storage.googleapis.com/index.html) / (https://sites.google.com/a/chromium.org/chromedriver/downloads)): `npm install appium --chromedriver_version="2.44"`
11. Установить android studio: https://developer.android.com/studio/ (сразу рекомендуется установить хотя бы 1 эмулятор)
12. Открыть ~/.bash_profile (если его нет - необходимо создать) и указать PATH `export PATH="/usr/local/bin:$PATH"`. 
После чего следует запустить: `appium-doctor`. В зависимости от наличия ошибок и месторасположения установленных пакетов, следует указать так же следующие локали:

`export JAVA_HOME=[путь до java_home]` (например: '/usr/bin/java' или можно так $(/usr/libexec/java_home));
<br>
`export PATH=$JAVA_HOME/bin:$PATH`;
<br>
`export ANDROID_HOME=[путь до sdk]` (например: '/Users/{user}/Library/Android/sdk');
<br>
`export PATH=~/Library/Android/sdk/platform-tools:$PATH`;
<br>
`export PATH=~/Library/Android/sdk/tools:$PATH`;
<br>
`CHROMEDRIVER_VERSION=2.44` (указать версию из пункта 9)

# Для запуска на реальном iOS устройстве:
1. Установить Carthage: `brew install carthage` (Если возникли проблемы - ` brew reinstall carthage`)
2. Установить xcode: https://developer.apple.com/xcode/
3. Установить libimobiledevice: `brew install libimobiledevice`
4. Установить ios-deploy: `brew install ios-deploy`
5. Установить ideviceinstaller: `brew install ideviceinstaller`
6. Установить драйвер: `npm install appium-xcuitest-driver`
7. Использовать подписанный сертификат .p12

Возможные проблемы:
https://github.com/libimobiledevice/ideviceinstaller/issues/48 - установка и удаление приложения.
##### Важно, чтобы после указания все путей была произведена перезагрузка терминала.

# Запуск тестов:
1. Запускаем сервер аппиум: `appium`
2. Запускам емулятор: `путь до эмулятора -avd {указать название эмулятора}` например(`/Users/{user}/Library/Android/Sdk/emulator/emulator -avd Pixel_2_API_28`)
2. Запуск тестов под android `pytest -v -s tests/Android/ --html=ui-report.html` или автономно через ci:
    * `../run.sh`

# Полезные ссылки:
1. [Appium-python documentation](https://github.com/appium/python-client)
2. [Selenium](https://selenium-python.readthedocs.io/api.html#)
3. [Pytest](https://docs.pytest.org/en/)
4. [Pytest-html](https://github.com/pytest-dev/pytest-html)
5. [appium-xcuitest-driver](https://github.com/appium/appium-xcuitest-driver/blob/master/docs/real-device-config.md)
6. [appium+real ios device](https://medium.com/@yash3x/appium-xcuitest-on-real-ios-devices-bd1ebe0dea55)
7. [page objects](https://selenium-python.readthedocs.io/page-objects.html)

