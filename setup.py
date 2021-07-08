import os
import setuptools

class Clean(setuptools.Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -rf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

setuptools.setup(
    name=os.getcwd().split("/")[-1],
    packages=setuptools.find_packages(), 
    cmdclass={
        'clean': Clean,
    },
    zip_safe=False
)