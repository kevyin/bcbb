cd ~/dev/galaxy_pipeline/bcbb/nextgen

python setup.py install --record files.txt
cat files.txt | parallel -j4 "rm -rf {}"
python setup.py install
