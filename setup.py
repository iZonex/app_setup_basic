# -*- coding: utf-8 -*-
#
# app-setup-basic app
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

from os.path import dirname, join
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


with open(join(dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(join(dirname(__file__), 'requirements-performance.txt')) as f:
    required_performance = f.read().splitlines()

with open(join(dirname(__file__), 'README.md')) as f:
    long_description = f.read()


class PyTest(TestCommand):
    user_options = []

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, '-m', 'pytest', 'tests'])
        raise SystemExit(errno)


setup(
    name='app-setup-basic',
    version='1.0.0',
    install_requires=required,
    url='https://example.com',
    license='MIT',
    author='Dmytro Chystiakov',
    author_email='dlchistyakov@gmail.com',
    packages=['app_setup_basic'],
    include_package_data=True,
    extras_require={
        'performance':  required_performance
    },
    entry_points={
        'console_scripts': [
            'app_setup_basic=app_setup_basic.__main__:main',
        ],
    },
    description='App setup basic app',
    long_description=long_description,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    tests_require=['pytest', 'pytest-aiohttp'],
    cmdclass=dict(test=PyTest)
)
