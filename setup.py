from setuptools import setup
setup(
    name="TY_git_TEST",
    version='1.0.3',
    description="TY_test",
    url='https://github.com/arongi2436/TY_git_TEST.git',
    author='Taeyeoun Roh',
    author_email='tyroh@hyundai-ngv.com',
    packages=['TY_git_TEST'],
    include_package_data=True,
    package_data={
        '': ['file_test/*.xlsx'
             ]},
    zip_safe=False,
    install_requires=['pandas>=0.24.0']
)