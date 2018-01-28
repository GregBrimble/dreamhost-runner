cd ~
mkdir tmp
cd tmp

echo -n "Enter the version of Python you want to install (e.g. '3.6.4'): "
read version

wget https://www.python.org/ftp/python/$version/Python-$version.tgz
tar zxvf Python-$version.tgz
cd Python-$version

./configure --prefix=$HOME/opt/python-$version
make
make install

echo "export PATH=\$HOME/opt/python-$version/bin:\$PATH" >> ~/.bash_profile
rm -rf tmp
echo "Complete! Now run '. ~/.bash_profile' to update your path, and then check to see it installed correctly."
