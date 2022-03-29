class Main {
  public static void main(String[] args) {
  
    Cadastro<String> cliente = new Cadastro<String>("Teste", "Sobrenome", "18", "Rua Teste nº 123", "teste.sobrenome@email.com");
    cliente.imprime();
  }
}