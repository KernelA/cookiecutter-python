ARG PYTHON_VERSION={{cookiecutter.python_min_version}}

FROM python:${PYTHON_VERSION}-buster as builder

WORKDIR /home/app

RUN python -m venv /opt/venv

COPY ./requirements.txt ./

ENV PATH=/opt/venv/bin:${PATH}

# Add adiitional instructions
RUN --mount=type=cache,id=pip-cache,target=/root/.cache/pip pip install -r ./requirements.txt

FROM python:${PYTHON_VERSION}-slim

ENV TZ="Europe/Moscow"

COPY --from=builder /opt/venv /opt/venv

ENV PATH=/opt/venv/bin:${PATH}

WORKDIR /home/app

COPY ./main.py ./
