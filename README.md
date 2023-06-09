# Course Content

<!-- <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. -->

## Usage

### Reproducible environment for building the docker container



### Building the book

If you'd like to develop and/or build the data-science book, you should:

1. Clone this repository 
2. Launch the devcontainer via vscode dev container extension and run `poetry shell` to lauch the virtual environment `ai-book-py3.9`
3. (Optional) Edit the books source files located in the `artificial_intelligence/` directory
4. (Optional) Run `jupyter-book clean artificial_intelligence/` to remove any existing builds
5.  Run `sphinx-autobuild --host 0.0.0.0 artificial_intelligence _build/html` for interactive editing and liveview. 
6. (Optiona) Run `jupyter-book build --config artificial_intelligence/_config.yml --path-output standard artificial_intelligence` for a local build that uses the shphinx_book_theme theme.
7. (Optiona) Run `jupyter-book build --config artificial_intelligence/_config_lms.yml --path-output lms artificial_intelligence` for a local build that uses the pydata_shphinx_theme theme.


A fully-rendered HTML version of the book will be built in `artificial_intelligence/_build/html/`.

### Hosting the book

Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) to discover options for deploying a book online using services such as GitHub, GitLab, or Netlify.

For GitHub and GitLab deployment specifically, the [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) includes templates for, and information about, optional continuous integration (CI) workflow files to help easily and automatically deploy books online with GitHub or GitLab. For example, if you chose `github` for the `include_ci` cookiecutter option, your book template was created with a GitHub actions workflow file that, once pushed to GitHub, automatically renders and pushes your book to the `gh-pages` branch of your repo and hosts it on GitHub Pages when a push or pull request is made to the main branch.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/pantelis/data_mining/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).

