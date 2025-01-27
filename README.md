# Тестовый проект по установке приложения написанного на Python Django

## Окружение:

- OS - Rocky Linux 9.5 (Blue Onyx)
- Ядро - 5.14.0-362.8.1.el9_3.x86_64
- Ansible - core 2.14.17 
- Python - 3.9.21 (дополнительно необходим модуль requests)
- Jinja - 3.1.2
- Docker - 27.5.0, build a187fa5
- Docker-compose - 1.23.2, build 1110ad01

Требуемые дополнительные коллекции ansible:
community.docker-4.3.0.info

Приложение находится по пути files/app.

Версия контейнеров nginx и postgresql:
- postgres:13-alpine
- nginx:alpine

Конфигурация ansible описана в ansible.cfg в директории проекта.

## Логирование:
Ansible - ansible.log, файл будет располагаться в директории проекта.
Docker-compose - docker_compose_logs.txt, файл будет располагаться в директории проекта.

## Запуск:
1) Необходимо заполнить файл vault-pass - пароль для доступа к зашифрованным переменным: db_name, db_name, db_password;
2) Заполнить файл инвентаря ansible по пути inventory/hosts (в тестовом окружение использовался localhost) и заменить hosts в плейбуке deploy.yaml;
3) Запустить плейбук deploy.yaml с указанием vault password файла - ansible-playbook deploy.yaml --vault-password-file vault-pass. После выполнения на сервере будет создан файл docker-compose, из которого будет развернуто приложение.

