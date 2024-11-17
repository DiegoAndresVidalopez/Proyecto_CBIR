import cv2


class ContourDetector:

    #Inicializa el detector de contornos utilizando un preprocesador de imagen.
    def __init__(self, preprocessor: ImagePreprocessor):
        self.preprocessor = preprocessor
        self.contours = None
        self.hierarchy = None
    
    #Encuentra contornos en la imagen preprocesada.
    def find_contours(self):        
        # Obtener la imagen preprocesada del preprocesador
        preprocessed_image = self.preprocessor.preprocess()
        
        # Encontrar contornos
        self.contours, self.hierarchy = cv2.findContours(preprocessed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print(f"Total de contornos encontrados: {len(self.contours)}")
        return len(self.contours)
        
    def draw_contours(self):
        """Dibuja los contornos en la imagen original y devuelve la imagen con contornos."""
        if self.contours is None:
            raise ValueError("No se han encontrado contornos. Usa find_contours primero.")
        
        output_image = self.preprocessor.image.copy()
        cv2.drawContours(output_image, self.contours, -1, (0, 255, 0), 2)
        return output_image
    
    def get_hu_moments(self):
        """Calcula los momentos de Hu del contorno más grande y los retorna como un vector de características."""
        if self.contours is None or len(self.contours) == 0:
            raise ValueError("No se han encontrado contornos. Usa find_contours primero.")
        
        # Escoger el contorno más grande
        largest_contour = max(self.contours, key=cv2.contourArea)
        
        # Calcular los momentos y los momentos de Hu
        moments = cv2.moments(largest_contour)
        hu_moments = cv2.HuMoments(moments).flatten()
        
        print("Momentos de Hu calculados para el contorno más grande:", hu_moments)
        return hu_moments