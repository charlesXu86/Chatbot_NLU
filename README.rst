一、Chatbot_NLU
==========================

    Chatbot_NLU是一个基于RASA的自定义中文语言理解组件

1、钉钉群：

2、微信公众号；

3、QQ群；

4、外部平台：如电商平台、网页端等


二、安装使用
============

::

    pip install chatbot_nlu


三、使用示例
======================

1、dingtalk

.. code:: python

    import chatbot_help as ch
    from chatbot_help import DingtalkChatbot

    print(ch.__version__)                # 打印版本信息
    dtalk = DingtalkChatbot(webhook)     # 你设置群机器人的时候生成的webhook

详情请参考：`Dingtalk_README <https://github.com/charlesXu86/Chatbot_Help/blob/master/Dingtalk_README.rst>`_

2、wetalk

.. code:: python



四、Update News
======================

    * 2020.1.7  接入钉钉群，支持主动推送消息、outgoing交互

    * 2020.1.9  接入微信



五、Resources
======================

.. _`Dingtalk_README`: https://github.com/charlesXu86/Chatbot_Help/blob/master/Dingtalk_README.rst
