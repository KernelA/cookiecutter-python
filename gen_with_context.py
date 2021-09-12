import json
import os
import argparse

from cookiecutter.main import cookiecutter

def load_json(path_to_file) -> dict:
    with open(path_to_file, "rb") as jfile:
        context = json.load(jfile)
    return context

def context_var_from_env_var(env_name: str) -> str:
    var_name = env_name.split("_")[2:]
    return "_".join(var_name).lower()

def extend_context_form_env(env_prefix: str = "COOKIECUTTER_CONTEXT") -> dict:
    extended_context = dict()

    for env_name  in os.environ.keys():
        if env_name.startswith(env_prefix):
            context_name = context_var_from_env_var(env_name)
            context_value = os.environ[env_name]
            extended_context[context_name] = context_value

    return extended_context


def main(args):
    context = load_json("cookiecutter.json")
    extended_context = extend_context_form_env(args.env_prefix)
    context.update(extended_context)
    print(context)
    cookiecutter(".", extra_context=context, no_input=True, output_dir=args.out_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_dir", type=str, required=True)
    parser.add_argument("--env_prefix", type=str, default="COOKIECUTTER_CONTEXT")

    args = parser.parse_args()

    main(args)


