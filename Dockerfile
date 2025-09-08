#Docker file

#步骤1:选择一个带有python 3.9环境的轻量化Linux
FROM python:3.10-slim

#步骤2:在容器中创建一个工作目录/app，作为操作台
WORKDIR /app

#步骤3:先把需求清代，即requirements 复制到docker中，利用Docker的缓存机制，只要清单不便，下一步的安装就不需要重复进行
COPY requirements.txt .

#步骤4：根据需求清单，安装依赖库
#--no-cache-dir 选项可以减少镜像体积
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

#步骤5:把项目代码的所有文件拷贝到工作目录中
COPY . .

#步骤6：设置环境变量，告诉python代码启用无头模式
ENV HEADLESS=true

#步骤7:定义容器启动时，默认执行指令
CMD ["pytest"]

#docker build -t my-automation-project:1.0
#docker run --rm --network=host -v "$(pwd)/reports":/app/reports my-automation-project:1.0

#docker run -it --rm my-automation-project:1.0 /bin/bash