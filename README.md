# Visual EEG Pattern Synthesis and Recognition with Deep Learning

This project focuses on analyzing and generating EEG signal patterns using deep learning techniques. It leverages CNNs for classification and conditional GANs (cGANs) for synthesizing realistic EEG data. The work is based on `.npy` and `.dat` EEG datasets and implemented using PyTorch.

## 📌 Project Objectives

- 🧠 **Classify** real EEG signals using Convolutional Neural Networks (CNN).
- 🔁 **Generate** synthetic EEG-like signals using Conditional GANs (cGAN).
- 📊 **Compare** generated and real signals using similarity metrics like SSIM and visualization tools.

## 📂 Data Format

- `.npy`: NumPy binary files containing preprocessed EEG signals.
- `.dat`: Raw EEG signal data or label arrays in binary format.

### Data Files
The `1.npy` file has been compressed for GitHub upload.  
📦 Download and unzip `Data/1.zip` to get the `1.npy` file.

## 🧠 Models Used

- **CNN**: For classifying EEG signals.
- **cGAN**: For synthesizing realistic EEG data based on conditional labels.

## 📈 Evaluation Metrics

- **SSIM (Structural Similarity Index)**: To compare real and generated EEG visual representations.
- **Accuracy**: For CNN classification performance.

## 🛠️ Libraries & Tools

- Python
- PyTorch
- NumPy
- Matplotlib
- Scikit-image (SSIM)

## 🚀 Getting Started

```
git clone https://github.com/SiddardhaShayini/Visual_EEG_Pattern_Synthesis_and_Recognition_with_Deep_Learning.git
```
```
cd Visual_EEG_Pattern_Synthesis_and_Recognition_with_Deep_Learning
```

Open the notebook in Colab or Jupyter to explore the code.

## 🙌 Contributions

Open to improvements, better visualization, and GAN enhancements. Pull requests are welcome!


**Author:** Siddardha Shayini  
**License:** MIT


