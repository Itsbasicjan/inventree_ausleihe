# -*- coding: utf-8 -*-

import importlib
import importlib.util
import os
import setuptools

"""This file is used to package the Ausleihfunktion plugin.

- It was generated by the InvenTree Plugin Creator tool - version 1.2.0
- Ref: https://github.com/inventree/plugin_creator
"""

"""Read the plugin version from the source code."""
module_path = os.path.join(os.path.dirname(__file__), "ausleihfunktion", "__init__.py")
spec = importlib.util.spec_from_file_location("ausleihfunktion", module_path)
ausleihfunktion = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ausleihfunktion)

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="ausleihfunktion",
    version=ausleihfunktion.PLUGIN_VERSION,
    author="Jan Schüler",
    author_email="jandeluxe96@gmail.com",
    description="A short description of the project",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        # Enter your plugin library dependencies here
    ],
    setup_requires=[
        "wheel",
        "twine",
    ],
    python_requires=">=3.9",
    entry_points={
        "inventree_plugins": [
            "Ausleihfunktion = ausleihfunktion.core:Ausleihfunktion"
        ]
    },
)
