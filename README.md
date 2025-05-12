# CoverLetter-Ollama
A cover letter generator from resume using LLM locally with Ollama.
![Map](https://raw.githubusercontent.com/mfzulfikarr/CoverLetter-Ollama/refs/heads/main/img/CoverLetterLLM2.png)

### This project was inspired from <a href="https://towardsdatascience.com/from-resume-to-cover-letter-using-ai-and-llm-with-python-and-streamlit/" target="_blank">This Article</a> By Piero Paialunga

Check him out! ;)

## Table of Contents
- [Features](#features) | [Requirements](#requirements) | [Installation](#installation)
- [Getting Started](#getting-started) | [Run the Project](#run-the-project)
- [Upcoming Features](#upcoming-features-and-wip-bugfix)
- [LICENSE](#license)
## Features
1. Auto resume parser both pdf and docx.
2. Pre-formatted answers.
3. Unlimited generations and more secured privacy.
## Requirements
This program was tested using mistral 7B language model with ollama with following hardware:

1. Intel Core i7 4720HQ
2. 2GB Nvidia Geforce GTX 960m
3. 12GB of RAM
4. 1TB of drives space (Total size used was 4GB from Mistral-7B model.)

Time elapsed time for generating a cover letter is in between 5-10 minutes

To run this project, ensure to have the following installed:
### 1. Python and libraries
- **Python**: Version 3.9 or higher.
- **Python Libraries** (automatically installed via `requirements.txt`):
  - `streamlit 1.40.1 or higher`
  - `ollama`
  - `pypdf2`
  - `python-docx`

## Installation
### 1. Clone this repository
```bash
git clone https://github.com/mfzulfikarr/CoverLetter-Ollama.git
```

### 2. Use pip to automatically install the libraries:
```bash
pip install -r requirements.txt
```

## Getting Started
The resume or CV should be an ATS friendly resume in a form of text document with an extension of docx or pdf. An image converted into pdf will not work as it's not support OCR feature (yet).

### Run the project
After installing the ollama software from shell (recommended) or from an exe, install a language model from shell.
```shell
ollama pull mistral
```

Or you could also run it, it will automatically pull the model into your drive.
```shell
ollama run mistral
```

To check any locally available models, use ollama list.
```shell
ollama list
```

It is recommended to start ollama using shell.
```shell
ollama serve
```

## Upcoming Features
1. OCR to support creative or any non-ATS resume.
2. Reinforcement Learning from Human Feedback (RLHF) for regeneration.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
