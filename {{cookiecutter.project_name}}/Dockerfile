ARG PYTHON_VERSION={{cookiecutter.python_min_version}}

FROM python:${PYTHON_VERSION}-buster as builder

WORKDIR /home/app

RUN python -m venv /opt/venv

ENV PATH=/opt/venv/bin:${PATH}

# Add adiitional instructions
RUN --mount=type=cache,id=pip-cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements.txt,target./requirements.txt \
    pip install -r ./requirements.txt

RUN --mount=type=bind,source=./{{cookiecutter.project_slug}},target./{{cookiecutter.project_slug}} \
    --mount=type=bind,source=./setup.py,target./setup.py \
    --mount=type=bind,source=./pyproject.toml,target./pyproject.toml \
    pip install .

FROM python:${PYTHON_VERSION}-slim

ENV TZ="Europe/Moscow"

COPY --from=builder /opt/venv /opt/venv

ENV PATH=/opt/venv/bin:${PATH}

WORKDIR /home/app

COPY ./main.py ./
