How to Use?
===========

这是为VsCode配套的Hypersnips配置。

使用方法：

在VsCode中搜索安装名为 ``hypersnips`` 的扩展，作者 ``draivin`` 那个。

安装后，在VsCode中按 ``F1`` ，找到命令 ``HyperSnips: Open Snippets Directory``，点击，然后会打开一个目录。

``C:\Users\你的用户名\AppData\Roaming\Code\User\hsnips``

将 ``reStructuredText.hsnips`` 拷贝至此目录。


基本用户请使用基础版（Basic），即装即用。

高阶应用（配合外部脚本调用，需要修改相关的路径并安装依赖库）请使用高阶版（Advanced）。

基础版
======

用法
======


拷贝到对应目录即可。


提供的功能
----------

.. code-block::

    n       顶级双线标题
    a       单线一级标题（本质上这是整个文档的第二级标题，以下类推）
    b       单线二级标题
    c       单线三级标题
    cb      code-block代码块
    com     笔者作者注释（自定义）
    cnt     contents页内自动目录指令（用于渲染输出的结果）
    im      image指令

其中标题的长度会根据文本长度自动计算，中文字计算为2个字符长度。最短为6个字符长度。相关参数可自行调整。标题标记符自行设定。

高阶版
======

用法
------

1.  拷贝

    将 ``advanced`` 目录下所有文件拷贝至 ``C:\Users\你的用户名\AppData\Roaming\Code\User\hsnips`` 。


2.  安装依赖


    #.  安装 python 3.x 最新版。

    #.  安装 Python 第三方分词工具包，以实现自动关键字切分，使用如下命令（已切换国内源）：

        .. code-block::

            pip install -i https://pypi.tuna.tsinghua.edu.cn/simple jieba

    #.  然后视情况决定是否安装node.js（例如想要手动升级iconv版本，或者有运行问题需要调试）

3.  按需根据注释修改 ``reStructuredText.hsnips`` 中的配置代码。

    #.  例如修改第33行的名字；
    #.  例如修改标题标记符（27行）
    #.  例如修改依赖路径，以分别指向：

        #.  node_modules目录。
        #.  python脚本程序的路径。

提供的功能
----------

在基础版之外，额外添加以下功能：

.. code-block::

    i       生成index.rst中的内容，模板为递归同构文件夹形态
    nw      生成带元数据标签的文件头，模板是“互联网摘抄笔记”
    nn      生成带元数据标签的文件头，模板是“个人创作的笔记”
    e!      生成引用锚（发起）
    r!      生成引用锚（接收）
    sub     下标
    sup     上标
    fn      获取当前文档文件名

扩展指南
--------

#.  可根据该示例自行添加函数、snippets。
#.  hypersnips的全局变量与vscode内置的snippets全局变量是兼容的，即可以在hsnips中使用VsCode的全局变量，如 ``$TM_FILENAME_BASE`` 等。具体详见 https://code.visualstudio.com/docs/editor/userdefinedsnippets


Enjoy it!

更多修改请参阅 Hypersnips 文档 https://github.com/draivin/hsnips 。
