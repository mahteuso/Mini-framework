# Mini-framework

Mini-framwork |- framah -| baseado na arquitetura do framwork Flask que é um dos principais frameworks para desenvolvimento web com Python.

1) Foi criada uma classe para representar a app do nosso framework
2) Ao inicializar os objetos essenciais de um framework temos:
    - Mapa de roteamento de URLs
    - Configuração de template
    - Ambiente do motor de templates
4) Criamos um decorator para registar novas URLs, porém foi utilizado rotas com regex.
5) Geramos um método para renderizar templates.
6) A aplicação wsgi foi implementada em um método __call__
7) Temos um método run para executar a aplicação

-----------------------------------------------------------------------------------------------

Conclusão:

-----------------------------------------------------------------------------------------------
Criar um framework para desenvolvimento web com Pyhton é um desafio, pois muito mais coisas além da implementação básicas devem ser feitas.

- Facilidade no registro de rotas
- Segurança e autenticação
- Sessões e Cookies
- Execução assincrona



