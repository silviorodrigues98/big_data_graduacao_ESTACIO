---
marp: true
---
<!-- _class: lead -->
# Reconhecimento Facial em Tempo Real

---

## Importação das Bibliotecas

```python
from deepface import DeepFace
import cv2
import logging
```

- **DeepFace**: Biblioteca usada para análise facial.
- **cv2**: Utilizada para captura e manipulação de vídeo.
- **logging**: Para registro de logs.

---

## Configuração do Log

```python
def configurar_log():
    logging.basicConfig(
        filename='log_reconhecimento_facial.txt',
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
```

- Configuração básica do log com nível de informação.
- O log será gravado no arquivo `log_reconhecimento_facial.txt`.

---

## Função para Registrar Logs

```python
def registrar_log(mensagem, nivel='info'):
    if nivel == 'info':
        logging.info(mensagem)
    elif nivel == 'erro':
        logging.error(mensagem)
    elif nivel == 'aviso':
        logging.warning(mensagem)
```

- **registrar_log**: Função genérica para registrar diferentes níveis de logs (info, erro, aviso).

---

## Parâmetros do Reconhecimento Facial

```python
backends = ["opencv", "ssd", "dlib", "mtcnn", "retinaface"]
modelos = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
metricas = ["cosine", "euclidean", "euclidean_l2"]
```

- **Backends**: Opções de métodos de detecção de rosto.
- **Modelos**: Diferentes modelos de reconhecimento facial.
- **Métricas**: Métricas de distância para comparação de rostos.

---

## Captura e Processamento de Vídeo

```python
def reconhecimento_facial_tempo_real():
    video = cv2.VideoCapture(0)
    registrar_log("Captura de vídeo iniciada.")
```

- Inicia a captura de vídeo da webcam.
- Log de início da captura.

---

## Detecção e Identificação de Rostos

```python
pessoas = DeepFace.find(
    img_path=quadro, 
    db_path="Data/", 
    model_name=modelos[2], 
    distance_metric=metricas[2], 
    enforce_detection=False
)
registrar_log(f"{len(pessoas)} rostos detectados.")
```

- **DeepFace.find**: Encontra e identifica rostos na imagem capturada.
- Loga o número de rostos detectados.

---

## Exibição dos Resultados

```python
cv2.rectangle(quadro, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.putText(quadro, nome, (x, y), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)
cv2.imshow('RECONHECIMENTO FACIAL', quadro)
```

- Desenha um retângulo ao redor do rosto detectado.
- Exibe o nome da pessoa identificada.
- Mostra a imagem processada em uma janela.

---

## Finalização do Sistema

```python
video.release()
cv2.destroyAllWindows()
registrar_log("Sistema de reconhecimento facial encerrado.")
```

- Libera a captura de vídeo.
- Fecha todas as janelas abertas.
- Log de encerramento do sistema.

---

## Execução do Sistema

```python
configurar_log()
registrar_log("Sistema de reconhecimento facial iniciado.")
reconhecimento_facial_tempo_real()
```

- Configura e inicia o log.
- Inicia o sistema de reconhecimento facial em tempo real.