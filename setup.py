# from http://peterdowns.com/posts/first-time-with-pypi.html

from setuptools import find_packages, setup

setup(
  name = 'rpextract',
  packages = find_packages(),
  version = '0.1',
  description = 'Rhythm Pattern Audio Feature Extractor for Music Similarity, Music Classification and Music Recommendation',
  author = 'Thomas Lidy and Alexander Schindler',
  author_email = '',
  url = 'https://github.com/tuwien-musicir/rp_extract', # the URL to the github repo
  download_url = 'https://github.com/tuwien-musicir/rp_extract/tarball/0.1', # URL to the tagged version (use git tag 0.x -m "tagged version ..."; git push --tags origin master)
  keywords = ['audio', 'music', 'features', 'audio descriptors', 'feature extraction', 'music similarity', 'music recognition', 'music recommendation'],
  classifiers = [],
)