### 关于代码的说明如下：

------
#### 上传说明：
model.py、agents.py、game.py及权重文件上传在game2048文件夹中；其余文件直接上传在最外层目录下。

#### 运行说明：
1. data_generate.py、data_filtrate.py、data_threshold.py、data_combine.py分别用于产生数据、筛选需要的数据段、缩小数据集规模和合并数据集。
2. 命令行运行python model.py:可训练模型并保存训练得到的权重文件（用load_model函数导入欲优化的模型的权重文件）。
3. 命令行运行python agents.py:可编译生成自己的agent(MyOwnAgent)。其中agents.py中增加了MyOwnAgent的定义，并导入了自己模型的权重文件；由于MyOwnAgent对棋盘取对数进行预测，因此在game.py的Game类中添加了board_log(self)函数，预先将棋盘中的0转为1，以便取对数。
4. 命令行运行python evaluate.py >> evaluation.log:可利用自己的代理模型控制50局2048游戏，并输出均分和各局分别的得分。
5. 命令行运行python generate_fingerprint.py可生成自己模型的指纹。
