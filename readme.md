# Chatbot_CN_Component


# Nama Entity Recognition
    - bert命名实体提取(bert12层embedding + bilstm + crf)
        - args.py(配置一些参数)
        - keras_bert_embedding.py(bert embedding)
        - keras_bert_layer.py(layer层, 主要有CRF和NonMaskingLayer)
        - keras_bert_ner_bi_lstm.py(主函数, 定义模型、数据预处理和训练预测等)
        - layer_crf_bojone.py(CRF层, 未使用)

# Intent


# Sentiment
