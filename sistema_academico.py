class SistemaAcademico:
    def calcular_media(self, notas):
        if not notas:
            return 0
        # BUG 1: A divisão está errada. Está somando 1 ao tamanho da lista.
        # O correto seria apenas len(notas)
        return sum(notas) / (len(notas) + 1) 

    def verificar_aprovacao(self, media, frequencia):
        # BUG 2: A regra de aprovação da faculdade exige média >= 6.0 e frequência >= 75
        # O código está usando > 6.0 (excluindo o 6 exato) e >= 70 na frequência
        if media > 6.0 and frequencia >= 70:
            return "Aprovado"
        return "Reprovado"