import numpy as np
import torch
from torch import nn, optim
from torchvision.datasets import ImageFolder
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from torchvision import models
import os
import cv2
import matplotlib.pyplot as plt

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')



normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
train_augs = transforms.Compose([transforms.Resize(size=(224,224)), transforms.ToTensor(), normalize])
test_augs = transforms.Compose([transforms.Resize(size=(224,224)), transforms.ToTensor(), normalize])

pretrained_net = models.resnet50(pretrained=True)
print(pretrained_net.fc)

pretrained_net.fc = nn.Linear(2048, 4)
pretrained_net.to(device)

output_params = list(map(id, pretrained_net.fc.parameters()))
feature_params = filter(lambda p: id(p) not in output_params, pretrained_net.parameters())

lr = 0.01

batch_size = 1
num_epoch = 10

optimizer = optim.SGD([{'params':feature_params}, {'params':pretrained_net.fc.parameters(), 'lr': lr * 10}], lr=lr, weight_decay=0.001)


loss_fn = torch.nn.CrossEntropyLoss()

    
def single_pre(model, val_loader, device):
    model.eval()
    
    res = []

    with torch.no_grad():
        for batch_idx, (data, target) in enumerate(val_loader):
            data, target = data.to(device), target.to(device)
            yhat = model(data)
            
            pred = torch.max(yhat, dim=1, keepdim=True)[1]  #注10：找到概率最大的下标
            res.append((pred.numpy())[0][0])
            # 0 hole
            # 1 normal
            # 2 scratched
            # 3 shaved
    return res        

def predict_():
    predict_imgs = ImageFolder('D:/dataset0511/output/cache', transform=test_augs)
    
    predict_iter = DataLoader(predict_imgs, batch_size, shuffle=False)
    pretrained_net = torch.load('model0525.pkl', map_location='cpu')
    print('------TEST------')
    
    res = single_pre(pretrained_net, predict_iter, device)
    print(res)
    return res





