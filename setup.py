try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README') as file:
    long_description = file.read()

setup(name='vv-flask-restful-swagger',
      version='0.20.1',
      url='https://github.com/openvar/vv-flask-restful-swagger.git',
      zip_safe=False,
      packages=['vv_flask_restful_swagger'],
      package_data={
        'vv_flask_restful_swagger': [
          'static/*.*',
          'static/css/*.*',
          'static/images/*.*',
          'static/lib/*.*',
          'static/lib/shred/*.*',
        ]
      },
      description='Extract swagger specs from your flast-restful project',
      author='Ran Tavory',
      license='MIT',
      long_description=long_description,
      install_requires=['Flask-RESTful>=0.3.6']
      )
