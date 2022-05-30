
# Spectral–Spatial Attention Network for Hyperspectral Image Classification


### 1. Introduction

This is the reserch code of the IEEE Transactions Geoscience and Remote Sensing 2020 paper.

H. Sun, X. Zheng, X. Lu, and S. Wu, "Spectral–Spatial Attention Network for Hyperspectral Image Classification," IEEE Transactions Geoscience and Remote Sensing, vol. 58, no. 5, pp. 3232–3245, 2020.

Hyperspectral image (HSI) classification aims to assign each hyperspectral pixel with a proper land-cover label. Recently, convolutional neural networks (CNNs) have shown superior performance. To identify the land-cover label, CNN-based methods exploit the adjacent pixels as an input HSI cube, which simultaneously contains spectral signatures and spatial information. However, at the edge of each land-cover area, an HSI cube often contains several pixels whose land-cover labels are different from that of the center pixel. These pixels, named interfering pixels, will weaken the discrimination of spectral-spatial features and reduce classification accuracy. In this article, a spectral-spatial attention network (SSAN) is proposed to capture discriminative spectral-spatial features from attention areas of HSI cubes. First, a simple spectral-spatial network (SSN) is built to extract spectral-spatial features from HSI cubes. The SSN is composed of a spectral module and a spatial module. Each module consists of only a few 3-D convolution and activation operations, which make the proposed method easy to converge with a small number of training samples. Second, an attention module is introduced to suppress the effects of interfering pixels. The attention module is embedded into the SSN to obtain the SSAN. The experiments on several public HSI databases demonstrate that the proposed SSAN outperforms several state-of-the-art methods.

### 2. Start

Requirements:
             
        tensorflow-1.4.1
        
        numpy
                
        scipy
                
        scikit-image
                
        pandas



### 3. Related work 

If you find the code and dataset useful in your research, please consider citing:

 
     @article{sun2020spectral,
      title={Spectral--spatial attention network for hyperspectral image classification},
      author={Sun, Hao and Zheng, Xiangtao and Lu, Xiaoqiang and Wu, Siyuan},
      journal={IEEE Transactions on Geoscience and Remote Sensing},
      volume={58},
      number={5},
      pages={3232--3245},
      year={2020},
      publisher={IEEE}
    }

    @article{sun2021supervised,
      title={A supervised segmentation network for hyperspectral image classification},
      author={Sun, Hao and Zheng, Xiangtao and Lu, Xiaoqiang},
      journal={IEEE Transactions on Image Processing},
      volume={30},
      pages={2810--2825},
      year={2021},
      publisher={IEEE}
    }

    @article{yang2021cross,
      title={Cross-Attention Spectral-Spatial Network for Hyperspectral Image Classification},
      author={Yang, Kai and Sun, Hao and Zou, Chunbo and Lu, Xiaoqiang},
      journal={IEEE Transactions on Geoscience and Remote Sensing},
      year={2021},
      publisher={IEEE}
    }



