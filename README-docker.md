## Create an environment using docker

If you use docker, you can use the provided Dockerfile to create an environment for the tutorial. We assume you have git installed.

0. Clone the git repository `git clone https://github.com/SwissDataScienceCenter/reproducible-data-science.git`
1. Enter the directory `cd reproducible-data-science`
2. Build the dockerfile `docker build -t r10eds -f Dockerfile.renku .`

## Use the docker environment

Execute
```bash
docker run --rm -it -p"8888:8888" -v(pwd):/r10eds r10eds jupyter lab --ip=0.0.0.0 --no-browser --allow-root --notebook-dir=/r10eds
```

Then point a browser at

```http://localhost:8888/?token=token_from_console_output```

replacing the string `token_from_console_output` with the token printed to the terminal in a line like:
```
    Or copy and paste one of these URLs:
        http://127.0.0.1:8888/?token=28a1280f57ab62049600640456be0b92f996141a6671fe21
```
