# short-term-forecasting <!-- omit in toc -->

[![Code License: GPL v3](https://img.shields.io/badge/Code%20License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 
[![Documentation License: FDL 1.3](https://img.shields.io/badge/Documentation%20License-FDL%20v1.3-blue.svg)](https://www.gnu.org/licenses/fdl-1.3) 
[![Image license: CC BY-SA 4.0](https://img.shields.io/badge/Image%20License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Output Data License: ODbL](https://img.shields.io/badge/Output%20Data%20License-ODbL-brightgreen.svg)](https://opendatacommons.org/licenses/odbl/)

Short-term forecasting of electricity generation, demand and prices using machine learning, by Nithiya Streethran (nmstreethran@gmail.com).

This is a work-in-progress. Please feel free to suggest improvements (see the [code of conduct](/CODE_OF_CONDUCT.md) and [contributing guidelines](/CONTRIBUTING.md)). 

## Table of contents <!-- omit in toc -->
- [Folders](#folders)
- [Resources](#resources)
- [Documentation](#documentation)
- [Funding](#funding)
- [Licenses and terms of use](#licenses-and-terms-of-use)
- [Credits](#credits)

## Folders
* [data/](https://drive.google.com/drive/folders/1_3Y30j_c-4iai0WuhcrysXHYdZ4F2AKB) contains datasets (both input and output) and their terms of use (available externally on Google Drive)
* [scripts/](/scripts/) contains all Python scripts
* [jupyter-notebooks/](/jupyter-notebooks/) contains Python files in Jupyter notebook format
* [docs/](/docs/) contains the documentation ([GitHub Wiki](https://github.com/ENSYSTRA/short-term-forecasting/wiki) (Markdown) converted to other formats) 
* [images/](/images/) contains images and their license

## Resources 

The source code editor I use is [VSCodium](https://vscodium.github.io/) (fully open-source alternative to [Visual Studio Code](https://code.visualstudio.com/)), with Git integration and the following extensions:

* [Anaconda Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-python.anaconda-extension-pack)
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Visual Studio IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
* [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
* [Markdown All in One](https://marketplace.visualstudio.com/itemdetails?itemName=yzhang.markdown-all-in-one)
* [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
* [YAML](https://marketplace.visualstudio.com/itemdetails?itemName=redhat.vscode-yaml)
* [VS Code Jupyter Notebook Previewer](https://marketplace.visualstudio.com/items?itemName=jithurjacob.nbpreviewer)

Computing:
* Python version 3.6.8
* conda version 4.6.11
* git version 2.18.0.windows.1
* Processor: Intel(R) Core(TM) i5-7200U CPU @ 250 GHz 2.71 GHz
* RAM: 8 GB

My coding notes can be found in my [coding](https://github.com/nmstreethran/coding) repository.

## Documentation

Documentation is kept in the repository's [GitHub Wiki](https://github.com/ENSYSTRA/short-term-forecasting/wiki). The documentation is also imported to the [docs/](/docs/) folder and the [wiki/](/wiki/) folder as a submodule. The [docs/](/docs/) folder contains all the documentation files. The wiki documentation is converted from Markdown into the [LaTeX](/docs/docs-home.tex) and [HTML](/docs/docs.html) formats using [Pandoc](https://pandoc.org/MANUAL.html). The Pandoc commands and the command to copy wiki markdown files to [docs/](/docs/) are written in [`commands.txt`](/docs/commands.txt), which is run in Bash using:

```sh
bash docs/commands.txt
```

A [PDF](/docs/docs.pdf) version is then compiled with [`docs.tex`](/docs/docs.tex) and [`ensystra-article.sty`](/docs/ensystra-article.sty) using pdfLaTeX.

<!-- ```shell
$ pandoc -V fontsize="10pt" -V papersize="a4" -V geometry:margin="2.5cm" -V linkcolor="blue" -V urlcolor="blue" -V toccolor="blue" --metadata date="`date '+%-d %B %Y'`" --metadata author="Nithiya Streethran" --metadata title="Documentation" --toc -o docs.pdf Home.md
```  -->

## Funding

This work is part of my research as Early-Stage Researcher (ESR) 9 of the [ENSYSTRA (ENergy SYStems in TRAnsition)](https://ensystra.eu/) Innovative Training Network. ENSYSTRA is funded by the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No: 765515.

## Licenses and terms of use

Where sources have not been specified:

* Code license: [GNU General Public License Version 3](/LICENSE.md)
* Documentation license: [GNU Free Documentation License Version 1.3](/docs/License.md)
* Image license: [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](/images/LICENSE.md)
* Output data license: [ODC Open Database License (ODbL)](/data/output/LICENSE.md)

Licenses and terms of the input data used can be found in their corresponding folders within the [data](https://drive.google.com/drive/folders/1_3Y30j_c-4iai0WuhcrysXHYdZ4F2AKB) folder on Google Drive. More information is provided in the [wiki](https://github.com/ENSYSTRA/short-term-forecasting/wiki).

## Credits

Contributing guidelines: adapted from the [Open Science MOOC](https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source/blob/master/CONTRIBUTING.md)

License badges: [lukas-h/license-badges.md](https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba); made with [Shields.io](http://shields.io/)

Markdown-formatted Creative Commons licenses: [idleberg/Creative-Commons-Markdown](https://github.com/idleberg/Creative-Commons-Markdown)