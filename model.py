import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super().__init__()

        #Add Linear NN layers
        self.layer1 = nn.Linear(64*64,512)
        self.layer2 = nn.Linear(512,512)
        self.layer3 = nn.Linear(512,256)
        self.layer4 = nn.Linear(256,10)
    
    def forward(self,x):
        
        #Pass x through the sequence of layers. Don't forget activation functions!
        x = self.layer1(x)
        x = nn.ReLU()(x)
        x = self.layer2(x)
        x = nn.ReLU()(x)
        x = self.layer3(x)
        x = nn.ReLU()(x)
        x = self.layer4(x)

        return x