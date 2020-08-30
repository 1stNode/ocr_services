# 银行支票OCR识别
## 场景说明
银行支票的文字提取以及信息结构化输出；
如下图所示：
  <div align="center">
    <img src="pics/bankcheque_01.jpg" height="60%" width="60%" >
  </div>

### 特点
1. 支持扫描件的识别
2. 支持机打，手写，机打手写混合

## 请求与返回
- URI
  ```
  /ocr/api/common
  ```

- 产品代码
  - I_BANK_CHEQUE_BASE

- 请求返回说明
    - 响应结果参数说明：
      - code，字符串类型，接口调用状态码
      - message，字符串类型，接口调用状态描述信息
      - result:，识别结果数组，具体格式定义如下：
        - ocr_type : 字符串类型，产品类型编号，各产品类型编号详见产品定义章节
        - logid: 字符串类型，调用时传入的图像唯一编号，方便调用端定位
        - content : 识别结果键值对
          - key : 字符串类型，识别结果的字段名
          - value : 字符串类型，识别结果文本内容
          - score: 字符串类型，识别结果置信度
    - 支票Content字段说明：
        | key            | 对应字段     |
        | :------------- | :----------- |
        | voucher_no_1   | 支票号码1    |
        | voucher_no_2   | 支票号码2    |
        | issue_date     | 出票日期     |
        | payer_bank     | 付款行名称   |
        | payee_name     | 收款人名称   |
        | payer_account  | 出票人账号   |
        | amount_chinese | 金额（大写） |
        | amount         | 金额（小写） |
        | purpose        | 用途        |
        | password       | 支付密码     |
        | bank_no        | 行号         |
        |                |
                  
    - 请求返回示例
        ```json
        {
            "code": "OK", 
            "message": "success", 
            "result": [
                {
                    "ocr_type": "T_BANK_CHEQUE", 
                    "logid": "c9f951b5-861a-4088-8107-2a7ffa6f1946", 
                    "content": [
                        {
                            "key": "voucher_no_1", 
                            "value": "00128010", 
                            "score": 0.66733
                        }, 
                        {
                            "key": "voucher_no_2", 
                            "value": "35549756", 
                            "score": 0.9967
                        }, 
                        {
                            "key": "issue_date", 
                            "value": "20100407", 
                            "score": 0.9945
                        }, 
                        {
                            "key": "payer_bank", 
                            "value": "光大银行济南泉城支行", 
                            "score": 0.48798
                        }, 
                        {
                            "key": "payee_name", 
                            "value": "利津县众合工贸有限公司", 
                            "score": 0.96108
                        }, 
                        {
                            "key": "payer_account", 
                            "value": "055247766047", 
                            "score": 0.9974
                        }, 
                        {
                            "key": "amount_chinese", 
                            "value": "伍佰陆拾伍萬零叁佰玖拾捌元整", 
                            "score": 0.54086
                        }, 
                        {
                            "key": "amount", 
                            "value": "162659.00", 
                            "score": 0.7441
                        }, 
                        {
                            "key": "purpose", 
                            "value": "人力费", 
                            "score": 0.93362
                        }, 
                        {
                            "key": "password", 
                            "value": "6473961178734168", 
                            "score": 0.669
                        }, 
                        {
                            "key": "bank_no", 
                            "value": "", 
                            "score": 0.0
                        }
                    ]
                }
            ]
        }
        ```
