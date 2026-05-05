import unittest
import json
from sistema_academico import SistemaAcademico

class TestSistemaAcademico(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaAcademico()

    def test_calcular_media(self):
        self.assertEqual(self.sistema.calcular_media([8, 8, 8]), 8.0, "Erro: O cálculo da média está incorreto.")

    def test_verificar_aprovacao_limite(self):
        self.assertEqual(self.sistema.verificar_aprovacao(6.0, 75), "Aprovado", "Erro: Regra de aprovação falhou no limite da nota/frequência.")
        
    def test_verificar_reprovacao_frequencia(self):
        self.assertEqual(self.sistema.verificar_aprovacao(10.0, 74), "Reprovado", "Erro: Regra de aprovação falhou na frequência.")

    def test_registro_presenca(self):
        # Lê o novo arquivo de presença como uma lista
        try:
            with open("presenca.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
        except FileNotFoundError:
            self.fail("Erro: Arquivo presenca.json não encontrado. Você renomeou ou apagou o arquivo?")
        
        self.assertIsInstance(dados, list, "Erro: O arquivo JSON deve conter uma lista de nomes ex: [\"Nome 1\", \"Nome 2\"].")
        self.assertTrue(len(dados) > 0, "Erro: A lista de presença não pode estar vazia.")

        for nome in dados:
            self.assertNotEqual(nome, "NOME_AQUI", "Erro: Substitua 'NOME_AQUI' pelos nomes reais dos integrantes.")
            self.assertTrue(len(nome.strip()) > 0, "Erro: O nome não pode ficar em branco.")

if __name__ == '__main__':
    unittest.main()