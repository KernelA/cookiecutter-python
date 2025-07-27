ARG PYTHON_VERSION={{cookiecutter.python_min_version}}

FROM python:${PYTHON_VERSION}-buster as builder

WORKDIR /home/app

ARG PDM_CACHE=/opt/pdm/cache

ENV PDM_CACHE_DIR=${PDM_CACHE}

RUN --mount=type=cache,id=pip-cache,target=/root/.cache/pip\
    pip install -U pip wheel && \
    pip install pdm

COPY ./pyproject.toml ./pdm.lock ./

RUN --mount=type=cache,id=pip-cache,target=${PDM_CACHE} \
    pdm install --prod --no-self --frozen-lockfile

COPY ./README.md ./

COPY ./{{cookiecutter.project_slug}} ./{{cookiecutter.project_slug}}

RUN --mount=type=cache,id=pip-cache,target=${PDM_CACHE} \
    pdm install --prod --frozen-lockfile --no-editable

FROM python:${PYTHON_VERSION}-slim

ARG PROJECT_VENV_DIR=/home/app/.venv

COPY --from=builder ${PROJECT_VENV_DIR} ${PROJECT_VENV_DIR}

ENV PATH="${PROJECT_VENV_DIR}/bin:$PATH"

ENV TZ="Europe/Moscow"

WORKDIR /home/app

COPY ./main.py ./

CMD python ./main.py

