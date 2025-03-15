## Инструкция к проекту

#### Запуск проекта локально на компьютере
```
docker compose -f docker/docker-compose.local.yml --env-file=docker/local.env up --build
```

#### Запуск юнит-тестов локально на компьютере
```
uv run -m unittest discover tests/unit
```

#### Запуск e2e-тестов локально на компьютере
```
uv run pytest -m e2e
```

### Управление зависимостями

#### Инициализация пакетного менеджера uv
```
uv init
```

#### Добавить зависимость в проект
```
uv add fastapi
```

#### Добавить зависимость для разработки
```
uv add --dev pytest
```

#### Экспортировать зависимости 
```
uv export --no-hashes --no-dev> requirements.txt 
uv export --no-hashes > requirements-with-dev.txt 
```