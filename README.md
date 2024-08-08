# Projeto de Reconhecimento Facial

Este projeto realiza reconhecimento facial utilizando o script `detect.py`.

## Estrutura do Projeto

- `__pycache__/`: Diretório para arquivos cache do Python.
- `.gitignore`: Arquivo para especificar quais arquivos e diretórios devem ser ignorados pelo Git.
- `detect.py`: Script principal para realizar o reconhecimento facial.
- `log_reconhecimento_facial.txt`: Arquivo de log para registrar as atividades de reconhecimento facial.
- `README.md`: Este arquivo de documentação.
- `requirements.txt`: Arquivo com as dependências do projeto.

## Requisitos

Para executar este projeto, você precisará instalar as dependências listadas no arquivo `requirements.txt`. Para instalar as dependências, execute:

```sh
pip install -r requirements.txt
```

# Sistema de Reconhecimento Facial em Tempo Real

Este código implementa um sistema de reconhecimento facial em tempo real utilizando a biblioteca **DeepFace** do Python. Ele captura o vídeo da webcam, detecta rostos, identifica as pessoas com base em um banco de dados, e exibe os nomes das pessoas detectadas na imagem.

## Funcionalidades

- Captura de vídeo em tempo real usando a webcam.
- Detecção e localização de rostos na imagem.
- Identificação das pessoas presentes no banco de dados.
- Exibição dos nomes das pessoas identificadas na imagem.
- Registro de logs em um arquivo de texto para acompanhamento e depuração.

## Bibliotecas Utilizadas

- `deepface`: Biblioteca para reconhecimento facial, utilizada para realizar a detecção e identificação de rostos.
- `cv2`: Biblioteca OpenCV, utilizada para captura de vídeo e manipulação da imagem.
- `logging`: Biblioteca padrão do Python, utilizada para registro de logs.

## Uso

1. Certifique-se de ter as bibliotecas `deepface` e `opencv-python` instaladas em seu ambiente Python.
2. Coloque o banco de dados de fotos das pessoas a serem reconhecidas na pasta `Data/`.
3. Execute o script Python.
4. O sistema iniciará a captura de vídeo da webcam e exibirá a janela com o reconhecimento facial em tempo real.
5. Pressione a tecla 'q' para encerrar o programa.

## Registro de Logs

O código configura um registro de logs em um arquivo chamado `log_reconhecimento_facial.txt`. Todas as informações, avisos e erros são registrados neste arquivo para acompanhamento e depuração.

## Personalizações

O código permite algumas personalizações, como:

- Alterar o modelo de reconhecimento facial utilizado (`modelos`).
- Alterar a métrica de distância utilizada (`metricas`).
- Alterar o backend de detecção de rostos (`backends`).
- Ajustar a janela de exibição do vídeo.

Certifique-se de consultar a documentação da biblioteca `DeepFace` para obter mais informações sobre estas opções.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Basta abrir uma nova issue ou enviar um pull request.
