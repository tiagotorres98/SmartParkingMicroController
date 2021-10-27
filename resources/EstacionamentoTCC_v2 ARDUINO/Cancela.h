#include "Servo.h"                            // Inclui a Biblioteca Servo.h 

class Cancela{
  private: 
    Servo meuservo;                           // Cria o objeto servo para programação
    int angulo = 5;                           // Define o ângulo inicial do servo motor
  public:

    Cancela(){
        fechaCancela();                       // Quando a classe é iniciada, a cancela é fechada.
    }
    
    void abreCancela(){                       //Método para abrir a cancela
        if(this->angulo < 90){                //Se o angulo do servo for menor que 90º significa que estava fechada.
            this->angulo = 90;                //Define o angulo de 90º para abrir a cancela
            this->meuservo.write(angulo);     //envia o comando para a cancela abrir
          }
      }

    void fechaCancela(){                      //Método para fechar a cancela
        if(this->angulo > 5){                 //Se o angulo do servo for maior que 5º significa que estava aberta.
            this->angulo = 5;                 //Define o angulo de 5º para fechar a cancela
            this->meuservo.write(angulo);     //envia o comando para a cancela fechar
          }
      }

      void defineAttach(){
         this->meuservo.attach(3);            //Define a porta analógica 3 no arduino para o servo motor
       }
};
