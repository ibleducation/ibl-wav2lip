from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = list(set(f.readlines()))
setup(
    name="Wav2Lip",
    version="0.0.1",
    description="A lip sync generation library",
    url="https://github.com/Joetib/Wav2lip",
    author="IBL",
    author_email="na",
    license="BSD License.",
    include_package_data=True,
    packages=find_packages(),
    install_requires=requirements,
    zip_safe=False,
)
