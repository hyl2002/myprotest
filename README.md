，视觉结业任务的心得：1做一个数据集的前提条件是要有一个标注软件的，根据教程我们使用的是labelImg软件来作为标注工具，在实践中发现Pip下载lambelImg的速度太慢，有时候会导致安装不成功，在这里我使用的conda命令conda install labelImg后下载成功，下载成功后，有了标注工具就要有图片的数据集，这里我是在网上找了几个数据集，将他们的图片给复制粘贴到我存放图片的文件夹内，
2进行图片的标注，并生成xml文件，在下载成功的labelImg中打开终端使用python labelImg.py赖实现打开labelImg，labelImg的使用我参考的是https://blog.csdn.net/Dontla/article/details/102662815，
3使用darknet框架进行训练，3.1从github仓库中拉取darknet文件，克隆到本地中，随后跳转到下载好的darknet文件目录中，对Makefile进行配置，在配置中1代表含有，0代表没有，根据自己电脑上的配置来进行，配置完成后开始编译，在该页面打开终端输入make命令，可能会出现错误大概意思就是darknet不能进行cudnn8的编码问题，参考https://github.com/arnoldfychen/darknet/blob/master/scr/convolutional_layer.c  4.使用yolov3来进行预训练模型的下载打开终端输入wget https://pjreddie.com/media/files/yolov3.weights
对下载的预训练模型进行测试：打开终端输入./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg，测试完成后会弹出识别的图片
按按照教程在darknet目录下创建myData下的文件，创建存放图像的文件夹JPEGImages，创建存放对应的xml文件的文件夹Annotations，创建存放训练、验证图片的文件夹ImageSets/Main，相对应的图片和xml文件放入对应的文件夹中，然后在myData的文件夹中创建一个test.py将教程中的代码拷贝运行生成四个文件（train.txt,val.txt,test.txt和trainval.txt）。
随后就是将数据转化为darknet支持的格式，使用教程中的脚本my_labels.py，此时先不必着急运行，及将自己在标注工具中标注好的类的名字进行更改到对应的类别中，此时进行保存操作，随后在该目录下开终端进行运行操作：python my_labels.py.运行完后会在./myData目录下生成一个labels文件夹一个txt文件(myData_train.txt)(内容是: 类别的编码和目标的相对位置)。
进行darkney/cfg下修改voc.data和yolov3-voc.cfg将myData_train.txt，myData.names,weights对应的绝对路径修改一下成自己实际的路径,随后进行哟liv.cfg文件的修改，修改的规则就是/yolo, 总共会搜出3个含有yolo的地方。每个地方都必须要改2处， filters：3*（5+len（classes））其中：classes: len(classes) = 3，这里以我的工程为例filters = 24classes = 3
指定训练的批次和训练轮数，这里要注意的是你到底是想测试还是训练，如果是前者，则需要将训练模式注释掉，测试模式打开，随后根据max_batches = 50200 ### 同样的根据后者，通过设置迭代次数可以控制自己训练的次数。
上述操作完成后需要在myData文件夹下更改自己的类的名称，此处更改依据的是自己在标注工具上设置的类的标签
随后进行预训练权重的下载：打开终端使用：wget https://pjreddie.com/mediafiles/darknet53.conv.74来进行下载
一切准备就绪后使用终端：./darknet detect cfg/my_yolov3.cfg weights/my_yolov3.weights 1.jpg来进行测试（前面的是训练好的模型的路径后面是图片的路径）
识别完后可以在predicition.jpg中找出来测试的图片。