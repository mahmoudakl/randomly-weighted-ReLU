import torch
import torch.nn as nn


def random_relu(input, weight):
    return weight*torch.relu(input)


class RandomReLU(nn.Module):
    def __init__(self):
        super(RandomReLU, self).__init__()

    def forward(self, input, weight):
        return random_relu(input, weight)
