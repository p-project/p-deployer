P-Project Deployer
==================

The P-Project Deployer can be used to install the whole project using a single
command.

Deploy (install or update)
--------------------------

This command allows you to install or update the project in one command:

```sh
./deploy.py
```

You may pass an optional argument to clone using `https` method instead of `ssh`:

```sh
./deploy.py https
```

Run the applications
--------------------

```sh
./run.py
```

Remove all the projects
-----------------------

```sh
./clear.py
```

Configuration files
-------------------

To enable P-Deployer support for an application:

- add a `.p-properties.yml` file at project root with following content:

```yaml
dependencies:
  bin: # optional section
    - binary
    - another-binary
  script: # optional section
    - ./script-to-be-run
    - ./another-script
install:
  - install-command
  - ./script-to-be-run
run:
  - ./prepare-script
  - run-command
```

The `bin` and `script` section are checks that are run during install (checking if binaries are present on system and
scripts return a 0 exit code). The `install` section contains commands that will be run if dependencies are met. The `run`
section contains scripts that will be used to run the application.

- add your project to the `config.yml` [file at P-Deployer root](https://github.com/p-project/p-deployer/blob/master/config.yml).
