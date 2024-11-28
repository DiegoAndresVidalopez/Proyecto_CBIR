import cv2
import numpy as np
from skimage.feature import local_binary_pattern
from skimage import feature

class FeatureExtractors:
    def __init__(self, image):
        self.image = image
    
    def extract_orb_features(self):
      
        # Crear el detector ORB
        orb = cv2.ORB_create()
        
        # Detectar puntos clave y calcular los descriptores
        keypoints, descriptors = orb.detectAndCompute(self.image, None)
        
        print(f"Se detectaron {len(keypoints)} puntos clave utilizando ORB.")
        
        return keypoints, descriptors
    

    def extract_lbp_features(self, radius=1, n_points=8):
       
        # Convertir a escala de grises si no lo está
        if len(self.image.shape) > 2:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            gray_image = self.image
        
        # Aplicar LBP
        lbp = local_binary_pattern(gray_image, n_points, radius, method="uniform")
        
        # Calcular el histograma de los valores LBP
        lbp_hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, n_points + 3), range=(0, n_points + 2))
        
        # Normalizar el histograma
        lbp_hist = lbp_hist.astype("float")
        lbp_hist /= (lbp_hist.sum() + 1e-6)
        
        print("Características LBP extraídas.")
        
        return lbp_hist
    
    
    def extract_hog_features(self, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=False):
      
        # Convertir a escala de grises si no lo está
        if len(self.image.shape) > 2:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            gray_image = self.image
        
        # Extraer las características HOG
        hog_features, hog_image = feature.hog(gray_image, pixels_per_cell=pixels_per_cell, cells_per_block=cells_per_block, block_norm='L2-Hys', visualize=visualize)
        
        print("Características HOG extraídas.")
        
        if visualize:
            return hog_features, hog_image
        else:
            return hog_features
        
