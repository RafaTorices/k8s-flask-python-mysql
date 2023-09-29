# Ejercicio simulacion proyecto k8s
# Despliegue de una aplicación flask con mysql en kubernetes
# Ejercicio de clase de KeepCoding

### Rafael Torices
**_Desplegar en Kubernetes el flask counter con mysql._**

**_Requisitos:_**
Configurar un secret con la contraseña root de mysql

**_Ejecución:_**
Desplegar todos los ficheros yaml mediante el comando:
kubectl apply -f .

**_Comprobación:_**

Para comprobar que se ha desplegado correctamente, ejecutar el comando:
`kubectl get all`


Hacer un port-forward hacia un pod de la aplicación:
`kubectl port-forward <pod> 5000:5000`


Comprobar que la aplicación funciona correctamente en la url:
`http://localhost:5000`


O mediante el comando:
`curl http://localhost:5000`




