# Sistema de Reconhecimento Facial

Este projeto implementa um sistema de reconhecimento facial em tempo real usando a biblioteca DeepFace e OpenCV. O sistema captura vídeo de uma webcam, detecta rostos e os identifica usando modelos pré-treinados.

## Estrutura do Projeto

```
__pycache__/
.gitignore
data/
    ds_model_facenet512_detector_opencv_aligned_normalization_base_expand_0.pkl
    README.md
detect.py
log_reconhecimento_facial.txt
README.md
requirements.txt
```

- `data/`: Contém o modelo pré-treinado e um arquivo README.
- `detect.py`: Script principal para executar o sistema de reconhecimento facial.
- `log_reconhecimento_facial.txt`: Arquivo de log para registrar eventos e erros do sistema.
- `requirements.txt`: Lista de dependências Python necessárias para o projeto.

## Instalação

1. Clone o repositório.
2. Instale os pacotes Python necessários usando pip:

    ```sh
    pip install -r requirements.txt
    ```

## Uso

Execute o script `detect.py` para iniciar o sistema de reconhecimento facial:

```sh
python detect.py
```

## Visão Geral do Código

### `detect.py`

Este script contém a lógica principal do sistema de reconhecimento facial.

#### Importações

```python
from deepface import DeepFace
import cv2
import logging
```

#### Configuração de Log

```python
def configurar_log():
    logging.basicConfig(filename='log_reconhecimento_facial.txt', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
```

#### Função de Log

```python
def registrar_log(mensagem, nivel='info'):
    if nivel == 'info':
        logging.info(mensagem)
    elif nivel == 'erro':
        logging.error(mensagem)
    elif nivel == 'aviso':
        logging.warning(mensagem)
```

#### Modelos e Métricas Disponíveis

```python
backends = ["opencv", "ssd", "dlib", "mtcnn", "retinaface"]
modelos = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
metricas = ["cosine", "euclidean", "euclidean_l2"]
```

#### Função de Reconhecimento Facial em Tempo Real

```python
def reconhecimento_facial_tempo_real():
    # ... (código da função)
```

#### Execução Principal

```python
configurar_log()
registrar_log("Sistema de reconhecimento facial iniciado.")
reconhecimento_facial_tempo_real()
```

## Licença

Este projeto está licenciado sob a Licença MIT.