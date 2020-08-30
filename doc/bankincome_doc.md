# 银行进账单OCR识别
## 场景说明
银行进账单的文字提取以及信息结构化输出；
如下图所示：
  <div align="center">
    <img src="pics/bankincome_01.jpg" height="60%" width="60%" >
  </div>

### 特点
1、支持扫描件的识别
2、支持机打，手写，机打手写混合

### 请求返回说明
    - 响应结果参数说明：
    - result:，识别结果数组，具体格式定义如下：
      - ocr_type : 字符串类型，产品类型编号，各产品类型编号详见产品定义章节
      - logid: 字符串类型，调用时传入的图像唯一编号，方便调用端定位
      - content : 识别结果键值对
        - key : 字符串类型，识别结果的字段名
        - value : 字符串类型，识别结果文本内容
        - score: 字符串类型，识别结果置信度
    - 支票Content字段说明：
        | key            | 对应字段     |
        | :------------- | :--------- |
        | issue_date     | 出票日期    |
        | payer_name     | 出票人全称   |
        | payer_account  | 出票人账号   |
        | payer_bank     | 出票人行名   |
        | payee_name     | 收款人全称   |
        | payee_account  | 收款人账号   |
        | payee_bank     | 收款人行名   |
        | amount_chinese | 金额（大写） |
        | amount         | 金额（小写） |
        | remark         | 备注        |
        |
        
    - 请求返回示例
        ```json
        {
            "code": "OK",
            "message": "success",
            "result": [
                {
                    "ocr_type": "T_BANK_INCOME",
                    "logid": "d11f98d1-e229-4836-81d9-7d0b0ef3cdd8",
                    "content": [
                        {
                            "key": "issue_date",
                            "value": "20220219",
                            "score": 0.993
                        },
                        {
                            "key": "payer_name",
                            "value": "上海中原物业顾问有限公司沪亭北路第三分公司",
                            "score": 0.98369
                        },
                        {
                            "key": "payer_account",
                            "value": "0220901225820031",
                            "score": 0.559
                        },
                        {
                            "key": "payer_bank",
                            "value": "中信银行张家港保税区支行",
                            "score": 0.62986
                        },
                        {
                            "key": "payee_name",
                            "value": "南京冠华高新技术研究所",
                            "score": 0.88564
                        },
                        {
                            "key": "payee_account",
                            "value": "536040005598194",
                            "score": 0.9938
                        },
                        {
                            "key": "payee_bank",
                            "value": "大连农商行山东路支行",
                            "score": 0.9913
                        },
                        {
                            "key": "amount_chinese",
                            "value": "伍万壹仟零佰伍拾伍拾玖元整",
                            "score": 0.7607
                        },
                        {
                            "key": "amount",
                            "value": "13048.17",
                            "score": 0.7024
                        },
                        {
                            "key": "remark",
                            "value": "往来款",
                            "score": 0.9992
                        }
                    ]
                }
            ],
        }
        ```
