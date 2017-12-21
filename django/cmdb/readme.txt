使用sqllite3 数据库

python3 manage.py migrate   # 创建表结构
python3 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
python3 manage.py migrate TestModel   # 创建表结构

你可以通过命令 python manage.py createsuperuser 来创建超级用户，如下所示：
admin	yemwangyc
邮箱 test@163.com