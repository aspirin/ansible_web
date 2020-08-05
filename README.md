scp -r * root@192.168.1.16:/home/jz/ansibleSite/


yum install epel-release
yum -y install sqlite-devel
wget http://www.openssl.org/source/openssl-1.0.2j.tar.gz
tar -zxvf openssl-1.0.2j.tar.gz
cd openssl-1.0.2j
./config --prefix=/usr/local/lab/openssl-1.0.2j shared zlib
make && make install
ln -s /usr/local/lab/openssl-1.0.2j/lib/libssl.so.1.0.0 /usr/lib64/libssl.so.1.0.0
ln -s /usr/local/lab/openssl-1.0.2j/lib/libcrypto.so.1.0.0 /usr/lib64/libcrypto.so.1.0.0

wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz
tar xvf Python-3.8.5.tgz
cd Python-3.8.5
./configure --prefix=/usr/local/python38 --enable-optimizations --enable-loadable-sqlite-extensions
vi Modules/Setup
SSL=/usr/local/lab/openssl-1.0.2j/    #取消这一行的注释，并将原来的/usr/local/ssl改为我们新安装的openssl目录：/usr/local/lab/openssl-1.0.2j/
_ssl _ssl.c \     #取消这一行的注释
-DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \      #取消这一行的注释
-L$(SSL)/lib -lssl -lcrypto      #取消这一行的注释

make && make install

/usr/local/python38/bin/pip3.8 install django==3.0.5

/usr/local/python38/bin/pip3.8 install -r requirements.txt