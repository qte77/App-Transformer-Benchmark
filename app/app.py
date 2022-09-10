#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# %%
"""Entrypoint of the app"""

# %% [markdown]
# # BERT Benchmarking

# %% [markdown]
# ## Pre-Requisites

# %%
# ### Install modules
# TODO mount project folder or download from github
# from sys import executable, exit
# !{executable} -m pip install pipenv
# !{executable} -m pipenv install
# !{executable} -m pipenv shell
# %watermark -a qte77 -gu qte77 -ws qte77.github.io -u -i -v -iv

# %%
# ### Import modules
# TODO export into helper
from logging import basicConfig, DEBUG, debug

# from __version__ import __version__ as ver
# from helper.load_save_hf import (
#     load_and_save_model,
#     load_and_save_dataset,
#     load_and_save_tokenizer,
#     load_and_save_metrics
# )

# %%
# ###
log_level = DEBUG
log_format = '[%(levelname)s] %(asctime)s - %(process)d - %(message)s'
basicConfig(level = log_level, format = log_format)

# %% [markdown]
# ## Papermill parameters
# ### PM Start in the following code cell

# %% tags=["parameters"]

# %% [markdown]
# ### PM Parameters End


# %%
def main():
    msg = 'This is app speaking'
    print(msg)
    debug(msg)


if __name__ == "__main__":
    exit(main)
