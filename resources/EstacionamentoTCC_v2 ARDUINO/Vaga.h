class Vaga{
  
  private:
    int sensorTrigger = 0;                                  //Variável de Inicialização da Porta que envia o sinal do sensor
    int sensorEcho = 0;                                     //Variável de Inicialização da Porta que recebe o sinal do sensor
    int ledVerde = 0;                                       //Variável de Inicialização da Porta para o LED verde
    int ledVermelho = 0;                                    //Variável de Inicialização da Porta para o LED vermelho
    char estacionado = ' ';                                 //Variável de Inicialização do caractere que define se tem carro estacionado na vaga
    char naoEstacionado = ' ';                              //Variável de Inicialização do caractere que define se não tem carro estacionado na vaga
    
    //Configurações do Sensor
    int distanciaMinima = 1;                                //Definição da distância mínima do carro ao sensor
    int distanciaMaxima = 10;                               //Definição da distância máxima do carro ao sensor
    int tempoTrigger  = 58;                                 //Definição do tempo base para calcular o tempo e retornar em cm
    
    // Variáveis para retorno ou cálculo;
    int distanciaObjSensor = 0;                             //Variável de Inicialização do valor da distancia do carro ao sensor

  public:
      //Método construtor - Inserindo os dados nas variáveis de inicialização quando um objeto dessa classe for instanciado
      Vaga(int sTrigger,int sEcho, int lVerde, int lVermelho, int numVaga, char est, char naoEst){
        this->sensorTrigger = sTrigger;
        this->sensorEcho = sEcho;
        this->ledVerde = lVerde;
        this->ledVermelho = lVermelho;
        this->estacionado = est;
        this->naoEstacionado = naoEst;
      }
      
      //Método que define as portas que cada componente vai ocupar no arduino 
      void definePinMode(){
          pinMode(this->sensorTrigger,OUTPUT);              //Envia Sinal
          pinMode(this->sensorEcho, INPUT);                 //Recebe Sinal
          pinMode(this->ledVerde, OUTPUT);                  //Envia Sinal
          pinMode(this->ledVermelho,OUTPUT);                //Envia Sinal
        }

      int getSensorValues(){
        
        digitalWrite(this->sensorTrigger,LOW);              //Emissor fica desativado
        delayMicroseconds(5);                               //Aguarda 5 microsegundos 
        digitalWrite(this->sensorTrigger,HIGH);             //Emissor envia sinal IR para colidir com o objeto
        delayMicroseconds(10);                              //Aguarda 10 microsegundos
        digitalWrite(this->sensorTrigger,LOW);              //Emissor fica desativado
        
        return pulseIn(this->sensorEcho,HIGH)/tempoTrigger; //retorna em CM a distancia do objeto do sensor
      }
      
      char isEstacionado(){
        char value;               
        //Se a distancia do objeto estiver entre a distancia mínima e máxima:
        if(getSensorValues() > distanciaMinima && getSensorValues() < distanciaMaxima){
          acendeLedVerde();                                 //Led Verde Acende
          apagaLedVermelho();                               //Led Vermelho Apaga
          value = this->estacionado;                        //Retorna que o caractere que define que está estacionado
          return value;                                     //Retorna que o caractere que define que está estacionado  
        }
        else{
          acendeLedVermelho();                              //Led Vermelho Acende
          apagaLedVerde();                                  //Led Verde Apaga
          value = this->naoEstacionado;                     //Retorna que o caractere que define que não está estacionado
          return value;                                     //Retorna que o caractere que define que não está estacionado
        }
      }
      
      void acendeLedVerde(){
          digitalWrite(this->ledVerde,HIGH);                //Método que Liga o Led Verde
      }

      void apagaLedVerde(){
         digitalWrite(this->ledVerde,LOW);                  //Método que Apaga o Led Verde
      }

      void acendeLedVermelho(){
          digitalWrite(this->ledVermelho,HIGH);             //Método que Liga o Led Vermelho
      }

      void apagaLedVermelho(){
         digitalWrite(this->ledVermelho,LOW);               //Método que Apaga o Led Vermelho
      }

      void acendeLeds(){                                    //Método que liga os dois Leds
        digitalWrite(this->ledVerde,HIGH);
        digitalWrite(this->ledVermelho,HIGH);
      }

      void apagaLeds(){                                     //Método que apaga os dois Leds
        digitalWrite(this->ledVermelho,LOW);
        digitalWrite(this->ledVerde,LOW);
      }
};
