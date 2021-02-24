import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyBrainf_ck",
    version="1.0.0",
    author="Vishwa.R",
    author_email="v.i.s.h.w.a.08.11.2001@gmail.com",
    description="A simple package which gives the brainfuck code for the passed Text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/code-reaper08/PyBrainf_ck",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='BRAINFUCK',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)