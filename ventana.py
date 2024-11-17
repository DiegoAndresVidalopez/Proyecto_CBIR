import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QSlider, QVBoxLayout,QHBoxLayout, QGridLayout, QComboBox, QSplitter, QFrame, QSizePolicy,QFileDialog 
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

#coneccion base de datos 
from connect_database import ConnectDatabase

class Ventana(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):

         # Crear el layout principal
        #layout_principal = QVBoxLayout()
        layout_principal = QHBoxLayout()
        layout_principal.setContentsMargins(0, 0, 0, 0)  # Eliminar márgenes para ocupar todo el espacio
        

        # Crear el splitter para dividir la pantalla verticalmente
        splitter = QSplitter(Qt.Orientation.Horizontal)

        #seccion izquierda: subir imagen, slider y otras opciones
        seccion_izquierda = QWidget()
        layout_izquierda = QVBoxLayout(seccion_izquierda)
        layout_izquierda.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        

        # QLabel para la imagen subida
        # Reemplazo de QLabel para la imagen subida por una imagen personalizada
        self.imagen_label = QLabel(self)
        pixmap = QPixmap("carton.jpg")  # Reemplaza con la ruta de tu imagen
        pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)  # Escalar la imagen manteniendo la proporción
        self.imagen_label.setPixmap(pixmap)
        self.imagen_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imagen_label.setStyleSheet("margin-top:40%; margin-bottom:20%")

        # Botón para subir imagen
        btn_subir_imagen = QPushButton("Subir imagen")
        btn_subir_imagen.clicked.connect(self.subir_imagen)  # Conectar el botón a la función para subir imagen
        btn_subir_imagen.setStyleSheet("background-color: red; color: white; border-radius:5px; padding-top:10px; padding-bottom:10px; font-weight:bold; cursor:pointer")

        # Slider para cantidad de imágenes similares
        slider_label = QLabel("Cantidad imágenes similares", self)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(2)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(1)
        slider_label.setStyleSheet("margin-top:30%;")

        # Conectar el slider a la función que actualiza el valor
        #self.slider.valueChanged.connect(self.actualizar_valor_slider)

        # QLabel para mostrar el valor actual del slider
        self.valor_slider_label = QLabel("2", self)

        # Conectar el slider a la función que actualiza el valor
        self.slider.valueChanged.connect(self.actualizar_valor_slider)

        # Layout para slider
        layout_slider = QVBoxLayout()
        layout_slider.addWidget(slider_label)
        layout_slider.addWidget(self.slider)
        layout_slider.addWidget(self.valor_slider_label)

         # Botón para subir imagen
        btn_procesar = QPushButton("Procesar")
        btn_procesar.clicked.connect(self.procesar_imagenes)  # Conectar el botón a la función procesar
        btn_procesar.setStyleSheet("background-color: lightblue; color: black; border-radius:5px; padding-top:10px; padding-bottom:10px; font-weight:bold; cursor:pointer")

        # Añadir widgets a la sección izquierda
        layout_izquierda.addWidget(self.imagen_label)
        layout_izquierda.addWidget(btn_subir_imagen)
        layout_izquierda.addLayout(layout_slider)

        layout_izquierda.addWidget(btn_procesar)

        # Configurar la sección izquierda para que se ajuste a sus elementos
        seccion_izquierda.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
       

        #splitter.setHandleWidth(5)  # Ancho de la línea divisoria
        #splitter.setStyleSheet("QSplitter::handle { background-color: black }")  # Color negro

        # Sección central: resultados de clasificación
        self.seccion_central = QWidget()
        self.layout_central = QVBoxLayout(self.seccion_central)

        # Título
        self.titulo_resultados = QLabel("RESULTADOS CLASIFICACIÓN")
        self.titulo_resultados.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_resultados.setStyleSheet("margin-bottom:20%; magin-top:30%; font-weight:bold;")

        # Crear grid layout para las clases
        self.grid_layout = QGridLayout()

        # Añadir imágenes y textos de clase a la cuadrícula
        for i in range(2):
            for j in range(3):
                # imagen_clase = QLabel(self)
                # imagen_clase.setFixedSize(150, 150)
                # imagen_clase.setStyleSheet("border: 1px solid black; margin-bottom:10%")
                # grid_layout.addWidget(imagen_clase, i, j)

                # # Texto debajo de cada imagen
                # #texto_clase = QLabel(f"Clase {i * 3 + j + 1} %")
                # texto_clase = QLabel("hola")
                # #grid_layout.addWidget(texto_clase, i + 2, j, alignment=Qt.AlignmentFlag.AlignCenter)
                # grid_layout.addWidget(texto_clase, i, j)  # El texto va en la fila siguiente a la imagen
                  # Cargar la imagen personalizada
                    imagen_clase = QLabel(self)
                    pixmap = QPixmap("carton.jpg")
                    pixmap = pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)  # Escalar la imagen
                    imagen_clase.setPixmap(pixmap)
                    self.grid_layout.addWidget(imagen_clase, i * 2, j)  # La imagen se pone en la fila "i*2"

                    # Añadir el texto debajo de cada imagen
                    texto_clase = QLabel("hola", self)
                    texto_clase.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.grid_layout.addWidget(texto_clase, i * 2 + 1, j)  # El texto va en la fila siguiente a la imagen
                    self.grid_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Etiqueta de categoría posible
        categoria_label = QLabel("CATEGORÍA POSIBLE: Plástico")
        #categoria_label.setStyleSheet("border: 1px solid black; background-color: lightgray;")
        categoria_label.setStyleSheet("border: 1px solid black; background-color: lightgray; max-height: 20%px; border-radius:5px; padding-top:10px; padding-bottom:10px; font-weight:bold; margin-top:20%; border:none")
        categoria_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Añadir todo al layout central
        self.layout_central.addWidget(self.titulo_resultados)
        self.layout_central.addLayout(self.grid_layout)
        self.layout_central.addWidget(categoria_label)

        self.layout_central.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Sección derecha: evaluación del usuario
        seccion_derecha = QWidget()
        layout_derecha = QVBoxLayout(seccion_derecha)

        # Título evaluación
        titulo_evaluacion = QLabel("EVALUACIÓN DEL USUARIO")
        titulo_evaluacion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_evaluacion.setStyleSheet("font-weight:bold; margin-bottom:10%; margin-top:20%")

        # Combobox para evaluación del usuario
        combo_evaluacion = QComboBox()
        combo_evaluacion.addItems(["Seleccione una opción", "Correcto", "Incorrecto"])

        # Añadir todo al layout derecho
        layout_derecha.addWidget(titulo_evaluacion)
        layout_derecha.addWidget(combo_evaluacion)
        layout_derecha.setAlignment(Qt.AlignmentFlag.AlignTop)


        # Añadir las secciones al splitter
        splitter.addWidget(seccion_izquierda)
        splitter.addWidget(self.seccion_central)
        splitter.addWidget(seccion_derecha)

        # Establecer proporciones iniciales: la sección central será más grande
        splitter.setSizes([200, 400, 100])

        # Añadir el splitter al layout principal
        layout_principal.addWidget(splitter)

        # Asignar el layout principal a la ventana
        self.setLayout(layout_principal)

        #recibe pocicion en x, pocicion en y, ancho, alto
        #self.setGeometry(100,100,800,500)
        self.setGeometry(50,50,600,600)
        self.setWindowTitle("CBIR RESIDUOS")
        self.show()


        #crear un objeto coneccion a base de datos
        self.db = ConnectDatabase()

        #si queremos tomar elementos de la interfaz y conectarlos a la svariables
        # self.student_id = self.ui.lineedit #aqui va el id del campo
        #self.db.add_info()

    
    def subir_imagen(self):
        # Abrir un cuadro de diálogo para seleccionar la imagen
        ruta_imagen, _ = QFileDialog.getOpenFileName(self, "Subir Imagen", "", "Imágenes (*.png *.xpm *.jpg *.jpeg)")

        if ruta_imagen:  # Si se seleccionó una imagen
            pixmap = QPixmap(ruta_imagen)  # Cargar la imagen
            pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)  # Escalar la imagen
            self.imagen_label.setPixmap(pixmap)  # Establecer la imagen en el QLabel


    def actualizar_valor_slider(self, valor):
        valores_posibles = [2,3,5]
        valor_mostrado = valores_posibles[valor]
        self.valor_slider_label.setText(f"{valor_mostrado}")
        #self.valor_slider_label.setText(f"Valor: {valor_mostrado}")

    def limpiar_grid_layout(self, layout):
        for i in reversed(range(layout.count())):
            widget_to_remove = layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.deleteLater()  # Asegura la eliminación del widget
                layout.removeWidget(widget_to_remove)
    
    def procesar_imagenes(self):

        self.limpiar_grid_layout(self.grid_layout)

        # Leer el valor del slider
        valor_slider = self.slider.value()
        valores_posibles = [2, 3, 5]
        num_imagenes = valores_posibles[valor_slider]

        # Definir el número máximo de columnas
        max_columnas = 3

        # Añadir las imágenes al grid layout
        for index in range(num_imagenes):
            fila = index // max_columnas
            columna = index % max_columnas

            # Crear y agregar la imagen
            imagen_clase = QLabel(self)
            pixmap = QPixmap("carton.jpg")
            pixmap = pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)
            imagen_clase.setPixmap(pixmap)
            self.grid_layout.addWidget(imagen_clase, fila * 2, columna)  # La imagen se pone en la fila "fila * 2"

            # Crear y agregar el texto debajo de la imagen
            texto_clase = QLabel(f"Clase {index + 1}", self)
            texto_clase.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.grid_layout.addWidget(texto_clase, fila * 2 + 1, columna)  # El texto va en la fila siguiente a la imagen

        # Actualizar la sección central con el grid layout modificado
        self.layout_central.addLayout(self.grid_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana =  Ventana()
    ventana.showMaximized()  # Abre la ventana maximizada
    sys.exit(app.exec())

