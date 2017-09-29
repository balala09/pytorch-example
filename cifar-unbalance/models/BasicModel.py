#coding:utf-8
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5,padding=(2,2))
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5,padding=(2,2))
        self.fc1 = nn.Linear(16 * 8 * 8, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 1)
    
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 8 * 8)
        x = F.relu(self.fc1(x))
        x = F.tanh(self.fc2(x))
        x = F.sigmoid(self.fc3(x))
        return x

import torch.optim as optim
def optimizer(net):
    optimize = optim.SGD(net.parameters(),lr=0.1)
    return optimize
    


    

if __name__=="__main__":
    net = Net()
    torch.save(net.state_dict(),"init.pkl")
    n = Net()
    n.load_state_dict(torch.load("init.pkl"))
    print n
