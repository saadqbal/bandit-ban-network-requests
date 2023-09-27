from setuptools import find_packages, setup

setup(
    name="bandit-ban-network-requests",
    version="0.0.1",
    description="Ban all network requests.",
    # url="....",
    packages=["bandit_plugins"],
    author="Asad Iqbal",
    install_requires=[
        "bandit",
    ],
    entry_points={
        "bandit.plugins": [
            "ban_network_requests = bandit_plugins.ban_network_requests:ban_network_requests"
        ],
    },
)
