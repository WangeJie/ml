#��װPython�Ĳ���
mkdir -p /home/limeihang/lcy/software/python27
./configure --prefix="/home/limeihang/lcy/software/python27"
/home/limeihang/lcy/software/python27/bin/python setup.py install
/home/limeihang/lcy/software/python27/bin/python setup.py install
#�����ƶ�Ŀ¼
cd /home/limeihang/lcy/software/python27/bin/
#����PythonΪ������
PATH=$PATH:/home/limeihang/lcy/software/python27/bin
export PATH=/home/limeihang/lcy/software/python27/bin/:$PATH
source .bash_profile
#�鿴���н��
ps -ef |grep main2.py
#���г���
nohup python main3.py &