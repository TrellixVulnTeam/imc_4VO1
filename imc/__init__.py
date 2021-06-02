#! /usr/bin/env python

from __future__ import (
    annotations,
)  # fix the type annotatiton of not yet undefined classes
import os
import sys
import logging
from functools import partialmethod
from pathlib import Path as _Path

from outdated import warn_if_outdated
from joblib import Memory
import matplotlib
import matplotlib.pyplot as plt
import seaborn as _sns

try:
    # Even though there is no "imc/_version" file,
    # it should be generated by
    # setuptools_scm when building the package
    from imc._version import version

    __version__ = version
except ImportError:
    from setuptools_scm import get_version as _get_version

    version = __version__ = _get_version(root="..", relative_to=__file__)


# warn_if_outdated("imc", __version__)

plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["text.usetex"] = False


def setup_logger(name: str = "imc", level: int = logging.INFO) -> logging.Logger:
    """Setup the logger for the package."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


LOGGER = setup_logger()

# Setup joblib memory
JOBLIB_CACHE_DIR = _Path("~/.imc").expanduser()
MEMORY = Memory(location=JOBLIB_CACHE_DIR, verbose=0)

# Decorate seaborn clustermap
# _sns.clustermap = colorbar_decorator(_sns.clustermap)


_Path.mkdir = partialmethod(_Path.mkdir, exist_ok=True, parents=True)


from imc.data_models.project import Project
from imc.data_models.sample import IMCSample
from imc.data_models.roi import ROI
from imc.cli import main
