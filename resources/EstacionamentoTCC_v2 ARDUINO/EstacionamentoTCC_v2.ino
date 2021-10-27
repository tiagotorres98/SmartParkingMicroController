#include "Vaga.h"
#include "Cancela.h"


String pacote = "";                                                       //Pacote que é recebido do python
String pacoteOut = "";                                                    //Pacote que é enviado para o python

char vetor[20];                                                           //Pacote que foi recebido e transformado em vetor

Vaga vaga3(13, 8, 2, 9, 1, 'a', 'b');                                     //Instanciando a vaga 3
Vaga vaga2(11, 10, 4, 5, 2, 'c', 'd');                                    //Instanciando a vaga 2
Vaga vaga1(13, 12, 6, 7, 2, 'e', 'f');                                    //Instanciando a vaga 1
Cancela cancela;                                                          //Instanciando a cancela

void setup() {
  Serial.begin(9600);                                                     //Define a velocidade de comunicação
  vaga1.definePinMode();                                                  //Define os Pinos da vaga 1
  vaga2.definePinMode();                                                  //Define os Pinos da vaga 2
  vaga3.definePinMode();                                                  //Define os Pinos da vaga 2
  cancela.defineAttach();                                                 //Define Pino da Cancela
}

void loop() {
  Serial.flush();                                                         //Limpa buffer
  getPacote();                                                            //Pega dados que veio do python e transforma em pacote
  
  delay(100);                                                             //delay de 100 milisegundos
  sendValues();                                                           //envia pacote para o python
  
  delay(100);                                                             //delay e 100 milisegundos
  Serial.flush();                                                         //Limpa buffer
  
  resetValues();                                                          //Limpa os pacotes
  Serial.print('_');                                                      //envia o "_" para sempre manter o fluxo de atualização
  delay(1000);                                                            //delay de 1 segundo
}

void getPacote(){
   do {                                                                   //Laço Do-While
    delay(10);                                                            //delay de 10 milisegundos                                         
    if (Serial.available() > 0) {                                         //se houver algum bit para ser lido
      char c = Serial.read(); //gets one byte from serial buffer          //O bit será adicionado no char
      pacote += c; //makes the string readString                          //Incrementa os bits na string
    }
  } while (Serial.available());                                           //executa enquanto houver bits para serem lidos
}

void sendValues(){                                                          
    if (pacote.length() > 0) {                                            //Se o pacote recebido tiver mais de 0 caracteres
    pacote.toCharArray(vetor, sizeof(vetor));                             //Transforma o pacote recebido em array
    for(int i=0;i<=(pacote.length());i++){                                //Laço FOR que será utilizado para percorrer o array
         switch(vetor[i]){                                                
            case '4':                                                     //Caso no pacote haja o valor 4
              cancela.abreCancela();                                      //A cancela abre
              break;
            case '5':                                                     //Caso no pacote haja o valor 5
              cancela.fechaCancela();                                     //A cancela fecha
              break;
          }
        switch(vetor[i]){
            case '1':                                                    //Caso no pacote haja o valor 1
              pacoteOut += vaga1.isEstacionado();                        //Envia para o python que a vaga 1 está ocupada
              break;
            case '2':                                                    //Caso no pacote haja o valor 2
              pacoteOut += vaga2.isEstacionado();                        //Envia para o python que a vaga 2 está ocupada
              break;
            case '3':                                                    //Caso no pacote haja o valor 2
              pacoteOut += vaga3.isEstacionado();                        //Envia para o python que a vaga 2 está ocupada
              break;
          }
      }
  }
  Serial.print(pacoteOut);                                               //Envia o pacote pelo SERIAL
}


void resetValues(){
    pacote = "";                                                         //Reseta o pacote de entrada
  pacoteOut = "";                                                        //Reseta o pacote de Saída
  }
