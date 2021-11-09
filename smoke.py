import torch.nn as nn
import torch
from torchvision.models.resnet import ResNet, BasicBlock


class SmokeClassifier(ResNet):
    def __init__(self):
        super(SmokeClassifier, self).__init__(BasicBlock, [2,2,2,2], num_classes=2)


        