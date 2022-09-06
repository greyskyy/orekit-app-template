# Orekit application template

This template provides the basic environment and framework for an orekit-based
application written in python.

Simply click the green *"Use this template"* button to get started, then, follow
these instructions:

1. Rename the `app_name` directory to your application name.
2. Update `pyproject.toml` by:
    1. Update the application name and description on lines 6 and 7.
    2. Update the author(s) on line 9.
    3. Update the app_name on line 31 to the new application directory value from step 1.
3. Update `environment.yaml` by:
    1. Updating the environment name on line 1.
    2. Adding any additional dependencies you know at the start.
4. Update `src/__main__.py` by:
    1. Updating the import on line 4 with the application directory name from step 1.
6. Update `src/utils/logging.py` by:
    1. Updating the logger on line 24, replacing *app_name_ with the application directory name fro step 1.
7. Delete this list and update this `readme.md` with app-specific details.
8. Write your application code in the `.apps` module. See the examples, or the section below

## Apps

A modules in the `apps` module is a python file containing functions of specific names. 

* `execute(vm=None, args:argparse.Namespace=None, config:dict=None)` - This is the application entrypoint. It takes 3 keyword parameters:
    * `vm` is the handle returned by `orekit.initVM()`, this can be used to register subthreads in the application
    * `args` the parsed command line arguments
    * `config` the parsed contents of the `config.yaml` file, if one was loaded, `None` otherwise

An additional method may optionally be specified:

* `config_args(parser)` - This method is called with the argument parser from *argparse*. Implement this method to add application-specific command line arguments.

### Subcommands / multiple apps

This framework supports multiple apps in the same application through the use of *subcommands*. Each file the `apps` module containing an `execute()` method is considered a sub-command. The file name is used as the sub-command. In this example, note there are 2 example apps provided. `example.py` and `minimal_example.py`. Unless overridden, the subcommands would be *example* and *minimal_example*.

When muliple apps are specified, the subcommand is specified on the command line, before any app-specific command line options.

```bash
python src minimal_example
```

The subcommand name can be overridden by setting the following variables in the app *.py file:

* `SUBCOMMAND` - The string name of the subcommand. Used instead of the file name.
* `ALIASES` - A list of strings which can be used as aliases for the subcommand.

Remember that subcommands only apply when multiple apps are found.

# App name

## tl;dr

Build and activate the conda environment from the `environment.yaml`

```bash
mamba env create -f environment.yaml
mamba activate orekit-application
python src --help
```

## Developers

Recreate the `environment.yaml` as follows:

```bash
mamba env export --from-history | grep -vi '^prefix:' > environment.yaml
```
