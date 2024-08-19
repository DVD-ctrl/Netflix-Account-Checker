Aqui está o README traduzido para o português:

```markdown
# Verificador de Contas Netflix

Este script verifica a validade de contas da Netflix usando o Selenium WebDriver. Ele faz login em contas fornecidas em um arquivo e verifica se o login é bem-sucedido.

## 🚀 Funcionalidades

- **Verificação de Contas:** O script faz login em contas da Netflix usando o email e a senha fornecidos.
- **Execução Paralela:** Suporta múltiplas threads para realizar as verificações simultaneamente.
- **Registro de Contas Válidas:** Contas válidas são salvas em um arquivo `valid.txt`.

## 📦 Requisitos

- **Python 3.x**
- **Selenium**
- **Colorama**
- **ChromeDriver**

## 🔧 Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seuusuario/netflix-account-checker.git
   cd netflix-account-checker
   ```

2. **Instale as dependências:**

   ```bash
   pip install selenium colorama
   ```

3. **Baixe o ChromeDriver** compatível com sua versão do Google Chrome [aqui](https://sites.google.com/a/chromium.org/chromedriver/downloads) e coloque o executável na mesma pasta que o script.

## 📋 Uso

1. **Prepare seu arquivo de contas:** Crie um arquivo chamado `combo.txt` com cada conta no formato `email:senha`.

2. **Execute o script:**

   ```bash
   python script.py
   ```

3. **Escolha a velocidade de verificação:** Após iniciar o script, você será solicitado a escolher uma velocidade de verificação. Selecione um valor de 1 a 5, onde 1 é mais lento e 5 é mais rápido.

4. **Acompanhe o progresso:** O script imprimirá no console se as contas são válidas ou inválidas e salvará as contas válidas em `valid.txt`.

## 🔧 Exemplo de Uso

```plaintext
Escolha a velocidade de verificação (1 a 5): 3
Tentando login com: exemplo@email.com
Conta válida: exemplo@email.com
```

## ⚠️ Avisos

- O uso de múltiplas threads pode sobrecarregar o servidor da Netflix. Use com responsabilidade.
- O script pode ser bloqueado se usado de forma excessiva ou abusiva.

## 📝 Contribuições

Sinta-se à vontade para contribuir para este projeto. Envie pull requests ou abra issues se encontrar algum bug.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

Se você tiver dúvidas ou precisar de suporte, entre em contato via [Discord](https://discord.gg/dexterscript) ou [GitHub](https://github.com/seuusuario).
```

Substitua `https://github.com/seuusuario/netflix-account-checker.git` e `https://github.com/seuusuario` pelos URLs apropriados para o seu repositório e perfil do GitHub.
