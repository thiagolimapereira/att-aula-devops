import unittest
import json
from sistema_academico import SistemaAcademico

class TestSistemaAcademico(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaAcademico()

    def test_calcular_media(self):
        # Deve retornar 8.0
        self.assertEqual(self.sistema.calcular_media([8, 8, 8]), 8.0, "Erro: O cálculo da média está incorreto.")

    def test_verificar_aprovacao_limite(self):
        # Aluno com média 6.0 e 75% de presença deve ser aprovado
        self.assertEqual(self.sistema.verificar_aprovacao(6.0, 75), "Aprovado", "Erro: Regra de aprovação falhou no limite da nota/frequência.")
        
    def test_verificar_reprovacao_frequencia(self):
        # Aluno com média 10, mas 74% de presença, deve reprovar
        self.assertEqual(self.sistema.verificar_aprovacao(10.0, 74), "Reprovado", "Erro: Regra de aprovação falhou na frequência.")

    def test_registro_presenca(self):
        # Valida se o trio preencheu o arquivo de presença
        with open("presenca_trio.json", "r") as f:
            dados = json.load(f)
        
        for chave, valor in dados.items():
            self.assertNotEqual(valor, "NOME_AQUI", f"Erro: O trio esqueceu de preencher o {chave} no arquivo JSON.")
            self.assertTrue(len(valor.strip()) > 0, "Erro: O nome não pode estar vazio.")

if __name__ == '__main__':
    unittest.main()