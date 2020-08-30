# coding=utf-8

import os
import sys

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
import cv2

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

from service.income_service import IncomeService
from service.cheque_service import ChequeService
from service.rec_service import RecService


if __name__ == "__main__":
    income_image = cv2.imread('test_datas/002.jpg')
    cheque_image = cv2.imread('test_datas/001.jpg')
    image = cv2.imread('test_datas/0_0.jpg')

    rec_service = RecService()
    r_result = rec_service.image_pred([image])
    print(r_result)

    cheque_service = ChequeService()
    c_result = cheque_service.image_pred([cheque_image])
    print(c_result)

    income_service = IncomeService()
    i_result = income_service.image_pred([income_image])
    print(i_result)
