# DeepNLPIntro  
Hands on introduction to Deep learning for NLP using MLP, CNN, and RNN/LSTM for language classificatin and translation.  

### Topic Outline  
[Deep Learning](slides/1%20Deep%20Learning%20Introduction.pdf)  
- Deep Learning Concepts   
- Instructions for running labs  

[Text Classification](slides/2%20NLP%20Text%20Classification)  
- NLP, why NLP is hard  
- Embeddings  
- Neural architectures for NLP   
- Context for Lab 1 - Sentiment Classification   

#### Lab 1 – Sentiment Classification  
- Text classification  
- NLP vocabulary  
- Embeddings  
- Network architectures: MLP, CNN, RNN   
- Model development and evaluation, review  
- [Sentiment Classification Notebook](Text%20Classification/SentimentClassification.ipynb)  

[Text Translation](slides/3%20NLP%20Text%20Translations.pdf)    
- Encoder - decoder   
- Bidirectional LSTM  
- Attention  
- Neural architectures for NLP   
- Context for Lab 2 - Date Translation   

#### Lab 2 – Date translation  
- Encoder-decoder  
- Attention  
- Network architecture: LSTM with attention  
- Model development and evaluation, review  
- [Text Translation Notebook](Text%20Translation/TextTranslation.ipynb)  

### Running the NLP workshop labs

#### Google Collab (recommended)

Detailed instructions can be found in the intro slides: [Deep Learning](slides/1%20Deep%20Learning%20Introduction.pdf) 

#### Docker
1) Install Docker CE  
https://www.docker.com/community-edition   

2) Open a terminal and run Docker to launch the workshop image in a Docker container  

$ docker run -p 8889:8888  jayurbain/deepnlpintro:latest  

You will see something like the following. Copy the token highlighted below.  

```
$ docker run -p 8889:8888  jayurbain/deepnlpintro:latest
[I 00:54:28.847 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[W 00:54:28.889 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
[I 00:54:28.905 NotebookApp] Serving notebooks from local directory: /notebooks
[I 00:54:28.905 NotebookApp] 0 active kernels
[I 00:54:28.905 NotebookApp] The Jupyter Notebook is running at:
[I 00:54:28.905 NotebookApp] http://7da85c11dc3a:8888/?token=e1bc2fe905e1b0de7ec0820b03841c9d7d3bb434377540df
[I 00:54:28.906 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 00:54:28.907 NotebookApp]
```

    Copy/paste this URL into your browser when you connect for the first time,  
    to login with a token:  
        http://7da85c11dc3a:8888/?token=e1bc2fe905e1b0de7ec0820b03841c9d7d3bb434377540df&token=e1bc2fe905e1b0de7ec0820b03841c9d7d3bb434377540df

3) Open Chrome browser to localhost, port 8889, with the token  

http://localhost:8889/?token=e1bc2fe905e1b0de7ec0820b03841c9d7d3bb434377540df  
