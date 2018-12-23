## python learning  
https://developer.github.com/v3/users/  

### install python(linux)  
requirements:  
yum -y groupinstall "Development tools"  
yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel  
1 wget  https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz  
2 ./configure --prefix=/opt/python3.6  --with-ssl  
3 make  
4 make install  
5 vim /etc/profile, export PATH=/opt/python3.6/bin:$PYTHON  
pip install ipython  


