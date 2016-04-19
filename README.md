# cookiecutter-alfred-workflow #

[cookiecutter][cc] template to create new [Alfred 2][alfred] workflows based on the [Alfred-Workflow][aw] **Python** library.

This is a very opinionated template to create workflows the way I like to create them. I plan to make it even more so.

## What it assumes and does ##

The template puts everyting in a subdirectory of the current working directory, giving it the name `repo_name`.

The template assumes the following:

- The "root" directory is intended to be published as a GitHub repository and may contain a copy of the compiled `.alfredworkflow` file.
- The actual workflow code is in the `src` subdirectory, *not* the root. Zipping the contents of `./src` will produce a viable `.alfredworkflow` file.
- The workflow uses Python, the [Alfred-Workflow][aw] library and [docopt][docopt].

The template does the following:

- Creates `repo_name` subdirectory of `CWD`. Within that directory:
    - `.gitignore` file with reasonable defaults for a Python project.
    - GitHub-style `README.md`.
    - `src/` subdirectory with workflow source code:
        - `info.plist` configured with workflow name and description, bundle ID, and author name.
        - Skeleton Python script `<script_name>.py` to drive a Script Filter.
        - MIT licence as `LICENCE.txt`.
        - Installs [Alfred-Workflow][aw].
        - Installs [docopt][docopt].
- Initialises `repo_name` as a `git` repository.

A newly-created workflow using the defaults looks like this (`*.pyc` files and other guff excluded):

```bash
alfred-thingumy
├── .git
│   ├── ...
├── .gitignore
├── README.md
└── src
    ├── Alfred_Workflow-1.13.dist-info
    │   ├── ...
    ├── LICENCE.txt
    ├── alfred_thingumy.py
    ├── docopt-0.6.2.dist-info
    │   ├── ...
    ├── docopt.py
    ├── info.plist
    ├── version
    └── workflow
        ├── __init__.py
        ├── background.py
        ├── update.py
        ├── version
        ├── web.py
        ├── workflow.py
```


## Installation ##

Make sure you have [cookiecutter][cc] installed. [Homebrew][homebrew] is the simplest option:

```bash
brew install cookiecutter
```

That's enough. The template is installed the first time you use it. See [below](#usage) for details.


## Usage ##

**Note**: The template puts everything **in a subdirectory of the current working directory**. The subdirectory is given the name you specify for `repo_name`.

1. Open a shell and navigate to your projects directory.
2. Run `cookiecutter gh:deanishe/cookiecutter-alfred-workflow` and answer the questions.
3. Your workflow skeleton is now at `./<repo_name>`

**Note:** You only need to use `cookiecutter gh:deanishe/cookiecutter-alfred-workflow` the first time. After that, the template will be saved locally, and you can use `cookiecutter cookiecutter-alfred-workflow`, not that it saves a whole lot of time…


### Template variables ###

**Note:** You should set your own defaults for `full_name`, `email` and `bundle_id_root`. See [Customising the defaults](#customising-the-defaults) for details.

|       Variable      |                              Meaning and usage                              |
|---------------------|-----------------------------------------------------------------------------|
| `full_name`         | Your name. Added to `info.plist`, script comments and `LICENCE.txt`         |
| `email`             | Your email address. Added to script comments and `LICENCE.txt`              |
| `bundle_id_root`    | Used in the template for `bundle_id`. Override in `~/.cookiecutterrc`       |
| `github_username`   | Used with `repo_name` to create remote/origin and `README.md` links         |
| `workflow_name`     | Added to `info.plist` and used as basis for `repo_name`                     |
| `repo_name`         | Name of the subdirectory created in `CWD`                                   |
| `bundle_id`         | Added to `info.plist`. Auto-generated from `bundle_id_root` and `repo_name` |
| `script_name`       | Name of skeleton Python script for Script Filter (without `.py` extension)  |
| `short_description` | Added to `info.plist` and `README.md`                                       |
| `date`              | Added to script comments. Defaults to today.                                |
| `year`              | Added to `LICENCE.txt` and copyright notices.                               |
| `version`           | Added to `version` file in workflow root (for `Alfred-Workflow`)            |


### Customising the defaults ###

It's conceivable that you'll want to use your own name, email address etc. when creating workflows, not mine. You can change the default answers to the template's questions (i.e. replace my name and email with your own) by creating a corresponding `~/.cookiecutterrc` file (which is in [YAML][yaml] format).

To override *this* template, your `~/.cookiecutterrc` might look like this:

```yaml
default_context:
  full_name: "Lance Uppercut"
  email: "lanceu@example.com"
  github_username: "luppercut"
  bundle_id_root: "com.example"
```

The first three options are *de facto* standards used by many templates.

`bundle_id_root` is used by the template for the workflow bundle ID: `<bundle_id_root>.<repo_name>`.

`github_username` is used with `repo_name` for the GitHub repo: `https://github.com/<github_username>/<repo_name>`.

The GitHub repo and its `README.md`, releases and issues are used as the generated workflow's help, update and feedback links respectively.

If you set these values, you should just be able to mash on ENTER, stopping only for `workflow_name` and `short_description`.

For more information on `~/.cookiecutterrc`, see [the cookiecutter User Config docs][ccrc].



[homebrew]: http://brew.sh/
[cc]: https://github.com/audreyr/cookiecutter
[ccrc]: http://cookiecutter.readthedocs.org/en/latest/advanced_usage.html#user-config-0-7-0
[alfred]: https://www.alfredapp.com/
[aw]: http://www.deanishe.net/alfred-workflow/
[docopt]: http://www.docopt.org/
[yaml]: http://yaml.org/
