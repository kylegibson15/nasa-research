# Nasa Research

## Getting Started

### 1. Install Docker Engine
> depending on your host OS there may be different way to installing Docker Engine. Please see the Docker [documentation](https://docs.docker.com/engine/install/) to install.

### 2. Check your Docker installation
```shell
docker --version
# output example: Docker version 24.0.6, build ed223bc
```

### 3. Check Docker Compose is installed
> __Note:__ If you installed the Docker Desktop, Docker Compose should be installed by default.
> If command below fails, please see the Docker Compose [documentation](https://docs.docker.com/compose/install/) to install
```shell
docker compose images --help
# example output: 
# Usage:  docker compose images [OPTIONS] [SERVICE...]
#
# List images used by the created containers
#
# Options:
#      --dry-run         Execute command in dry run mode
#      --format string   Format the output. Values: [table | json]. (default "table")
#  -q, --quiet           Only display IDs
```

### 4. Run Docker Compose on the Project
> It's important to include the `--build` flag
```shell
docker compose up --build
```

### 5. Swagger API Docs
Swagger API Docs can be found at `http://localhost:8000/docs`

### 6. Initialize the Database
- Run the `POST /init` endpoint from the Swagger UI. This will initialize the database by dropping all tables and then creating all tables.

or by using cURL

```shell
curl -X 'POST' \
    'http://localhost:8000/init' \
    -H 'accept: application/json' \
    -d ''
```

### 7. Collect NASA Lunar Mission Data
- Run the `POST /collect-lunar-samples` endpoint from the Swagger UI. This will ingest data from the NASA Lunar Samples API.

or 

```shell
curl -X 'POST' \
    'http://localhost:8000/collect-lunar-samples' \
    -H 'accept: application/json' \
    -d ''
```

### Other Available APIs
- `GET /missions`
- `GET /samples`
- `GET /stations`
