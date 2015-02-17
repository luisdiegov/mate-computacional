for k = 1:6
  x = linspace(0, 4*pi, 2^(k+1)+1);
  subplot(3,2,k), plot(x, cos(3*x)-2*sin(x))
  axis([0, 4*pi, -1.5, 1.5])
end

# El c�digo genera 6 gr�ficas diferentes, las cuales representan la misma
# funci�n, pero cada vez se va suavizando m�s la gr�fica, esto debido a 
# que los espacios entre los puntos se van disminuyendo. 

# Si hacemos el cambio dentro del subplot, la gr�fica se ensancha y se reduce
# su altura. Esto debido al tama�o en el cual el subplot ajusta la gr�fica. 

# Si se quita el comando axis, la gr�fica se dibuja hasta el mayor valor
# que se tiene en �sta y corta la gr�fica. No respeta un mismo valor de
# margen como cuando se pone el axis. 