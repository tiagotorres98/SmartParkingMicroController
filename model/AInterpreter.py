class AInterpreter:

    def dePara(self, comands):
        lista = [0, 0, 0]
        for i in range(len(comands)):
            if comands[i] == 'e':
                # print('vaga 1 estacionada')
                lista[0] = 1
            if comands[i] == 'f':
                # print('vaga 1 não estacionada')
                lista[0] = 0

            if comands[i] == 'c':
                # print('vaga 2 estacionada')
                lista[1] = 1
            if comands[i] == 'd':
                # print('vaga 2 não estacionada')
                lista[1] = 0

            if comands[i] == 'a':
                # print('vaga 3 estacionada')
                lista[2] = 1
            if comands[i] == 'b':
                # print('vaga 3 não estacionada')
                lista[2] = 0

        return lista
