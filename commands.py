"""Снабди каждый комментарий правильной командой."""

python3 -V  # команда для проверки текущей версии Питона
python3 # запуск интерпретатора Питона в режиме REPL
pip3 install --user virtualenv # создание виртуального окружения в текущей директории
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 & source ~/.local/bin/virtualenvwrapper.sh paste >> ~/.bashrc  # активация вышесозданного виртуального окружения
rmvirtualenv env-name # деактивация виртуального окружения
python3 ./run.py # запуск скрипта run.py находящегося в текущей директории
pip3 install requests # установка пакета reqgituests через пакетный менеджер pip
