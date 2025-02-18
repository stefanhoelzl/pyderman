from setuptools import setup, find_packages


def readme(file='', split=False):
	with open(file) as f:
		if split:
			return f.readlines()
		else:
			return f.read()


setup(
	name='pyderman',
	version='2.0.2',
	description='Installs the latest Chrome/Firefox/Opera/PhantomJS/Edge web drivers automatically.',
	long_description=readme('README.md'),
	long_description_content_type='text/markdown',
	url='http://github.com/shadowmoose/pyderman',
	author='ShadowMoose',
	author_email='shadowmoose@github.com',
	license='MIT',
	packages=find_packages(),
	install_requires=[],  # readme('requirements.txt', split=True),
	zip_safe=False
)

# python setup.py sdist;twine upload dist/*
