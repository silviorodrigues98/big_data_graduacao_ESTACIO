import cv2
import logging
from deepface import DeepFace

def configurar_log():
    logging.basicConfig(filename='log_reconhecimento_facial.txt', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

def registrar_log(mensagem, nivel='info'):
    print(f"LOG: {mensagem}")
    if nivel == 'info':
        logging.info(mensagem)
    elif nivel == 'erro':
        logging.error(mensagem)
    elif nivel == 'aviso':
        logging.warning(mensagem)

def reconhecimento_facial_tempo_real():
    # Definir um objeto de captura de vídeo
    video = cv2.VideoCapture(0)
    registrar_log("Captura de vídeo iniciada.")

    cv2.namedWindow('Reconhecimento Facial', cv2.WINDOW_NORMAL)

    while True:
        # Capturar o quadro do vídeo frame a frame
        ret, frame = video.read()
        if not ret:
            registrar_log("Erro: Não foi possível capturar o quadro de vídeo", nivel='erro')
            break
        
        # Encontrar rostos e identificar pessoas usando um modelo específico e métrica de distância
        try:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pessoas = DeepFace.find(img_path=img, db_path="Data/", model_name="VGG-Face", distance_metric="cosine", enforce_detection=False)
            registrar_log(f"{len(pessoas)} rostos detectados.")
        except Exception as e:
            registrar_log(f"Erro: Não foi possível abrir o banco de dados. Detalhes: {str(e)}", nivel='erro')
            break
        
        if len(pessoas) == 0:
            registrar_log("Nenhum rosto detectado no banco de dados.")
            break
        
        for pessoa in pessoas:
            try:
                # Recuperar as coordenadas da caixa delimitadora do rosto
                x = pessoa['source_x'][0]
                y = pessoa['source_y'][0]
                w = pessoa['source_w'][0]
                h = pessoa['source_h'][0]

                # Desenhar um retângulo ao redor do rosto
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Obter o nome da pessoa e exibi-lo na imagem
                nome = pessoa['identity'][0].split('/')[1]
                cv2.putText(frame, nome, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                registrar_log(f"Rosto identificado: {nome}")
            except Exception as e:
                registrar_log(f"Erro ao processar rosto detectado. Detalhes: {str(e)}", nivel='erro')
                pass 
        
        # Exibir o quadro resultante
        cv2.imshow('Reconhecimento Facial', frame)

        # Verificar se o botão 'q' foi pressionado para sair do programa
        if cv2.waitKey(1) & 0xFF == ord('q'):
            registrar_log("Encerrando captura de vídeo.")
            break

    # Liberar o objeto de captura de vídeo
    video.release()
    cv2.destroyAllWindows()
    registrar_log("Sistema de reconhecimento facial encerrado.")

# Realizar o reconhecimento facial em tempo real usando a webcam
configurar_log()
registrar_log("Sistema de reconhecimento facial iniciado.")
reconhecimento_facial_tempo_real()