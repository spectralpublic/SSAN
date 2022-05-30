
# Pairwise Comparison Network for Remote Sensing Scene Classification<!--论文标题-->


### 1. Introduction

This is the reserch code of the IEEE Transactions Geoscience and Remote Sensing 2020 paper.

H. Sun, X. Zheng, X. Lu, and S. Wu, "Spectral–spatial attention network for hyperspectral image classification," IEEE Transactions Geoscience and Remote Sensing, vol. 58, no. 5, pp. 3232–3245, 2020.

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

 
    @ARTICLE{8909379,
      author={Sun, Hao and Zheng, Xiangtao and Lu, Xiaoqiang and Wu, Siyuan},
      journal={IEEE Transactions on Geoscience and Remote Sensing}, 
      title={Spectral–Spatial Attention Network for Hyperspectral Image Classification}, 
      year={2020},
      volume={58},
      number={5},
      pages={3232-3245},
      doi={10.1109/TGRS.2019.2951160}}

    @ARTICLE{9347809,
      author={Sun, Hao and Zheng, Xiangtao and Lu, Xiaoqiang},
      journal={IEEE Transactions on Image Processing}, 
      title={A Supervised Segmentation Network for Hyperspectral Image Classification}, 
      year={2021},
      volume={30},
      number={},
      pages={2810-2825},
      doi={10.1109/TIP.2021.3055613}}

    @ARTICLE{8844315,
      author={Sun, Hao and Li, Siyuan and Zheng, Xiangtao and Lu, Xiaoqiang},
      journal={IEEE Transactions on Geoscience and Remote Sensing}, 
      title={Remote Sensing Scene Classification by Gated Bidirectional Network}, 
      year={2020},
      volume={58},
      number={1},
      pages={82-96},
      doi={10.1109/TGRS.2019.2931801}}

    @ARTICLE{8730481,
      author={Lu, Xiaoqiang and Sun, Hao and Zheng, Xiangtao},
      journal={IEEE Transactions on Geoscience and Remote Sensing}, 
      title={A Feature Aggregation Convolutional Neural Network for Remote Sensing Scene Classification}, 
      year={2019},
      volume={57},
      number={10},
      pages={7894-7906},
      doi={10.1109/TGRS.2019.2917161}}
    
    @ARTICLE{8730481,
      author={Lu, Xiaoqiang and Sun, Hao and Zheng, Xiangtao},
      journal={IEEE Transactions on Geoscience and Remote Sensing}, 
      title={A Feature Aggregation Convolutional Neural Network for Remote Sensing Scene Classification}, 
      year={2019},
      volume={57},
      number={10},
      pages={7894-7906},
      doi={10.1109/TGRS.2019.2917161}}




