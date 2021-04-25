class Main {
  public static void main(String[] args) {
    CalculadoraAninhada.Divisao div = new CalculadoraAninhada(6, 7).new Divisao();
    
    System.out.println(div.dividir());
  }
}