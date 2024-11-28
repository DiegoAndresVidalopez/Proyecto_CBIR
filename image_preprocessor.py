import cv2

class ImagePreprocessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.preprocessed_image = None
    
    #carga la imagen desde la ruta del archivo
    def load_image(self):
        self.image = cv2.imread(self.image_path)
        if self.image is None:
            raise ValueError(f"No se pudo cargar la imagen desde {self.image_path}")
        print(f"Imagen cargada desde {self.image_path}")
    

    #Aplica preprocesamiento: escala de grises, desenfoque, umbral y dilatación 
    #posiblemente modificar esta parte hacer varias pruebas
    def preprocess(self):
        
        if self.image is None:
            raise ValueError("Imagen no cargada. Usa load_image primero.")
        
        # Convertir a escala de grises
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        
        # Desenfoque para reducir el ruido
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        
        # Umbral binario
        _, binary_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)
        
        # Dilatación para cerrar huecos en los bordes
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        self.preprocessed_image = cv2.dilate(binary_image, kernel, iterations=1)
        print("Preprocesamiento completado.")
        return self.preprocessed_image