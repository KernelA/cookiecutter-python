ARG PYTHON_VERSION={{cookiecutter.python_min_version}}

FROM python:${PYTHON_VERSION}-buster as builder

WORKDIR /home/app

RUN python -m venv /opt/venv

ENV PATH=/opt/venv/bin:${PATH}

RUN pip install -U pip setuptools wheel && \
    pip install pdm

# Add adiitional instructions
RUN --mount=type=cache,id=pip-cache,target=/root/.cache/pip \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=pdm.lock,target=pdm.lock \
    pdm install --prod --no-self --frozen-lockfile

RUN --mount=type=bind,source=./{{cookiecutter.project_slug}},target./{{cookiecutter.project_slug}} \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=pdm.lock,target=pdm.lock \
    pdm install --prod --frozen-lockfile --no-editable

FROM python:${PYTHON_VERSION}-slim

ENV TZ="Europe/Moscow"

COPY --from=builder /opt/venv /opt/venv

ENV PATH=/opt/venv/bin:${PATH}

WORKDIR /home/app

COPY ./main.py ./
